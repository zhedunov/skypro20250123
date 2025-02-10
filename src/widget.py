import src.masks


def mask_account_card(card_number: str) -> str:
    '''Функция маскирует номер счета или карты'''
    digit_quadres = card_number.split()
    # print(get_mask_card_number(lst[-1]))
    if card_number.startswith("Счет"):
        return "Счет " + src.masks.get_mask_account(digit_quadres[-1])
    else:
        if len(digit_quadres) > 2:
            type_card_name = digit_quadres[0] + " " + digit_quadres[1] + " "
        else:
            type_card_name = digit_quadres[0] + " "
        return "" + type_card_name + src.masks.get_mask_card_number(digit_quadres[-1])


def get_date(date_string: str) -> str:
    """Функция меняет формат даты на российский"""
    date_elements = date_string.split("-")

    month = date_elements[1]
    day = date_elements[2][:2]
    year = int(date_elements[0])
    res_date = "{0}.{1}.{2:02}".format(day, month, year % 100)
    return "" + res_date
