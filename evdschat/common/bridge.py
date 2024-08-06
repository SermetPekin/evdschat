# evdschat - An open-source Python package for enhanced data retrieval.
# Copyright (c) 2024 Sermet Pekin
# Licensed under the Creative Commons Attribution-NonCommercial 4.0 International License.
# You may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://creativecommons.org/licenses/by-nc/4.0/
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import ctypes
import os
import platform
from pathlib import Path
from importlib import resources
from .github_actions import PytestTesting
from typing import Union

def check_c_executable() -> Union[Path, bool]:
    executable_name = "libpost_request.so"
    if platform.system() == "Windows":
        executable_name = "libpost_request.dll"

    if PytestTesting().is_testing():
        executable_path = Path(".") / executable_name
    else:
        # Use importlib.resources to get the path to the executable
        try:
            with resources.path("evdschat", executable_name) as executable_path:
                if executable_path.is_file() and os.access(executable_path, os.X_OK):
                    return executable_path
        except FileNotFoundError:
            return False

    return False

lib_path = check_c_executable()
if lib_path:
    lib = ctypes.CDLL(lib_path)
    lib.post_request.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p]
    lib.post_request.restype = ctypes.c_char_p

    lib.free_memory.argtypes = [ctypes.c_void_p]
    lib.free_memory.restype = None

    def c_caller(url, prompt, api_key):
        response = lib.post_request(url, prompt, api_key)
        return ctypes.string_at(response).decode("utf-8")

    def c_caller_main(prompt, api_key, url):
        prompt = prompt.replace("\n", " ")
        url_encoded = url.encode("utf-8")
        prompt_encoded = prompt.encode("utf-8")
        api_key_encoded = api_key.encode("utf-8")

        return c_caller(url_encoded, prompt_encoded, api_key_encoded)
else:
    c_caller_main = None
