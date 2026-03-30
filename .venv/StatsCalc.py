
import matplotlib.pyplot as plt


def statsCalc(results):
    if not results:
        print("No results to analyze.")
        return

    component_health_keys = {
        "Engine": "engine_health",
        "Fuel": "fuel_health",
        "Avionics": "avionics_health",
        "Wing Left": "wing_left_health",
        "Wing Right": "wing_right_health",
    }

    damaged_runs = {component: 0 for component in component_health_keys}
    failed_when_damaged = {component: 0 for component in component_health_keys}

    for result in results:
        mission_failed = not result["mission_success"]

        for component, health_key in component_health_keys.items():
            if result[health_key] < 100:
                damaged_runs[component] += 1
                if mission_failed:
                    failed_when_damaged[component] += 1

    components = list(component_health_keys.keys())
    failure_rates = []
    failure_rate_ratios = []
    damage_samples = []

    for component in components:
        if damaged_runs[component] == 0:
            failure_rates.append(0)
            failure_rate_ratios.append(0)
        else:
            ratio = failed_when_damaged[component] / damaged_runs[component]
            rate = ratio * 100
            failure_rates.append(rate)
            failure_rate_ratios.append(ratio)

    for result in results:
        mission_failed = not result["mission_success"]
        for health_key in component_health_keys.values():
            damage_amount = max(0, 100 - result[health_key])
            if damage_amount > 0:
                damage_samples.append((damage_amount, mission_failed))

    print("Mission failure frequency when each component is damaged:")
    for component in components:
        print(
            f"{component}: {failed_when_damaged[component]}/{damaged_runs[component]} failed "
            f"({(failed_when_damaged[component] / damaged_runs[component] * 100) if damaged_runs[component] else 0:.1f}%)"
        )

    plt.figure(figsize=(10, 6))
    bars = plt.bar(components, failure_rates, color="#3a7ca5")
    plt.title("Mission Failure Rate When Component Is Damaged")
    plt.xlabel("Damaged Component")
    plt.ylabel("Failure Rate (%)")
    plt.ylim(0, 100)
    plt.grid(axis="y", linestyle="--", alpha=0.35)

    for i, bar in enumerate(bars):
        component = components[i]
        label = f"{failed_when_damaged[component]}/{damaged_runs[component]}"
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 1,
            label,
            ha="center",
            va="bottom",
            fontsize=9,
        )

    plt.tight_layout()

    plt.figure(figsize=(10, 6))
    bars = plt.bar(components, failure_rate_ratios, color="#ef8354")
    plt.title("Failure Rate Ratio by Damaged Component")
    plt.xlabel("Damaged Component")
    plt.ylabel("failure_rate = failures_when_hit / times_hit")
    plt.ylim(0, 1)
    plt.grid(axis="y", linestyle="--", alpha=0.35)

    for i, bar in enumerate(bars):
        component = components[i]
        label = f"{failed_when_damaged[component]}/{damaged_runs[component]}"
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 0.02,
            label,
            ha="center",
            va="bottom",
            fontsize=9,
        )

    plt.tight_layout()

    if not damage_samples:
        print("No damage samples were found for damage-level analysis.")
        plt.show()
        return

    bin_ranges = [
        (1, 20),
        (21, 40),
        (41, 60),
        (61, 80),
        (81, 100),
        (101, 200),
    ]
    bin_labels = [f"{low}-{high}" for low, high in bin_ranges]
    bin_totals = [0] * len(bin_ranges)
    bin_failures = [0] * len(bin_ranges)

    for damage_amount, mission_failed in damage_samples:
        for index, (low, high) in enumerate(bin_ranges):
            if low <= damage_amount <= high:
                bin_totals[index] += 1
                if mission_failed:
                    bin_failures[index] += 1
                break

    failure_probability_by_bin = []
    for index in range(len(bin_ranges)):
        if bin_totals[index] == 0:
            failure_probability_by_bin.append(0)
        else:
            failure_probability_by_bin.append(bin_failures[index] / bin_totals[index])

    plt.figure(figsize=(11, 6))
    bars = plt.bar(bin_labels, failure_probability_by_bin, color="#2d936c")
    plt.title("Failure Probability vs Damage Level")
    plt.xlabel("Damage Level")
    plt.ylabel("Failure Probability")
    plt.ylim(0, 1)
    plt.grid(axis="y", linestyle="--", alpha=0.35)

    for i, bar in enumerate(bars):
        label = f"{bin_failures[i]}/{bin_totals[i]}"
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 0.02,
            label,
            ha="center",
            va="bottom",
            fontsize=9,
        )

    plt.tight_layout()
    plt.show()