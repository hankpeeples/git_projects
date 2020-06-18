import random


#breaking out of while loops / continuing / classes
print("\n- 1. Breaking out of while loops / Continuing / Classes / Instance Variables / ")

class Enemy: #class = blueprint for objects(variables kinda)
    hp = 200

    def __init__(self, atkl, atkh):
        self.atkl = atkl
        self.atkh = atkh

    def get_atk(self): #self is the class instance of the object
        print("atk is", self.atkl)

    def get_hp(self):
        print("hp is", self.hp)


enemy1 = Enemy(40, 49)
enemy1.get_atk()
enemy1.get_hp()

enemy2 = Enemy(75, 90)
enemy2.get_atk()
enemy2.get_hp()

'''

playerhp = 260
enemyatkl = 60
enemyatkh = 80

while playerhp > 0:
    dmg = random.randrange(enemyatkl, enemyatkh)
    playerhp = playerhp - dmg

    if playerhp <= 30:
        playerhp = 30
        
    print("Enemy strikes for", dmg, "points of damage. Current hp is", playerhp)

    if playerhp > 30:
        continue #everything after this is ignored and re-starts the loop
        
    print("You have low health. You've been teleported to the nearest med area.")
    break #exits while loop

'''