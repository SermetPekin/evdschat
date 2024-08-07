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

import argparse
from evdschat.model.chatters import ModelAbstract, OpenAI
from ..common.github_actions import PytestTesting
from typing import TypeVar, Tuple, Union

Result = TypeVar("Result")
Notes = TypeVar("Notes")


class GotNoneFromGetter(BaseException): ...


def chat(
    prompt: str,
    getter: ModelAbstract = OpenAI(),
    debug=False,
    test=False,
    force=False,
) -> Union[Tuple[Result, Notes], None]:
    """
    Function to process the chat prompt and return the result.

    :param prompt: str - The prompt for the chat.
    :param getter: ModelAbstract - The model to use for processing the chat.
    :param debug: bool - Flag for enabling debug mode.
    :param test: bool - Flag indicating whether to run in test mode.
    :return: DataFrame or Result Instance with .data (DataFrame), .metadata (DataFrame), and .to_excel (Callable).
    """

    if not force and PytestTesting().is_testing():
        test = True

    getter.debug = debug
    getter.test = test
    res = getter(prompt)
    if isinstance(res, type(None)):
        raise GotNoneFromGetter()
    if isinstance(res, str):
        return res
    if isinstance(res, bool):
        raise ValueError(
            """
    Could not connect the evdschat API. 
    Please try again later or check documentation for
    new API URLs"""
        )
    if not isinstance(res, tuple) or len(res) != 2:
        raise ValueError(
            """
    Could not connect the evdschat API. 
    Please try again later or check documentation for
    new API URLs"""
        )
    result, notes = res
    return result, notes


def chat_console():
    """
    Console function to handle user input and produce output.

    :return: None. Outputs the result of the chat function to an Excel file specified by the user.
    """
    parser = argparse.ArgumentParser(description="Chat Console")
    parser.add_argument("prompt", type=str, help="Prompt for the chat")
    parser.add_argument(
        "file_name", type=str, help="File name for the output Excel file"
    )
    parser.add_argument("--debug", action="store_true", help="Enable debug mode")
    parser.add_argument("--test", action="store_true", help="Enable test mode")
    args = parser.parse_args()

    result, notes = chat(prompt=args.prompt, debug=args.debug, test=args.test)
    print(result)
    print(notes)
    def correct(x:str):
        if x.endswith('.xlsx') : return x 
        return f'{x}.xlsx'
    
    result.to_excel(f"{correct(args.file_name)}")


if __name__ == "__main__":
    chat_console()
