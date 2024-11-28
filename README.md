[![Python package](https://github.com/SermetPekin/evdschat/actions/workflows/python-package.yml/badge.svg?1)](https://github.com/SermetPekin/evdschat/actions/workflows/python-package.yml?1) [![PyPI](https://img.shields.io/pypi/v/evdschat)](https://img.shields.io/pypi/v/evdschat) ![](https://img.shields.io/badge/python-3.10+-blue.svg)   [![Downloads](https://static.pepy.tech/badge/evdschat)](https://pepy.tech/project/evdschat) [![Downloads](https://static.pepy.tech/badge/evdschat/month)](https://pepy.tech/project/evdschat) [![Downloads](https://pepy.tech/badge/evdschat/week)](https://pepy.tech/project/evdschat)

# evdschat

**evdschat** is an open-source Python package designed to enhance the **evdspy** package by allowing users to interact with the **evdschat Application**. This Node.js project aims to provide the most specific and accurate data users request during conversations, based on arguments such as start date, end date, and aggregation type, as described in the evdspy Python package. However, since it is a Generative AI application, it may sometimes be incorrect. Please be aware of the tickets and data it provides. To minimize inconvenience, the application will be tailored to indicate which tickets and which names correspond to the provided data. With further improvements, the application's mistakes might become less frequent in future versions.

As an experimental project, this package seeks to create an experimental bridge between the evdspy package and the EVDS API of the Central Bank of the Republic of Türkiye.

## Usage

```python
from evdschat import chat 

prompt = '''
Can you give me reserves data since 2010 can you aggregate it monthly by average? Thanks. 
'''

result, notes = chat(prompt, test=False) 
print(result)
```



## Usage from console 

```bash [terminal/console $] 

evdschat 'I need sectoral inflation expectations data since 2020. quarterly and aggregated as end value' fileName.xlsx

```


![image](https://github.com/user-attachments/assets/b8e3534f-4d8b-4f72-ae4f-e10e76dc06dc)

## Installation

```bash
pip install evdschat -U

# or
python3.11 -m pip install evdschat -U

# or
python3.10 -m pip install evdschat -U
```

## Defining Api Keys ( .env file )

```bash
  # .env file content 

  OPENAI_API_KEY = "sk-proj-ABCDEFGIJKLMNOPQRSTUXVZ"
  EVDS_API_KEY=ABCDEFGIJKLMNOP

```

## Example

```python
from evdschat import chat 

prompt = '''
# Your prompt describing which data you want here.
'''

result, notes = chat(prompt, test=False) 
print(result)
```



## New in this version 



## License

This project is licensed under the Creative Commons Attribution-NonCommercial 4.0 International License. See the [LICENSE](LICENSE) file for details.



## evdschat Application (Node.js)

**evdschatJS** is a web API assistant for the evdspy Python package. It helps users by providing code suggestions to retrieve data from conversations.

[![tellme](https://github.com/user-attachments/assets/14024132-4d41-4879-9ea8-3e510b2f8f02)](https://evdspychat.onrender.com/)



## License

This project is licensed under the Creative Commons Attribution-NonCommercial 4.0 International License. See the [LICENSE](LICENSE) file for details.

