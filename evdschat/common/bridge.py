import ctypes
import os
import platform
from pathlib import Path
from importlib import resources
from typing import Union
from .github_actions import PytestTesting 

class PostParams(ctypes.Structure):
    _fields_ = [
        ("url", ctypes.c_char_p),
        ("prompt", ctypes.c_char_p),
        ("api_key", ctypes.c_char_p),
        ("proxy_url", ctypes.c_char_p)
    ]

def get_exec_file(test = False ) -> Path :

    executable_name = "libpost_request.so"
    if platform.system() == "Windows":
        executable_name = "libpost_request.dll"

    if test or PytestTesting().is_testing():
        executable_path = Path(".") / executable_name
        if executable_path.is_file() : 
            return executable_path
    return False  
        
def check_c_executable(test = False ) -> Union[Path, bool]:
    executable_name= get_exec_file(test )    
    if not executable_name:
        return False 
    try:
        with resources.path("evdschat", executable_name) as executable_path:
            if executable_path.is_file() and os.access(executable_path, os.X_OK):
                return executable_path
    except FileNotFoundError:
        return False

lib_path = check_c_executable()
if lib_path:
    lib = ctypes.CDLL(lib_path)
    
    lib.post_request.argtypes = [ctypes.POINTER(PostParams)]
    lib.post_request.restype = ctypes.c_char_p

    lib.free_memory.argtypes = [ctypes.c_void_p]
    lib.free_memory.restype = None

    def c_caller(params):
        response = lib.post_request(ctypes.byref(params))
        result = ctypes.string_at(response).decode("utf-8")
        return result

    def c_caller_main(prompt, api_key, url, proxy=None):
        prompt = prompt.replace("\n", " ")
        
        params = PostParams(
            url=url.encode("utf-8"),
            prompt=prompt.encode("utf-8"),
            api_key=api_key.encode("utf-8"),
            proxy_url=proxy.encode("utf-8") if proxy else None
        )

        return c_caller(params)
    
    
else:
    c_caller_main = None
