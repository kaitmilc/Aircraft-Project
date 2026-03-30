def calcSurvival(parts, damage, components):
    prob_failure = 0
    failure_cause = None

    for i in range(len(parts)):
        components[parts[i]]["health"] -= damage[i]

    for i in range(len(components)):
        if components[i]["health"] <= 0:
            prob_failure += 1
            failure_cause = components[i]["name"]
        elif components[i]["health"] < 70 and components[i]["health"] > 50:
            prob_failure += 0.1
        elif components[i]["health"] < 50 and components[i]["health"] > 10:
            prob_failure += 0.5
        elif components[i]["health"] <= 10:
            prob_failure += 0.9
        elif prob_failure > .85:
            failure_cause = "Combination"

    mission_success = prob_failure < 0.85

    run_result = {
        "mission_success": mission_success,
        "failure_cause": failure_cause,
        "engine_health":     next(c["health"] for c in components if c["name"] == "engine"),
        "fuel_health":       next(c["health"] for c in components if c["name"] == "fuel"),
        "avionics_health":   next(c["health"] for c in components if c["name"] == "avionics"),
        "wing_left_health":  next(c["health"] for c in components if c["name"] == "wing_left"),
        "wing_right_health": next(c["health"] for c in components if c["name"] == "wing_right"),
    }

    return run_result