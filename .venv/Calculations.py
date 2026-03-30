def calcSurvival(parts, damage, components):
    probFailure = 0

    for i in range(len(parts)):
        components[parts[i]]["health"] -= damage[i]

    for i in range(len(components)):
        if components[i]["health"] <= 0:
            probFailure += 1
        elif components[i]["health"] < 70 and components[i]["health"] > 50:
            probFailure += 0.1
        elif components[i]["health"] < 50 and components[i]["health"] > 10:
            probFailure += 0.5
        elif components[i]["health"] <= 10:
            probFailure += 0.9

    if probFailure >= .85:
        missionSuccess = False
    else: 
        missionSuccess = True


    return probFailure, components