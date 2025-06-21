from typing import List, Dict


class Filter:

    def return_data(self, data, value, symbol) -> List[Dict[str, str]]:
        if ">" in str(value) or "<" in str(value) or "=" in str(value):
            raise ValueError("wrong sign, need use > or < or =")
        value = int(value)
        if symbol == ">":
            data = self.more(data, value)
        elif symbol == "<":
            data = self.less(data, value)
        elif symbol == "=":
            data = self.equals(data, value)
        if data == []:
            raise ValueError("not found value")
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
