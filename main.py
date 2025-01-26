import src.masks
import src.widget

card_number = "Maestro 1596837868705199"
card_number = "Счет 64686473678894779589"
card_number = "MasterCard 7158300734726758"
card_number = "Счет 35383033474447895560"
card_number = "Visa Classic 6831982476737658"
card_number = "Visa Platinum 8990922113665229"
card_number = "Visa Gold 5999414228426353"
card_number = "Счет 73654108430135874305"

# s = mask_account_card(card_number)
# print(s)  # **4305

date_given = "2024-03-11T02:26:18.671407"
s = src.widget.get_date(date_given)
print(s)  # **4305
