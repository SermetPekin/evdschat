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


from pydantic import BaseModel, Field
from abc import ABC
import os
from pathlib import Path
from typing import Union, Dict
import time

from evdschat.common.globals import WARNING_SLEEP_SECONDS


class ErrorApiKey(Exception):
    """Exception raised for errors related to API key issues.

    Attributes:
        message (str): Explanation of the error.
    """

    def __init__(self, message="There is an issue with the provided API key."):
        self.message = message
        super().__init__(self.message)


class ApiKey(ABC):
    def __init__(self, key: str, key_name: str = 'ApiKey') -> None:
        self.key = key
        self.key_name = key_name
        self.check()

    def __str__(self):
        return self.key

    def msg_before_raise(self):
        showApiKeyMessage(self.__class__.__name__)
        # create_env_example_file()

    def check(self):
        if isinstance(self.key, type(None)):
            raise ErrorApiKey("Api key not set. Please see the documentation.")
        if not isinstance(self.key, str) or len(str(self.key)) < 5:
            raise ErrorApiKey(f"Api key {self.key} is not a valid key")
        return True

    def get_key(self):
        return self.key

    def set_key(self, key: str):
        self.key = key


def sleep(number: int):
    time.sleep(number)


def showApiKeyMessage(cls_name: str) -> None:
    msg = f"""
   {cls_name} not found. 
   
   create `.env` file and put necessary API keys for EVDS and {cls_name}
   see documentation for details.
   
   """

    print(msg)
    sleep(WARNING_SLEEP_SECONDS)


def write_env_example(file_name: Path):
    content = (
        "\nOPENAI_API_KEY=sk-proj-ABCDEFGIJKLMNOPQRSTUXVZ\nEVDS_API_KEY=ABCDEFGIJKLMNOP"
    )
    with open(file_name, "w") as f:
        f.write(content)
        print("Example .env file was created.")
        sleep(WARNING_SLEEP_SECONDS)


def create_env_example_file():
    file_name = Path(".env")
    if not file_name.exists():
        write_env_example(file_name)


class OpenaiApiKey(ApiKey):
    def __init__(self, key: str) -> None:
        super().__init__(key)
        self.key = key
        self.key_name = 'openai_api_key'
        # self.check()

    def check(self, raise_=True) -> Union[bool, None]:
        if not str(self.key).startswith("sk-") and len(str(self.key)) < 6:
            self.msg_before_raise()
            if raise_:
                raise ErrorApiKey(f"{self.key} is not a valid key")
            return False
        return True


class EvdsApiKey(ApiKey): ...


class MistralApiKey(ApiKey): ...


def load_api_keys() -> Dict[str, OpenaiApiKey | EvdsApiKey]:
    from dotenv import load_dotenv

    env_file = Path(".env")
    load_dotenv(env_file)
    openai_api_key = OpenaiApiKey(os.getenv("OPENAI_API_KEY"))
    evds_api_key = EvdsApiKey(os.getenv("EVDS_API_KEY"))
    return {
        "OPENAI_API_KEY": openai_api_key,
        "EVDS_API_KEY": evds_api_key,
    }


def load_api_keys_string() -> Dict[str, str]:
    from dotenv import load_dotenv

    env_file = Path(".env")
    load_dotenv(env_file)
    openai_api_key = os.getenv("OPENAI_API_KEY")
    evds_api_key = os.getenv("EVDS_API_KEY")
    return {
        "OPENAI_API_KEY": openai_api_key,
        "EVDS_API_KEY": evds_api_key,
    }


def get_openai_key() -> OpenaiApiKey:
    d = load_api_keys()
    return d["OPENAI_API_KEY"]


def get_openai_key_string() -> str | None:
    d = load_api_keys_string()
    return d["OPENAI_API_KEY"]


class ApiKeyManager(BaseModel):
    api_key: ApiKey = Field(default_factory=lambda: ApiKey())

    class Config:
        arbitrary_types_allowed = True
