from typing import List, Dict

from tabulate import tabulate

from app.data import Data


class Writer:
    def __init__(self, arg):
        self.files: List[str] = arg

    def write(self, where, agregate) -> None:
        data_obj = Data()
        data = data_obj.return_data(self.files, where, agregate)
        print(tabulate(data, headers="keys", tablefmt="pipe"))
