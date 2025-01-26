import src.masks

def mask_account_card(card_number: str) -> str:
    """Функция маскирует номер карты"""
    lst = card_number.split()
    # print(get_mask_card_number(lst[-1]))
    if card_number.startswith("Счет"):
        return "Счет " + src.masks.get_mask_account(lst[-1])
    else:
        if len(lst) > 2:
            type_card_name = lst[0] + " " + lst[1] + " "
        else:
            type_card_name = lst[0] + " "
        return "" + type_card_name + src.masks.get_mask_card_number(lst[-1])


def get_date(date_string: str) -> str:
    """Функция меняет формат даты на российский"""
    lst = date_string.split("-")

    month = lst[1]
    day = lst[2][:2]
    year = int(lst[0])
    res_date = "{0}.{1}.{2:02}".format(day, month, year % 100)
    return "" + res_date
