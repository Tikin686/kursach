import json


def load_operation():
    """
    Создание списка операций
    """
    with open("operations.json", "r", encoding="UTF-8") as file:
        return json.load(file)
