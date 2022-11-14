knight_name = 'Jhon'
knight_damage = 40

dragon_name = 'Neltharion'
dragon_hp = 100

dinosaur_name = 'T-rex'
dinosaur_hp = 1000


def knight_make_damage(damage: int, target_hp: int) -> int:
    target_hp = target_hp - knight_damage
    return target_hp


def fight(knight_damage: int, target_name: str, target_hp: int, gratz_message: str = 'Ты молодец!') -> None:
    """Проверяет что хотя бы у одной ставки пользователя есть допуск к переторжке"""
    while True:
        target_hp = knight_make_damage(knight_damage, target_hp)
        if target_hp > 0:
            print(f'{target_name} не побежден')
            continue
        print(f'{target_name} побежден')
        print(gratz_message)
        break


fight(knight_damage=knight_damage, target_name=dragon_name, target_hp=dragon_hp)
fight(knight_damage, dragon_name, dragon_hp, 'Это был слабый дракон')
