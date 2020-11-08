from stack import Stack
from builders import RandomStackBuilder, ConcreteStackBuilder


def fight(stack1, stack2):
    damage1 = stack1._number * stack1._damage * (stack1._attack - stack2._defence)
    if damage1 < 0:
        damage1 = 0
    stack2.get_damage(damage1)
    if stack2._is_dead:
        return
    else:
        if stack1._retaliation:
            damage2 = stack2._number * stack2._damage * (stack2._attack - stack1._defence)
            if damage2 < 0:
                damage2 = 0
            stack1.get_damage(damage2)


def check_alive(stack1, stack2):
    if stack1._is_dead:
        print("Second stack won this battle")
        return False

    if stack2._is_dead:
        print("First stack won this battle")
        return False

    return True


def fight_to_death(stack1: Stack, stack2: Stack):

    if stack1._is_dead or stack2._is_dead:
        print("I'm really sorry, but some of these creatures are dead")
    
    else:
        while True:
            fight(stack1, stack2)
            if not check_alive(stack1, stack2):
                break

            fight(stack2, stack1)
            if not check_alive(stack1, stack2):
                break


concrete_builder = ConcreteStackBuilder()
concrete_builder.set_attack(20)
concrete_builder.set_defence(20)
concrete_builder.set_damage(50)
concrete_builder.set_max_health(200)
concrete_builder.set_number(3)

random_builder = RandomStackBuilder()
random_builder.set_attack()
random_builder.set_defence()
random_builder.set_damage()
random_builder.set_max_health()
random_builder.set_number()
random_builder.make_no_retaliation()

angels = concrete_builder.get_stack()
random_creatures = random_builder.get_stack()

fight_to_death(angels, random_creatures)
                    
