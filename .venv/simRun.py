from RandomHit import randomHits
from Components import printcomponents
from Calculations import calcSurvival

def main():
    ##for i in range(1000):
        simulateFlight()

def simulateFlight():
    components = [
    {"name": "engine", "health": 100, "failure": 0},
    {"name": "fuel", "health": 100, "failure": 30},
    {"name": "avionics", "health": 100, "failure": 30},
    {"name": "wing_left", "health": 100, "failure": 0},
    {"name": "wing_right", "health": 100, "failure": 0}]

    part, damage = randomHits()
    probSurvival, components= calcSurvival(part, damage, components)
    print(f"prob survival {probSurvival}\n")
    printcomponents(components)
    print(probSurvival)
    

if __name__ == "__main__":
    main()