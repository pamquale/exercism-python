def commands(binary_str):
    actions = ['wink', 'double blink', 'close your eyes', 'jump']
    handshake = []
    for i, bit in enumerate(reversed(binary_str)):
        if i == 4 and bit == '1':
            handshake.reverse()
            continue
        if bit == '1':
            handshake.append(actions[i])
    return handshake