import json
from dateutil import parser


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


def formation_data(date):
    """
    Форматирование даты
    """
    date = parser.parse(date).date()
    operation = date.strftime("%d.%m.%Y")
    return operation


def formation_card(transfer):
    """
    Скрытие номера карты
    """
    number_card = transfer.split(" ")[-1]
    number_card = number_card[:4] + " " + number_card[4:6] + "** **** " + number_card[-4:]
    return  number_card


def formation_account(transfer):
    """
    Скрытие номера счёта
    """
    number_account = transfer.split(" ")[-1]
    number_account = "**" + number_account[-4:]
    return number_account

