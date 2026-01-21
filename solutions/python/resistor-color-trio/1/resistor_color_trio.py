def label(colors):
    color_map = {
        'black': '0',
        'brown': '1',
        'red': '2',
        'orange': '3',
        'yellow': '4',
        'green': '5',
        'blue': '6',
        'violet': '7',
        'grey': '8',
        'white': '9'
    }
    result = int(color_map[colors[0]] + color_map[colors[1]]) * 10 ** int(color_map[colors[2]])
    if result < 1000:
        return f'{result} ohms'
    elif result < 1000 * 1000:
        return f'{result // 1000} kiloohms'
    elif result < 1000 * 1000 * 1000:
        return f'{result // (1000 * 1000)} megaohms'
    elif result < 1000 * 1000 * 1000 * 1000:
        return f'{result // (1000 * 1000 * 1000)} gigaohms'
    return None