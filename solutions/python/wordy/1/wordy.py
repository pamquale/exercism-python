def answer(question):
    if not question.startswith('What is '):
        raise ValueError("syntax error")
    else:
        question = question.replace('What is ', '').replace('by','').replace('?','')
    question = question.split()
    try:
        result = int(question[0])
    except:
        raise ValueError("syntax error")
    for i, element in enumerate(question):
        if i % 2 == 0:
            try:
                int(element)
            except:
                raise ValueError("syntax error")
        else:
            if element == 'plus':
                try:
                    result += int(question[i + 1])
                except:
                    raise ValueError("syntax error")
            elif element == 'minus':
                try:
                    result -= int(question[i + 1])
                except:
                    raise ValueError("syntax error")
            elif element == 'multiplied':
                try:
                    result *= int(question[i + 1])
                except:
                    raise ValueError("syntax error")
            elif element == 'divided':
                try:
                    result /= int(question[i + 1])
                except:
                    raise ValueError("syntax error")
            else:
                try:
                    test = int(element)
                except:
                    raise ValueError("unknown operation")
                raise ValueError("syntax error")
    return result