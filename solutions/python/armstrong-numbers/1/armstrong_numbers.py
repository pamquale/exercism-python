def is_armstrong_number(number):
    if number >= 0 and number <= 9:
        return True
    elif number == 10:
        return False
    else:
        number_array = []
        temp_num = number
        while temp_num / 10 != 0:
            one_num = temp_num % 10
            number_array.append(one_num)
            temp_num //= 10
        number_array = list(reversed(number_array))
        length = len(number_array)
        sum = 0
        for num in number_array:
            sum += num ** length
        if number == sum:
            return True
        else:
            return False
    