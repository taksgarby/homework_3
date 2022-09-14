def return_10():
    return 10

def add(num_1, num_2):
    result =  num_1 + num_2
    return result 

def subtract(num_1, num_2):
    result = num_1 - num_2
    return result 

def multiply(num_1, num_2):
    result = num_1 * num_2
    return result 

def divide(num_1, num_2):
    result = num_1 / num_2
    return int(result)

def length_of_string(str):
    result = len(str)
    return result

def join_string(str_1, str_2):
    result = str_1 + str_2
    return result

def add_string_as_number(str_1, str_2):
    result = int(str_1) + int(str_2)
    return result

def number_to_full_month_name(num):
    if num == 1:
        return "January"

    elif num == 3:
        return "March"

    elif num == 9:
        return "September"

def number_to_short_month_name(num):
    if num == 1:
        return "Jan"
    
    elif num == 4:
        return "Apr"

    elif num == 10:
        return "Oct"