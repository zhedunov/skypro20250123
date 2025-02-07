import src.masks
import src.widget
import src.processing

'''
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
'''


test_data = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
res = src.processing.filter_by_state(test_data, 'CANCELED')
print(res)
'''
test_data2 = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
res = src.processing.sort_by_date(test_data2, False)
print(test_data2)
'''