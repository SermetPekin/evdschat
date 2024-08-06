Proxy Configuration
==========================

You can configure proxies for your application by defining them in a `.env` file. The script will load your proxies from this file if it is available.

[Option 1 ] Creating a `.env` File
=======================================

Create a `.env` file in the root directory of your project and define your proxies as shown below:


.. code-block:: bash 

    # Example .env file content
    # .env file content (example)
    OPENAI_API_KEY = "sk-proj-ABCDEFGHIJKLMNOprqstuVYZ"
    EVDS_API_KEY=ABCDEFGH
    
    

[Option 2 ] Setting Environment Variables
==========================================

Windows
--------------------
To set environment variables on Windows, you can use the `setx` command in the Command Prompt:

.. code-block:: bash

    setx OPENAI_API_KEY "sk-proj-ABCDEFGHIJKLMNOprqstuVYZ"
    setx EVDS_API_KEY "AxByCzDsFoGmHeIgJaKrLbMaNgOe"



Linux and macOS
--------------------
To set environment variables on Linux or macOS, you can use the `export` command in the terminal:

.. code-block:: bash

    export OPENAI_API_KEY="sk-proj-ABCDEFGHIJKLMNOprqstuVYZ"
    export EVDS_API_KEY="AxByCzDsFoGmHeIgJaKrLbMaNgOe"


You can add these lines to your shell configuration file (e.g., `.bashrc`, `.bash_profile`, `.zshrc`) to make them persistent.

Notes
--------------------

