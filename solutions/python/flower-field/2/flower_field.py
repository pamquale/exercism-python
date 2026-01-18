def annotate(garden):
    if not garden:
        return garden
    length_row = len(garden[0])
    length_garden = len(garden)
    allowed_symbols = ['*', ' ']
    for i, row in enumerate(garden):
        if len(row) != length_row:
            raise ValueError("The board is invalid with current input.")
        if not set(row).issubset(allowed_symbols):
            raise ValueError("The board is invalid with current input.")
        garden[i] = list(garden[i])
    for i, row in enumerate(garden):
        for j, col in enumerate(row):
            potential_neighbours = (
                (i - 1, j - 1), (i - 1, j), (i - 1, j + 1),
                (i, j - 1),                 (i, j + 1),
                (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)
            )
            mines = 0
            for rows, cols in potential_neighbours:
                if 0 <= rows < length_garden and 0 <= cols < length_row:
                    if garden[rows][cols] == '*':
                        mines += 1
            if mines > 0 and garden[i][j] != '*': garden[i][j] = str(mines)
    for i in range(length_garden):
        garden[i] = ''.join(garden[i])
    return garden