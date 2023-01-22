from random import randint


def attack(char_name, char_class):
    damage_text = 'нанёс урон противнику равный'
    if char_class == 'warrior':
        return (f'{char_name} {damage_text} {5 + randint(3, 5)}')
    if char_class == 'mage':
        return (f'{char_name} {damage_text} {5 + randint(5, 10)}')
    if char_class == 'healer':
        return (f'{char_name} {damage_text} {5 + randint(-3, -1)}')


def defence(char_name, char_class):
    if char_class == 'warrior':
        return (f'{char_name} блокировал {10 + randint(5, 10)} урона')
    if char_class == 'mage':
        return (f'{char_name} блокировал {10 + randint(-2, 2)} урона')
    if char_class == 'healer':
        return (f'{char_name} блокировал {10 + randint(2, 5)} урона')


def special(char_name, char_class):
    castspell = 'применил специальное умение'
    if char_class == 'warrior':
        return (f'{char_name} {castspell} «Выносливость {80 + 25}»')
    if char_class == 'mage':
        return (f'{char_name} {castspell} «Атака {5 + 40}»')
    if char_class == 'healer':
        return (f'{char_name} {castspell} «Защита {10 + 30}»')


def start_training(char_name, char_class):
    if char_class == 'warrior':
        print(f'{char_name}, ты Воитель — отличный боец ближнего боя.')
    if char_class == 'mage':
        print(f'{char_name}, ты Маг — превосходный укротитель стихий.')
    if char_class == 'healer':
        print(f'{char_name}, ты Лекарь — чародей, способный исцелять раны.')
    print('Потренируйся управлять своими навыками.')
    i_attack = 'attack — чтобы атаковать противника'
    i_defence = 'defence — чтобы блокировать атаку противника'
    i_special = 'special — чтобы использовать свою суперсилу'
    print(f'Введи одну из команд: {i_attack}, {i_defence} или {i_special}.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd = None
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd == 'attack':
            print(attack(char_name, char_class))
        if cmd == 'defence':
            print(defence(char_name, char_class))
        if cmd == 'special':
            print(special(char_name, char_class))
    return 'Тренировка окончена.'


def choice_char_class():
    approve_choice = None
    char_class = None
    while approve_choice != 'y':
        pers_info = 'Введи название персонажа, за которого хочешь играть:'
        war = 'Воитель — warrior'
        mag = 'Маг — mage'
        heal = 'Лекарь — healer'
        char_class = input(f'{pers_info} {war}, {mag}, {heal}: ')
        if char_class == 'warrior':
            warrior_info = 'Воитель — дерзкий воин ближнего боя.'
            print(f'{warrior_info} Сильный, выносливый и отважный.')
        if char_class == 'mage':
            mage_info = 'Маг — находчивый воин дальнего боя.'
            print(f'{mage_info} Обладает высоким интеллектом.')
        if char_class == 'healer':
            healer_info = 'Лекарь — могущественный заклинатель.'
            print(f'{healer_info} Черпает силы из природы, веры и духов.')
        press = 'Нажми (Y), чтобы подтвердить выбор,'
        button = 'или любую другую кнопку'
        other = 'чтобы выбрать другого персонажа '
        approve_choice = input(f'{press} или {button}, {other}').lower()
    return char_class


def main():
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class = choice_char_class()
    print(start_training(char_name, char_class))


main()
