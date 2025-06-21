from typing import Dict, List, Union


class Agregate:

    def return_data(self, data, arg_agregate) -> List[Dict[str, Union[int, float]]]:
        if (
                ">" in arg_agregate
                or "<" in arg_agregate
                or "=" in arg_agregate
        ):
            raise ValueError("wrong sign, need use =")
        if arg_agregate == "min":
            data = self.min_price(data)
        elif arg_agregate == "max":
            data = self.max_price(data)
        elif arg_agregate == "avg":
            data = self.avg_price(data)
        elif arg_agregate != None:
            raise ValueError("aggregate error")
        return data

    def min_price(self, data) -> List[Dict[str, int]]:
        min = int(data[0]["price"])
        for phone in data:
            if int(phone["price"]) < min:
                min = int(phone["price"])
        return [{"min": int(min)}]

    def max_price(self, data) -> List[Dict[str, int]]:
        max = int(data[0]["price"])
        for phone in data:
            if int(phone["price"]) > max:
                max = int(phone["price"])
        return [{"max": int(max)}]

    def avg_price(self, data) -> List[Dict[str, float]]:
        sum_price = 0
        count = len(data)
        for phone in data:
            sum_price += int(phone["price"])
        avg = sum_price / count
        return [{"avg": avg}]
