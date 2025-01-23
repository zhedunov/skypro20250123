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


card_number = "7000792289606361"
# ~ card_number = "70007922896063"
card_number_mask = get_mask_card_number(card_number)
print(card_number_mask)  # 7000 79** **** 6361

account_number = "73654108430135874305"
# ~ account_number = "7365410843013587430"
account_number_mask = get_mask_account(account_number)
print(account_number_mask)  # **4305
