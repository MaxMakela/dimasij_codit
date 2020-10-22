def correct_check(exp):
    for i in exp:
        if i.isalpha():
            return(print('В выражении не могут быть буквы'))

    if exp[0] == '+' or exp[0] == '-' or exp[0] == '*' or exp[0] == '/':
        return(print('Выражение не может начинаться со знака'))

    elif exp[-1] == '+' or exp[-1] == '-' or exp[-1] == '*' or exp[-1] == '/':
        return(print('Выражение не может заканчиваться на знак'))

    elif len(exp) < 3:
        return(print('Выражение слишком короткое'))

    elif '+' not in exp and '-' not in exp and '*' not in exp and '/' not in exp:
        return(print('В выражении нет знаков'))
        
    else:
        return exp


def splitter(exp):
    if '+' in correct_check(exp):
        spl = exp.split('+')
        spl = [int(i) for i in spl if i != '+']
        spl.append('+')
        return spl

    elif '-' in correct_check(exp):
        spl = exp.split('-')
        spl = [int(i) for i in spl if i != '-']
        spl.append('-')
        return spl

    elif '*' in correct_check(exp):
        spl = exp.split('*')
        spl = [int(i) for i in spl if i != '*']
        spl.append('*')
        return spl

    elif '/' in correct_check(exp):
        spl = exp.split('/')
        spl = [int(i) for i in spl if i != '/']
        spl.append('/')
        return spl
      

    return spl


def plus(exp):
    if splitter(exp)[2] == '+':
        return splitter(exp)[0] + splitter(exp)[1]


def minus(exp):
    if splitter(exp)[2] == '-':
        return splitter(exp)[0] - splitter(exp)[1]


def times(exp):
    if splitter(exp)[2] == '*':
        return splitter(exp)[0] * splitter(exp)[1]


def divide(exp):
    if splitter(exp)[1] == 0:
        return print('На ноль делить нельзя')
    elif splitter(exp)[2] == '/':
        return splitter(exp)[0] / splitter(exp)[1]        





#вызов главной функии 
exp = input('Введите выражение: ')
print(divide(exp))
