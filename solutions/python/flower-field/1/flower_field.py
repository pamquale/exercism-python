def annotate(garden):
    length_garden = len(garden)
    try:
        length_row = len(garden[0])
    except:
        return garden
    allowed_symbols = '* '
    for i, row in enumerate(garden):
        if len(row) != length_row:
            raise ValueError("The board is invalid with current input.")
        if not set(row).issubset(allowed_symbols):
            raise ValueError("The board is invalid with current input.")
        garden[i] = list(garden[i])
    for i, row in enumerate(garden):
        for j, square in enumerate(row):
            if square == '*':
                continue
            mines = 0
            if i > 0 and j > 0 and garden[i - 1][j - 1] == '*':
                mines += 1
            if j > 0 and garden[i][j - 1] == '*':
                mines += 1
            if i != length_garden - 1 and j > 0 and garden[i + 1][j - 1] == '*':
                mines += 1
            if i > 0 and garden[i - 1][j] == '*':
                mines += 1
            if i != length_garden - 1 and garden[i + 1][j] == '*':
                mines += 1
            if i > 0 and j != length_row - 1 and garden[i - 1][j + 1] == '*':
                mines += 1
            if j != length_row - 1 and garden[i][j + 1] == '*':
                mines += 1
            if i != length_garden - 1 and j != length_row - 1 and garden[i + 1][j + 1] == '*':
                mines += 1
            if mines > 0: garden[i][j] = str(mines)
    for i in range(length_garden):
        garden[i] = ''.join(garden[i])
    return garden