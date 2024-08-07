
evdschat Function (From Console / Terminal ) 
=============================================
The ``chat`` function returns the most specific data that was figured out by the current LLM we use and our current vector DB.   



Parameters
----------
prompt : str
    Question regarding the data.  
filename : str 
    Output file name to save result dataframes


Behavior and Errors
-------------------
.env file will be checked for OPENAI_API_KEY and EVDS_API_KEY

.. code-block:: bash
    
    # .env file content (example)
    OPENAI_API_KEY = "sk-proj-ABCDEFGHIJKLMNOprqstuVYZ"
    EVDS_API_KEY=ABCDEFGH


Example Usage
-------------
Here is how you might typically call this function:

.. code-block:: bash
    
   $[terminal]  evdschat 'Give me reserve data please. monthly and aggregate as average between 2010 and 2020 ' outputFileName 



Windows
----------

To set environment variables on Windows, you can use the `setx` command in the Command Prompt:

.. code-block:: bash
  
    setx EVDS_API_KEY "AxByCzDsFoGmHeIgJaKrLbMaNgOe"
    setx http_proxy "http://proxy.example.com:80"  
    setx https_proxy "http://proxy.example.com:80"



Linux and macOS
--------------------
To set environment variables on Linux or macOS, you can use the `export` command in the terminal:

.. code-block:: bash

    export EVDS_API_KEY="AxByCzDsFoGmHeIgJaKrLbMaNgOe"
    export http_proxy="http://proxy.example.com:80"
    export https_proxy="http://proxy.example.com:80"