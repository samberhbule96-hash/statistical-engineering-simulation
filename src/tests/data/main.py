import json
from src.stat_engine import StatEngine
from src.monte_carlo import run_simulation_report

def main():
    print("=== STATISTICAL ENGINEERING ANALYSIS ===")
    
    # 1. Load and Analyze Salary Data
    try:
        with open('data/sample_salaries.json', 'r') as f:
            data = json.load(f)
        
        engine = StatEngine(data)
        print(f"\nSalary Analysis (n={len(data)}):")
        print(f"Mean Salary:   ${engine.get_mean():,.2f}")
        print(f"Median Salary: ${engine.get_median():,.2f}")
        print(f"Std Deviation: ${engine.get_standard_deviation():,.2f}")
        
        outliers = engine.get_outliers(threshold=2)
        print(f"Extreme Outliers Found: {outliers}")
        
    except FileNotFoundError:
        print("Error: data/sample_salaries.json not found.")

    # 2. Run Probability Simulation
    run_simulation_report()

if __name__ == "__main__":
    main()
