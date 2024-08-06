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


from dataclasses import dataclass, field
from abc import ABC
import os
from pathlib import Path
from typing import Union


class ErrorApiKey(BaseException): ...


@dataclass
class ApiKey(ABC):
    key: str

    def __postinit__(self):
        self.check()

    def check(self):
        if str(self.key).__len__ < 5:
            raise ErrorApiKey(f"{self.key} is not a valid key")
        return True

    def get_key(self):
        return self.key

    def set_key(self, key: str):
        self.key = key


@dataclass
class OpenaiApiKey(ApiKey):
    ...

    def check(self)-> Union[bool , None ] :
        super().__init__(self)

        if not str(self.key).startswith("sk-") and str(self.key).__len__ < 8:
            raise ErrorApiKey(f"{self.key} is not a valid key")
        return True


@dataclass
class EvdsApiKey(ApiKey): ...


@dataclass
class MistralApiKey(ApiKey): ...


def load_api_keys() -> Union[dict[str, str], None]:
    from dotenv import load_dotenv

    env_file = Path(".env")
    load_dotenv(env_file)
    openai_api_key = OpenaiApiKey(os.getenv("OPENAI_API_KEY"))
    evds_api_key = EvdsApiKey(os.getenv("EVDS_API_KEY"))
    return {
        "OPENAI_API_KEY": openai_api_key,
        "EVDS_API_KEY": evds_api_key,
    }


def get_openai_key():
    d = load_api_keys()
    return d["OPENAI_API_KEY"].key 


@dataclass
class ApiKeyManager:
    api_key: ApiKey = field(default_factory=ApiKey)
