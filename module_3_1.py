def count_calls():
    global calls
    calls += 1
    
def string_info(string):
    text = (len(string), string.upper(), string.lower())
    count_calls()
    return text

def is_contains(string, list_to_search):
    contain = False
    for word in list_to_search:
        if word.lower() in string.lower():
            contain = True
    count_calls()
    return contain
    

calls = 0
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
