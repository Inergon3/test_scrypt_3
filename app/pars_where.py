def pars_where(arg_where):
    if arg_where is not None:
        symbols = ["<", ">", "="]
        for symbol in symbols:
            if symbol in arg_where:
                field, value = arg_where.split(symbol)
                return {"field": field, "symbol": symbol, "value": value}
        raise ValueError("error")
    return {"field": None, "symbol": None, "value": 0}


def pars_agregate(arg_aggregate):
    if arg_aggregate is not None:
        if "=" in arg_aggregate:
            field, value = arg_aggregate.split("=")
            return {"field": field, "value": value}
        raise ValueError("error")
    return {"field": None, "value": "None"}
