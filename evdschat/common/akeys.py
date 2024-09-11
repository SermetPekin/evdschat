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
from typing import Union


class ErrorApiKey(Exception):
    """Exception raised for errors related to API key issues.

    Attributes:
        message (str): Explanation of the error.
    """

    def __init__(self, message="There is an issue with the provided API key."):
        self.message = message
        super().__init__(self.message)


class ApiKey(ABC):
    def __init__(self, key: str) -> None:
        self.key = key
        self.check()

    def check(self):
        if isinstance(self.key, type(None)):
            raise ErrorApiKey('Api key not set. Please see the documentation.')
        if not isinstance(self.key, str) or len(str(self.key)) < 5:
            raise ErrorApiKey(f"Api key {self.key} is not a valid key")
        return True

    def get_key(self):
        return self.key

    def set_key(self, key: str):
        self.key = key


class OpenaiApiKey(ApiKey):
    def __init__(self, key: str) -> None:
        super().__init__(key)
        self.key = key
        self.check()

    def check(self) -> Union[bool, None]:

        if not str(self.key).startswith("sk-") and len(str(self.key)) < 6:
            raise ErrorApiKey(f"{self.key} is not a valid key")
        return True


class EvdsApiKey(ApiKey): ...


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


# @dataclass

class ApiKeyManager(BaseModel):
    api_key: ApiKey = Field(default_factory=lambda: ApiKey())

    class Config:
        arbitrary_types_allowed = True

        # def __get_pydantic_core_schema__(cls, handler):
    #     # Generate a schema if necessary, or skip it
    #     return handler.generate_schema(cls)