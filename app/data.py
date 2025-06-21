from typing import Dict, Union, List

from app.aggregate import Aggregate
from app.filter import Filter
from app.pars_arg import pars_where, pars_aggregate
from app.reader import Reader


class Data:

    def return_data(
        self, files, where=None, aggregate=None
    ) -> Union[List[Dict[str, Union[int, float]]], Union[int, float]]:
        reader = Reader()
        data = reader.return_dict(files)
        if where is not None:
            arg_where = pars_where(where)
            filter = Filter()
            data = filter.return_data(data, arg_where["value"], arg_where["symbol"])
        if aggregate is not None:
            arg_aggregate = pars_aggregate(aggregate)
            aggregate_obj = Aggregate()
            data = aggregate_obj.return_data(data, arg_aggregate["value"])
        return data
