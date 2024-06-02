from utils import load_operation, list_operations, formation_data, formation_account, formation_card, name_transfer


def main():
    catalog = load_operation()
    operations = list_operations(catalog)
    for operation in operations:
        date = formation_data(operation["date"])
        name_to = name_transfer(operation["to"])
        number_to = formation_account(operation["to"])
        if "from" in operation:
            name_from = name_transfer(operation["from"])
            if name_from == "Счет":
                account_from = formation_account(operation["from"])
                print(f"{date} {operation["description"]}\n"
                      f"{name_from} {account_from} -> {name_to} {number_to}\n"
                      f"{operation["operationAmount"]["amount"]} {operation["operationAmount"]["currency"]["name"]}\n")
            else:
                numder_card = formation_card(operation["from"])
                print(f"{date} {operation["description"]}\n"
                      f"{name_from} {numder_card} -> {name_to} {number_to}\n"
                      f"{operation["operationAmount"]["amount"]} {operation["operationAmount"]["currency"]["name"]}\n")
        else:
            print(f"{date} {operation["description"]}\n"
                  f"{name_to} {number_to}\n"
                  f"{operation["operationAmount"]["amount"]} {operation["operationAmount"]["currency"]["name"]}\n")


main()
