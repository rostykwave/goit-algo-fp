import random
import matplotlib.pyplot as plt
import numpy as np

def roll_dice():
    """Simulate rolling a single die and return the result (1-6)."""
    return random.randint(1, 6)

def monte_carlo_dice_simulation(num_trials):
    """
    Perform a Monte Carlo simulation of rolling two dice.
    
    Args:
        num_trials: The number of times to roll the dice.
        
    Returns:
        A tuple of (probabilities dict, counts dict)
    """
    # Initialize a dictionary to count occurrences of each sum
    sum_counts = {i: 0 for i in range(2, 13)}
    
    # Perform the simulation
    for _ in range(num_trials):
        die1 = roll_dice()
        die2 = roll_dice()
        dice_sum = die1 + die2
        sum_counts[dice_sum] += 1
    
    # Calculate probabilities
    sum_probabilities = {key: value / num_trials for key, value in sum_counts.items()}
    
    return sum_probabilities, sum_counts

def get_theoretical_probabilities():
    """
    Return the theoretical probabilities for each sum when rolling two dice.
    """
    return {
        2: 1/36,   # 2.78%
        3: 2/36,   # 5.56%
        4: 3/36,   # 8.33%
        5: 4/36,   # 11.11%
        6: 5/36,   # 13.89%
        7: 6/36,   # 16.67%
        8: 5/36,   # 13.89%
        9: 4/36,   # 11.11%
        10: 3/36,  # 8.33%
        11: 2/36,  # 5.56%
        12: 1/36,  # 2.78%
    }

def display_results_table(monte_carlo_probs, theoretical_probs, sum_counts, num_trials):
    """Display a comparison table of Monte Carlo vs theoretical probabilities."""
    print("\nResults of the two-dice rolling simulation:")
    print(f"{'Sum':<6}{'Monte Carlo (frequency)':<30}{'Theoretical probability':<30}{'Difference':<10}")
    print("-" * 76)
    
    for i in range(2, 13):
        mc_prob = monte_carlo_probs[i]
        theo_prob = theoretical_probs[i]
        count = sum_counts[i]
        
        # Calculate the absolute difference
        diff = abs(mc_prob - theo_prob)
        
        print(f"{i:<6}{mc_prob*100:.2f}% ({count}/{num_trials}){'':<5}{theo_prob*100:.2f}% ({theo_prob*36:.0f}/36){'':<5}{diff*100:.4f}%")

def create_comparison_plot(monte_carlo_probs, theoretical_probs):
    """Create and display a bar chart comparing Monte Carlo and theoretical probabilities."""
    sums = list(range(2, 13))
    mc_values = [monte_carlo_probs[i] * 100 for i in sums]
    theo_values = [theoretical_probs[i] * 100 for i in sums]
    
    x = np.arange(len(sums))  # the label locations
    width = 0.35  # the width of the bars
    
    fig, ax = plt.subplots(figsize=(12, 8))
    rects1 = ax.bar(x - width/2, mc_values, width, label='Monte Carlo')
    rects2 = ax.bar(x + width/2, theo_values, width, label='Theoretical')
    
    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_xlabel('Sum of dice')
    ax.set_ylabel('Probability (%)')
    ax.set_title('Comparison of probabilities for sums when rolling two dice')
    ax.set_xticks(x)
    ax.set_xticklabels(sums)
    ax.legend()
    
    # Add value labels on top of each bar
    def autolabel(rects):
        for rect in rects:
            height = rect.get_height()
            ax.annotate(f'{height:.2f}%',
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')
    
    autolabel(rects1)
    autolabel(rects2)
    
    fig.tight_layout()
    plt.savefig('dice_simulation_results.png')
    plt.show()

def main():
    # Set the number of trials for the Monte Carlo simulation
    num_trials = 1_000_000
    
    print(f"Simulating two-dice rolls using the Monte Carlo method ({num_trials:,} rolls)")
    
    # Run the Monte Carlo simulation
    monte_carlo_probs, sum_counts = monte_carlo_dice_simulation(num_trials)
    
    # Get theoretical probabilities
    theoretical_probs = get_theoretical_probabilities()
    
    # Display results as a table
    display_results_table(monte_carlo_probs, theoretical_probs, sum_counts, num_trials)
    
    # Create and display a comparison plot
    create_comparison_plot(monte_carlo_probs, theoretical_probs)
    
    print("\nConclusion:")
    print("The results of the Monte Carlo simulation are close to the theoretical probabilities.")
    print("As the number of trials increases, the simulation results converge to the theoretical values.")

if __name__ == "__main__":
    main()
