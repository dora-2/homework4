def filter_by_state(dictionary: list, state = ['EXECUTED'], d = []) -> list:
    for i in dictionary:
        if i['state'] == state:
            d += i
    return i

print(filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]))