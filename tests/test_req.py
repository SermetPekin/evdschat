import json
import pytest
import ctypes
from pathlib import Path
import platform

from evdschat.model.chatters import (
    get_openai_key,
    TestAI,
    get_myapi_url
)


def get_exec_file(test=False) -> Path:
    executable_name = "libpost_request.so"
    if platform.system() == "Windows":
        executable_name = "libpost_request.dll"
    return Path(".") / executable_name


def get_chatter():
    return TestAI()


@pytest.mark.skipif(not get_exec_file().exists(), reason="only tests locally")
def test_post():
    t = get_chatter()
    resp = t.post(prompt="test")
    # print(resp)
    assert resp


@pytest.mark.skipif(not get_exec_file().exists(), reason="requires C executable")
def test_post_c():
    # t = get_chatter()
    caller = get_c_fnc()
    resp = caller(prompt="Loan data", api_key=get_openai_key(), url=get_myapi_url())
    result_dict = json.loads(resp)
    r = result_dict["result"]
    res = json.loads(r)
    res["cache"] = False
    assert res["index"]


def get_c_fnc():
    class PostParams(ctypes.Structure):
        _fields_ = [
            ("url", ctypes.c_char_p),
            ("prompt", ctypes.c_char_p),
            ("api_key", ctypes.c_char_p),
            ("proxy_url", ctypes.c_char_p),
        ]

    lib_path = get_exec_file()  # check_c_executable()
    if lib_path.exists():
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
                proxy_url=proxy.encode("utf-8") if proxy else None,
            )

            return c_caller(params)

    return c_caller_main

# test_post_c()
