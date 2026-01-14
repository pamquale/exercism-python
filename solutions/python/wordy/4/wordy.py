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
            try:
                number = int(question[i+1])
            except:
                raise ValueError("syntax error")
            if question[i] == 'plus':
                    result += number
            elif question[i] == 'minus':
                    result -= number
            elif question[i] == 'multiplied':
                    result *= number
            elif question[i] == 'divided':
                    result /= number
        else:
            try:
                number = int(question[i])
            except:
                raise ValueError("unknown operation")
            raise ValueError("syntax error")
    return result