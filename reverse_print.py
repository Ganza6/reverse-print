def reverse_print(my_list):  # Рекурсивно
    if my_list['next'] is not None:
        reverse_print(my_list['next'])
    print(my_list['value'])


def reverse_print_2(my_list):  # Нерекурсивно
    value_array = []
    while my_list is not None:
        value_array.append(my_list['value'])
        my_list = my_list['next']
    for value in reversed(value_array):
        print(value)


some_list = {
  'value': 1,
  'next': {
    'value': 2,
    'next': {
      'value': 3,
      'next': {
        'value': 4,
        'next': None,
      },
    },
  },
}

if __name__ == "__main__":
    reverse_print(some_list)
    #reverse_print_2(some_list)
