import filters

menu = ("""
Меню фильтров:
""")
for fltr in filters:
    menu += str(fltr) + ') ' + filters[fltr].get('name') + '\n'
menu += '0) Выход'

while True:
    print(menu)
    f_choice = int(input('Выберите фильтр (или 0 для выхода):'))
    while f_choice not in [1, 2, 3, 4, 0]:
        print('извините, я вас не понял')
        f_choice = input('Выберите фильтр (или 0 для выхода):')

    if f_choice in [1, 2, 3, 4]:
        print(filters[f_choice].get('name') + ': ' + filters[f_choice].get('discription'))
    else:
        print('увидимся в следующий раз')
        break

    yes_no_question = input('хотите применить фильтр к тексту? (да/нет)\n')
    while yes_no_question.lower() not in ['да', 'нет']:
        print('извините, я вас не понял')
        yes_no_question = input('хотите применить фильтр к тексту? (да/нет)\n')

    if yes_no_question == 'да':
        text = input('введите текст:\n')
        print(filters[f_choice]['function'](text))










