Examples 
====================

Some examples to retrieve data 


Basic usage:

.. code-block:: python

    from evdschat import chat 
    prompt = '''

    Can I get reserves data please ? Monthly frequency would be great if you can aggreagate by average.
    between 2010 and 2020 by the way. Thanks.
    
    
    '''

    res = chat(prompt, debug=False  )
    print(res)
    print(res.data)
    print(res.data)
    res.to_excel('OutputFileName.xlsx')

