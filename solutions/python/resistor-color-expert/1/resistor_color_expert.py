def resistor_label(colors):
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
    tolerance_map = {
        'grey': '0.05%',
        'violet': '0.1%',
        'blue': '0.25%',
        'green': '0.5%',
        'brown': '1%',
        'red': '2%',
        'gold': '5%',
        'silver': '10%'
    }
    result = 0
    if len(colors) == 1:
        return f'{color_map[colors[0]]} ohms'
    elif len(colors) == 4:
        result = int(color_map[colors[0]] + color_map[colors[1]]) * 10 ** int(color_map[colors[2]])
    elif len(colors) == 5:
        result = int(color_map[colors[0]] + color_map[colors[1]] + color_map[colors[2]]) * 10 ** int(color_map[colors[3]])
    if result < 1000:
        return f'{result} ohms ±{tolerance_map[colors[-1]]}'
    elif result < 1_000_000:
        return f'{result / 1000:g} kiloohms ±{tolerance_map[colors[-1]]}'
    elif result < 1_000_000_000:
        return f'{result / 1_000_000:g} megaohms ±{tolerance_map[colors[-1]]}'
    elif result < 1_000_000_000_000:
        return f'{result / 1_000_000_000:g} gigaohms ±{tolerance_map[colors[-1]]}'
    return None