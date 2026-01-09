def square_root(number):
    sqr_root = 1
    low_border = 0
    top_border = number
    while low_border != top_border:
        if sqr_root * sqr_root < number:
            low_border = sqr_root
            sqr_root = round(sqr_root * 1.5)
        elif sqr_root * sqr_root > number:
            top_border = sqr_root
            if sqr_root // 2 <= low_border:
                sqr_root = sqr_root - ((top_border - low_border) // 2)
            else:
                sqr_root //= 2
        else:
            return sqr_root
    return "The number is not a perfect square"