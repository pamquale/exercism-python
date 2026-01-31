def encode(numbers):
    order = []
    for number in numbers:
        if number == 0:
            order.append(number)
        is_last = True
        mini_order = []
        while number != 0:
            part = number & 0x7F
            number = number >> 7
            if not is_last:
                part |= 0x80
            mini_order.append(part)
            is_last = False
        mini_order.reverse()
        order.extend(mini_order)
    return order

def decode(bytes_):
    if len(bytes_) == 1 and bytes_[0] & 0x80 == 128:
        raise ValueError("incomplete sequence")
    number = 0
    numbers = []
    new_number = True
    for i in range(0, len(bytes_)):
        if new_number:
            number = bytes_[i] & 0x7F
            new_number = False
            if bytes_[i] & 0x80 == 128:
                continue
            else:
                numbers.append(number)
                continue
        if bytes_[i] & 0x80 == 128:
            number *= 128
            number += bytes_[i] & 0x7F
            new_number = False
        else:
            number *= 128
            number += bytes_[i] & 0x7F
            numbers.append(number)
            new_number = True
    return numbers