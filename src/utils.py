import json


def load_operation():
    """
    Создание списка операций
    """
    with open("operations.json", "r", encoding="UTF-8") as file:
        return json.load(file)


def list_operations(operations):
    """
    Список операций
    """
    transfer_executed = [operation for operation in operations if operation.get("state") == "EXECUTED"]
    transfer_executed.sort(key=lambda x: str(x.get("date")), reverse=True)
    return transfer_executed[:5]
