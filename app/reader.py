from typing import List, Dict


class Reader:

    def read(self, files) -> List[List[List[str]]]:
        read_files: List[List[List[str]]] = []
        for file in files:
            try:
                with open(file, "r") as f:
                    lines: List[str] = f.readlines()
                    read_file: List[str] = []
                    for line in lines:
                        read_file.append(line.replace("\n", "").split(","))
                    read_files.append(read_file)
            except:
                raise ValueError(f"file {file} not found")
        return read_files

    def return_dict(self, files) -> List[Dict[str, str]]:
        read_file: List[List[List[str]]] = self.read(files)
        file_list_dict: List[Dict[str, str]] = []
        for file in read_file:
            header = file[0]
            file.pop(0)
            for val in file:
                count: int = 0
                cache: dict = {}
                while count <= len(val) - 1:
                    cache[header[count].lstrip().rstrip()] = (
                        val[count].lstrip().rstrip()
                    )
                    count += 1
                file_list_dict.append(cache)
        return file_list_dict
