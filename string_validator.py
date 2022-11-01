import re

def isStringValid(string):
    string_start_caps = startswith_upper(string)
    even_quotes = quotation_count_even(string)
    period_ending = endswith_period(string)
    number_convert = number_to_string_below_limit(string)
    if string_start_caps and even_quotes and period_ending and number_convert:
        return True
    else:
        return False

def startswith_upper(string):
    startswith_upper_check = string[0]
    if startswith_upper_check.isupper():
        return True
    else:
        return False

def quotation_count_even(string):
    quotation_count = string.count('"')
    if (quotation_count % 2) == 0:
        return True
    else:
        return False

def endswith_period(string):
    if string.endswith((".", "!", "?")):
        count = 0
        for _ in re.finditer('[.!?]', string):
            count += 1
        if count > 1:
            return False
        else:
            return True
    else:
        return False

def number_to_string_below_limit(string):
    number_in_string = re.findall(r'\d+', string)
    if number_in_string:
        d = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
             6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
             11: 'eleven', 12: 'twelve', 13: 'thirteen'}
        for i in number_in_string:
            i = int(i)
            if i < 13:
                int_string = d[i]
                is_string_in_test_string = string.find(int_string)
                if is_string_in_test_string > 0:
                    continue
                else:
                    return False
            else:
                return True
    else:
        return True

string = input("Enter a string and it will be validated: ")
result = isStringValid(string)
if result == True:
    print(string + " is valid")
else:
    print(string + " is invalid")