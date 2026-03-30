import random

def randomHits():
    numberHits = random.randint(1, 5)
    part = []
    damage = []
    for i in range(numberHits):
        part.append(random.randint(0, 4))
        damage.append(random.randint(1, 100))
    return part, damage
