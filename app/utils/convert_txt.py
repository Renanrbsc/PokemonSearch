import copy

from typing import List, Dict


def open_txt(url: str):
    archive = open(url, 'r', encoding="utf8")
    txt = archive.read()
    archive.close()
    return txt

def convert_txt_for_json(data: str, model_dict) -> List[dict]:
    list_of_processed_data: List[dict] = list()
    data_list: List[str] = data.strip().split("\n")
    for index_row, field_str in enumerate(data_list):
        processed_row: List[str, str] = field_str.split(';')
        processed_row.insert(0, str(index_row + 1))

        for index_field, key in enumerate(model_dict):
            model_dict[key] = processed_row[index_field]

        dict_save: Dict[str: str] = copy.deepcopy(model_dict)
        list_of_processed_data.append(dict_save)

    return list_of_processed_data


