# evdschat - An open-source Python package for enhanced data retrieval.
# Copyright (c) 2024 Sermet Pekin
# Licensed under the MIT License. See LICENSE file in the project root for full license information.


from evdschat import chat

prompt = """

 Can I get reserves data please ? frequence must be monthly and you may aggregate by averages. 
 
 
"""

res , notes  = chat(prompt, debug=False   )
print(res)
# res.to_excel('prompt1.xlsx')
