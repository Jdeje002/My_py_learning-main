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