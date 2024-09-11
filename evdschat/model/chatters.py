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

import json
import traceback
from typing import Callable, Any, Tuple, Union
from abc import ABC
import requests
from evdspy import get_series_exp
from evdschat.common.akeys import get_openai_key
from dataclasses import dataclass
from evdschat.common.globals import global_mock
from ..common.bridge import c_caller_main

import os
from pathlib import Path


from evdschat.core.result import ResultChat, create_result
from evdschat.core.result import Status


def get_myapi_url():
    from dotenv import load_dotenv

    load_dotenv(Path(".") / ".env")

    CHAT_API_URL = os.getenv(
        "CHAT_API_URL", "https://evdspychat-dev2-1.onrender.com/api/ask"
    )
    return CHAT_API_URL


@dataclass
class ModelAbstract(ABC):
    retrieve_fnc: Callable = get_series_exp
    request_fnc: Callable = requests.post
    model: str = "gpt-4"
    api_key: str = get_openai_key()
    debug = True
    test = False

    def parse(self, prompt) -> dict[str, str]:

        return {"prompt": prompt, "model": self.model, "openai_api_key": self.api_key}

    def defaultOptions(self) -> str:
        return get_myapi_url()

    def post(self, prompt: str) -> Union[dict, bool]:

        if self.debug:
            return str(self)
        response = self.request_fnc(self.defaultOptions(), json=self.parse(prompt))
        return self.post_helper(response)

    def obscure(self, string: str) -> str:
        nstr = []
        for i, char in enumerate(string.split()):
            if i % 3 == 1:
                nstr.append(char)
            else:
                nstr.append("*")

        return "".join(nstr)

    def __str__(self):
        api_key = self.obscure(self.api_key)

        return f"""

prompt : {self.parse('<prompt|>')}
fnc : {self.request_fnc}
key : {api_key}
api url : {get_myapi_url() }
"""

    def mock_req(self, prompt) -> dict[str, str]:
        return global_mock()

    def check_permitted(self, key: str, permitted=None) -> bool:
        if not permitted:
            permitted = ["start_date", "aggregate", "frequency" "cache"]
        return key in permitted

    def permitted_dict(self, kw: dict, permitted: None) -> Tuple[dict, str]:
        new_dict = {}

        for k, v in kw.items():
            if self.check_permitted(k, permitted):
                new_dict[k] = v

        return new_dict

    def eval_real(self, kw, permitted=None) -> tuple[ResultChat, str]:
        """eval_real"""
        notes = kw.get("notes", "")
        try:
            result = self.retrieve_fnc(
                kw["index"], **self.permitted_dict(kw, permitted)
            )
            return create_result(result, status=Status.success), notes
        except Exception:
            traceback.print_exc()

        return self.failed_result()

    def failed_result(self):
        """failed_result"""
        return create_result(None, status=Status.failed, reason="Eval failed")

    def eval(self, kw: dict, permitted=None) -> Tuple[Any, str]:
        """eval"""
        index = kw.get("index", None)

        if not index:
            return self.failed_result(), str("")
        return  self.eval_real(kw, permitted)

    def decide_caller(self):
        """decide_caller"""
        if self.test:
            return self.mock_req
        if callable(c_caller_main):
            return self.post_c
        return self.post

    def __call__(self, prompt, **kwargs) -> Union[Tuple[Any, str], bool]:

        if self.debug:
            return str(self)
        caller_fnc = self.decide_caller()
        res = caller_fnc(prompt)
        if res:
            return self.eval(res)
        return False

    def json_loads(self, result) -> dict[str, str]:
        try:
            res = json.loads(result)
        except Exception:
            self._raise()
        return res

    def post_helper(self, response) -> dict[str, str]:

        if response.status_code == 200:
            data = response.json()
            result_code = data.get("result")

            if result_code:
                result_code = result_code.replace("'", '"').replace("=", ":")
                result_dict = self.json_loads(result_code)
                result_dict["cache"] = False
                return result_dict
        self._raise()

    def _raise(self, *args):
        raise ValueError("Could not read return content form Node")


@dataclass
class OpenAI(ModelAbstract):
    """OpenAI"""

    def post_c(self, prompt: str , caller = c_caller_main ) -> dict[str, str]:
        resp = caller(prompt, get_openai_key(), self.defaultOptions())
        result_dict = json.loads(resp)
        r = result_dict["result"]
        res = json.loads(r)
        res["cache"] = False
        return res


@dataclass
class TestAI(OpenAI):
    """TestAI"""
