def greedy_algorithm(items, budget):
    # Calculate calorie-to-cost ratio for each food item
    ratios = {item: data["calories"] / data["cost"] for item, data in items.items()}
    
    # Sort food items based on calorie-to-cost ratio in descending order
    sorted_items = sorted(items.keys(), key=lambda x: ratios[x], reverse=True)
    
    selected_items = []
    total_cost = 0
    total_calories = 0
    
    # Select items greedily based on their ratio until budget is exhausted
    for item in sorted_items:
        if total_cost + items[item]["cost"] <= budget:
            selected_items.append(item)
            total_cost += items[item]["cost"]
            total_calories += items[item]["calories"]
    
    return selected_items, total_cost, total_calories

def dynamic_programming(items, budget):
    # Extract item names, costs and calories
    item_names = list(items.keys())
    n = len(item_names)
    
    # Create a 2D array for dynamic programming
    # dp[i][j] represents the maximum calories with budget j using the first i items
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]
    
    # Fill the dp table
    for i in range(1, n + 1):
        item = item_names[i-1]
        cost = items[item]["cost"]
        calorie = items[item]["calories"]
        
        for j in range(budget + 1):
            if cost <= j:
                # Choose the maximum of either including the current item or not
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-cost] + calorie)
            else:
                # Can't afford this item with current budget j
                dp[i][j] = dp[i-1][j]
    
    # Backtrack to find the selected items
    selected_items = []
    remaining_budget = budget
    total_cost = 0
    
    for i in range(n, 0, -1):
        # If including this item gives a better result
        if dp[i][remaining_budget] != dp[i-1][remaining_budget]:
            item = item_names[i-1]
            selected_items.append(item)
            remaining_budget -= items[item]["cost"]
            total_cost += items[item]["cost"]
    
    return selected_items, total_cost, dp[n][budget]

def main():
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }
    
    budget = 100
    
    greedy_items, greedy_cost, greedy_calories = greedy_algorithm(items, budget)
    print("Greedy Algorithm:")
    print(f"Selected items: {greedy_items}")
    print(f"Total cost: {greedy_cost}")
    print(f"Total calories: {greedy_calories}")
    
    dp_items, dp_cost, dp_calories = dynamic_programming(items, budget)
    print("\nDynamic Programming:")
    print(f"Selected items: {dp_items}")
    print(f"Total cost: {dp_cost}")
    print(f"Total calories: {dp_calories}")
    
    print("\nComparison:")
    if greedy_calories == dp_calories:
        print("Both algorithms found solutions with the same calorie count.")
    else:
        winner = "Greedy" if greedy_calories > dp_calories else "Dynamic Programming"
        print(f"{winner} algorithm found a better solution.")

if __name__ == "__main__":
    main()
