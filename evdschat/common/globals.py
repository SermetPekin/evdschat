def global_mock():
    template = """ 
TP_GSYIH01_GY_CF #
TP_GSYIH02_GY_CF #
TP_GSYIH03_GY_CF
TP_GSYIH04_GY_CF 
TP_GSYIH05_GY_CF
TP_GSYIH06_GY_CF
TP_GSYIH07_GY_CF
TP_GSYIH08_GY_CF

        """
    return {
        "index": template,
        "start_date": "31-12-2009",
        "frequency": "monthly",
        "aggregation": "end",
        "notes": "Note: This is a mock result for testing purposes... in order to get real results call the same function with test=False ",
    }
