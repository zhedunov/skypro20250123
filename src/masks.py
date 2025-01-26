def get_mask_card_number(card_number: str) -> str:
    """Функция маскирует номер карты"""
    if len(card_number) >= 16:
        masked_card_number = ""
        part1 = card_number[0:4]
        part2 = card_number[4:8]
        part4 = card_number[12:16]
        masked_card_number = part1 + " " + part2[:2] + "**  ****" + " " + part4
        return masked_card_number  # 7000 79** **** 6361
    else:
        return "card number too short!"


def get_mask_account(account_number: str) -> str:
    """Функция маскирует номер счета"""
    if len(account_number) >= 20:
        masked_account_number = ""
        masked_account_number = "**" + account_number[-4:]
        return masked_account_number
    else:
        return "account number too short!"
