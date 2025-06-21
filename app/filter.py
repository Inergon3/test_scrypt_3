from typing import List, Dict


class Filter:

    def return_data(self, data, value, symbol) -> List[Dict[str, str]]:
        if symbol == ">":
            data = self.more(data, value)
        elif symbol == "<":
            data = self.less(data, value)
        elif symbol == "=":
            data = self.equals(data, value)
        return data

    def more(self, data, value) -> List[Dict[str, str]]:
        new_data: List[Dict[str, str]] = []
        for phone in data:
            if int(phone["price"]) > value:
                new_data.append(phone)
        return new_data

    def less(self, data, value) -> List[Dict[str, str]]:
        new_data: List[Dict[str, str]] = []
        for phone in data:
            if int(phone["price"]) < value:
                new_data.append(phone)
        return new_data

    def equals(self, data, value) -> List[Dict[str, str]]:
        new_data: List[Dict[str, str]] = []
        for phone in data:
            if int(phone["price"]) == value:
                new_data.append(phone)
        return new_data
