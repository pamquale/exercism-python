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
    known_operations = ['plus', 'minus', 'multiplied', 'divided']
    for i in range(1, len(question), 2):
        if question[i] in known_operations:
            if question[i] == 'plus':
                try:
                    result += int(question[i + 1])
                except:
                    raise ValueError("syntax error")
            elif question[i] == 'minus':
                try:
                    result -= int(question[i + 1])
                except:
                    raise ValueError("syntax error")
            elif question[i] == 'multiplied':
                try:
                    result *= int(question[i + 1])
                except:
                    raise ValueError("syntax error")
            elif question[i] == 'divided':
                try:
                    result /= int(question[i + 1])
                except:
                    raise ValueError("syntax error")
        else:
            try:
                test = int(question[i])
            except:
                raise ValueError("unknown operation")
            raise ValueError("syntax error")
    return result

print(answer("What is 5 plus 5?"))