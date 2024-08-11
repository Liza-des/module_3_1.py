calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())


def is_contains(string, list_to_search):
    count_calls()
    return string.upper() in [item.upper() for item in list_to_search]


info = string_info('Capybara')
print(info)
info = string_info('Armageddon')
print(info)

contains = is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])
print(contains)
contains = is_contains('cycle', ['recycling', 'cyclic'])
print(contains)

print(calls)
