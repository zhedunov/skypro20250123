from src.masks import *

card_number = "7000792289606361"
# ~ card_number = "70007922896063"
card_number_mask = get_mask_card_number(card_number)
print(card_number_mask)  # 7000 79** **** 6361

account_number = "73654108430135874305"
# ~ account_number = "7365410843013587430"
account_number_mask = get_mask_account(account_number)
print(account_number_mask)  # **4305