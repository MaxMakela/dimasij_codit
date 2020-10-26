def correct_check(exp):
    sign_first = exp[0] == '+' or exp[0] == '-' or exp[0] == '*' or exp[0] == '/'
    sign_last = exp[-1] == '+' or exp[-1] == '-' or exp[-1] == '*' or exp[-1] == '/'
    for i in exp:
        if i.isalpha():
            return 'В выражении не могут быть буквы'

    if sign_first:
        return 'Выражение не может начинаться со знака'

    elif sign_last:
        return 'Выражение не может заканчиваться на знак'

    elif len(exp) < 3:
        return 'Выражение слишком короткое'

    elif '+' not in exp and '-' not in exp and '*' not in exp and '/' not in exp:
        return 'В выражении нет знаков'

    else:
        return exp


def splitter(exp):
    if '+' in correct_check(exp):
        spl = exp.split('+')
        return int(spl[0]) + int(spl[1])
    elif '-' in correct_check(exp):
        spl = exp.split('-')
        return int(spl[0]) - int(spl[1])
    elif '*' in correct_check(exp):
        spl = exp.split('*')
        return int(spl[0]) * int(spl[1])
    elif '/' in correct_check(exp):
        spl = exp.split('/')
        return int(spl[0]) / int(spl[1]) if int(spl[1]) != 0 else 'На ноль делить нельзя'


def retry(exp):
    while exp != correct_check(exp):
        print(correct_check(exp))
        exp = input('Введите выражение заново: ')
    return splitter(exp)


if __name__ == '__main__':
    exp = input('Введите выражение: ')
    print(retry(exp))
