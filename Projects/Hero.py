#Hero Object test

class hero (object):
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power
        self.coins = 0

    def attack(self, enemy):
        enemy.health -= self.power
        print("You do %d damage to the goblin." % self.power)
        if enemy.health <= 0:
            print("You killed the goblin!")

    def add_coins(self, coins):
        self.coins += coins
        print("You now have %d coins." % self.coins)

    def check_coins(self):
        print("You have %d coins." % self.coins)

    def rest(self):
        if self.health < 100:
            self.health += 1
            print("You feel a bit better.")


class enemy (object):
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def attack(self, hero):
        hero.health -= self.power
        print("The goblin does %d damage to you." % self.power)
        if hero.health <= 0:
            print("You have been killed by the goblin!")