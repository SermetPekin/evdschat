Introduction
===============================

.. image:: https://github.com/SermetPekin/evdschat/actions/workflows/python-package.yml/badge.svg
    :target: https://github.com/SermetPekin/evdschat/actions/workflows/python-package.yml
.. image:: https://img.shields.io/pypi/v/evdschat
    :target: https://pypi.org/project/evdschat/
.. image:: https://img.shields.io/pypi/pyversions/evdschat
    :target: https://pypi.org/project/evdschat/
.. image:: https://pepy.tech/badge/evdschat/week
    :target: https://pepy.tech/project/evdschat

**evdschat** is an open-source Python interface designed to simplify requests to the **Central Bank of the Republic of Turkey (CBRT) Electronic Data Delivery System (EVDS)**. 
It tries to decide which data user wants from the conversation and returns data as Result instance (data:pd.DataFrame, metadata:pd.DataFrame and to_excel: Callable function )  

View Source Code
----------------
You can view the source code for this project on GitHub: `View Source <https://github.com/SermetPekin/evdschat>`_.

What's New
----------

Updated in this version:
------------------------------
- chat function 

`evdspyChat <https://evdspychat.onrender.com/>`_

.. image:: https://github.com/user-attachments/assets/14024132-4d41-4879-9ea8-3e510b2f8f02
    :target: https://evdspychat.onrender.com/

.. image:: https://github.com/user-attachments/assets/2cece3e0-958a-454b-8876-5dbdfea1e1a4
    :target: https://evdspychat.onrender.com/

.. image:: https://github.com/user-attachments/assets/3e5d3ab4-df41-4d34-8e2a-e1ca3d19a190
    :target: https://evdspychat.onrender.com/

Key Features
------------
- retrievs data from conversation 

Installation
------------
To install **evdschat**, simply run the following command:

.. code-block:: bash

    pip install evdschat -U

Quick Start
-----------

Here's a quick example to get you started with using **evdschat**:

Using the ``chat`` function from evdschat:

.. code-block:: python

    prompt = '''

    Can I get reserves data please ? Monthly frequency would be great if you can aggreagate by average.
    between 2010 and 2020 by the way. Thanks.
    
    
    '''

    res = chat(prompt, debug=False  )
    print(res)
    print(res.data)
    print(res.data)
    res.to_excel('OutputFileName.xlsx')

