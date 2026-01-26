def recite(start, take=1):
    numbers = ['no', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten']
    text = []
    for i in range(take):
        current_bottle = 'bottles' if start > 1 else 'bottle'
        next_bottle = 'bottles' if start != 2 else 'bottle'
        text.append(f"{numbers[start]} green {current_bottle} hanging on the wall,")
        text.append(f"{numbers[start]} green {current_bottle} hanging on the wall,")
        text.append(f"And if one green bottle should accidentally fall,")
        text.append(f"There'll be {numbers[start-1].lower()} green {next_bottle} hanging on the wall.")
        if i != take - 1:
            text.append('')
        start -= 1
    return text