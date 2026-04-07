import random

def simulate_crashes(days: int) -> float:
    """Simulates a theoretical 4.5% daily crash probability."""
    PROBABILITY = 0.045
    crashes = sum(1 for _ in range(days) if random.random() < PROBABILITY)
    return crashes / days

def run_simulation_report():
    print("\n--- Monte Carlo Simulation: Server Crashes (Target: 4.5%) ---")
    for days in [30, 1000, 10000]:
        prob = simulate_crashes(days)
        error = abs(0.045 - prob)
        print(f"Days: {days:6} | Simulated Prob: {prob:.4%} | Variance from Target: {error:.4%}")
