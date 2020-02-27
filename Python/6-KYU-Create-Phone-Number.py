def create_phone_number(n):
    #ATTEMPT ONE
    # return_str = ''.join([str(el) for el in n])
    # return '(' + return_str[:3] + ') ' + return_str[3:6] + '-' + return_str[6:]

    # REFACTORED
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))