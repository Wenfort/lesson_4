#class Dragon:
#    name = 'Neltharion'
#    hitpoints = 100


#class Knight:
#    name = 'Jhon'
#    damage = 30

#    def make_damage(self, target_hp: int):
#        target_hp = target_hp - self.damage
#        return target_hp


#class Dinosaur:
#    name = 'T-rex'
#    hitpoint = 1000


#dragon = Dragon()
#knight = Knight()
#dinosaur = Dinosaur()

#knight.make_damage(Dragon.hitpoints)


def speak(animal):
    if isinstance(animal, Cat):
        animal.meow()
    elif isinstance(animal, Dog):
        animal.woof()


class Animal:

    def eat(self):
        print('Ням-ням')


class Dog(Animal):
    def woof(self, cat_phrase: str = 'Мяу') -> None:
        print(f'Собака говорит Гав')


class Cat(Animal):
    def __init__(self, name: str, color: str, escapes: int = 0, paws_amount: int = 4):
        self.name = name
        self.color = color
        self.escapes = escapes
        self.paws_amount = paws_amount

    def meow(self, cat_phrase: str = 'Мяу') -> None:
        print(f'Кот {self.name} говорит "{cat_phrase}"')

    def eat(self):
        print('Киса ням-ням')

    @property
    def info(self):
        return f'У кота {self.name} {self.escapes} побег и {self.paws_amount} лапки'


tigra = Cat(name='Тигра', color='ginger', escapes=1)
cat_description = tigra.info
tigra.eat()
dog = Dog()
speak(tigra)
speak(dog)


tigra = Cat(name='Тигра', color='ginger', escapes=1)
print(tigra.name)
print(f'У {tigra.name} {tigra.paws_amount} лапки и {tigra.escapes} побег! ')
tigra.meow()
speak(tigra)
print('----------')
matroskin = Cat(name='Матроскин', color='stipes', escapes=2)
print(matroskin.name)
print(f'У {matroskin.name} {matroskin.paws_amount} лапки и {matroskin.escapes} побега! ')
matroskin.meow('Покормите пожалуйста!')
some_string = 'Тигра'
some_string_len = len(some_string)
some_string = some_string.replace('и', 'И')

