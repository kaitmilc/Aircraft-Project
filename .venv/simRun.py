from RandomHit import randomHits
from Components import printcomponents
from Calculations import calcSurvival
from StatsCalc import statsCalc
results = []

def main():
    for i in range(1000):
        simulateFlight()

    statsCalc(results)

    

def simulateFlight():
    components = [
    {"name": "engine", "health": 100, "failure": 0},
    {"name": "fuel", "health": 100, "failure": 30},
    {"name": "avionics", "health": 100, "failure": 30},
    {"name": "wing_left", "health": 100, "failure": 0},
    {"name": "wing_right", "health": 100, "failure": 0}]

    part, damage = randomHits()
    result = calcSurvival(part, damage, components)
    results.append(result)
    

if __name__ == "__main__":
    main()