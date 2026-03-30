import random

def randomHits():
    numberHits = random.randint(1, 3)
    part = []
    damage = []
    for i in range(numberHits):
        part.append(random.randint(1, 3))
        damage.append(random.randint(1, 50))

    for i in range(numberHits):
        print(f"part: {part[i]}")
        print(f"damage: {damage[i]}")

randomHits()