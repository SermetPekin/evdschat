
chat Function
====================
The ``chat`` function returns the most specific data that was figured out by the current LLM we use and our current vector DB.   




Parameters
----------
prompt : str
    Question regarding the data.  

Behavior and Errors
-------------------
.env file will be checked for OPENAI_API_KEY and EVDS_API_KEY


.. code-block:: bash 

    # .env file content (example)
    OPENAI_API_KEY = "sk-proj-ABCDEFGHIJKLMNOprqstuVYZ"
    EVDS_API_KEY=ABCDEFGH



.. code-block:: bash 

    # .env file content (example)
    OPENAI_API_KEY = "sk-proj-ABCDEFGHIJKLMNOprqstuVYZ"
    EVDS_API_KEY=ABCDEFGH
    

Example Usage
-------------
Here is how you might typically call this function:

.. code-block:: python

    from evdschat import chat 
    prompt = '''

    Can I get reserves data please ? Monthly frequency would be great if you can aggreagate by average.
    between 2010 and 2020 by the way.  
    
    
    '''

    res = chat(prompt, debug=False  )
    print(res)
    res.to_excel('File_reserves.xlsx')