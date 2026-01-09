def is_paired(input_string):
    opened_bracket = ['(', '[', '{']
    closed_bracket = [')', ']', '}']
    current_brackets = []
    to_find = ''
    is_all_good = True
    for index, char in enumerate(input_string):
        if char in opened_bracket:
            current_brackets.append(char)
            to_find = bracket_to_find(current_brackets)
            is_all_good = False
        elif char in closed_bracket:
            if char == to_find:
                current_brackets.pop()
                to_find = ''
                is_all_good = True
                if current_brackets:
                    to_find = bracket_to_find(current_brackets)
                else:
                    continue
            else:
                return False
    return is_all_good

def bracket_to_find(current_brackets):
    if current_brackets[-1] == '(':
        return ')'
    elif current_brackets[-1] == '[':
        return ']'
    elif current_brackets[-1] == '{':
        return '}'