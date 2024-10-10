def filter_by_state(dictionary: list, state = ['EXECUTED'], new_dictionary = []) -> list:
    for i in dictionary:
      if i['state'] in state:
        new_dictionary.append(i)
    return new_dictionary

