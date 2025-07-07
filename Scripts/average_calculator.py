from collections import defaultdict
from statistics import mean

MAX_TRIALS = 10
TRIAL_SIZE = 20

def parse_confidence_data(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    results = defaultdict(list)
    current_group = None
    current_trial = []

    for line in lines:
        line = line.strip()
        if "%" in line:  # Start of a new group like "100% Real:" 
            if current_group and current_trial:
                results[current_group].append(current_trial)
                current_trial = []
            current_group = line
        elif "-> Estimated Whales Confidence:" in line and current_group:
            try:
                value = float(line.split(":")[-1].strip())
                current_trial.append(value)
                if len(current_trial) == TRIAL_SIZE:
                    results[current_group].append(current_trial)
                    current_trial = []
            except ValueError:
                continue

    # Catch remaining trial if any
    if current_group and current_trial:
        results[current_group].append(current_trial) 

    return results

def compute_averages(results):
    avg_results = {}
    for group, trials in results.items():
        avg_results[group] = [round(mean(trial), 4) for trial in trials]
    return avg_results

# Example usage
file_path = "whale_confidence_data.txt"
data = parse_confidence_data(file_path)
averages = compute_averages(data)

for group, avg_list in averages.items():
    print(f"{group}:")
    for i, avg in enumerate(avg_list, 1):
        print(f"  Trial {i}: {avg}")