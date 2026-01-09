def is_armstrong_number(number):
    if number >= 0 and number <= 9:
        return True
    elif number == 10:
        return False
    else:
        temp_num = number
        number_length = 0
        while temp_num / 10 != 0:
            temp_num //= 10
            number_length += 1
        temp_num = number
        sum = 0
        while temp_num / 10 != 0:
            one_num = temp_num % 10
            sum += one_num ** number_length
            temp_num //= 10
        return number == sum