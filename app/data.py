from typing import Dict, Union, List

from app.agregate import Agregate
from app.filter import Filter
from app.pars_where import pars_where, pars_agregate
from app.reader import Reader


class Data:

    def return_data(
        self, files, where, agregate
    ) -> Union[List[Dict[str, Union[int, float]]], Union[int, float]]:
        reader = Reader()
        data = reader.return_dict(files)
        if where is not None:
            arg_where = pars_where(where)
            if (
                ">" in arg_where["value"]
                or "<" in arg_where["value"]
                or "=" in arg_where["value"]
            ):
                raise ValueError("wrong sign, need use > or < or =")
            filter = Filter()
            data = filter.return_data(
                data, int(arg_where["value"]), arg_where["symbol"]
            )
        if agregate is not None:
            arg_agregate = pars_agregate(agregate)
            if (
                ">" in arg_agregate["value"]
                or "<" in arg_agregate["value"]
                or "=" in arg_agregate["value"]
            ):
                raise ValueError("wrong sign, need use =")
            agregate_obj = Agregate()
            data = agregate_obj.return_data(data, arg_agregate)
        return data
