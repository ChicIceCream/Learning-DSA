def greedy_knapsack(weights, values, capacity):
    n = len(weights)
    ratios = [(values[i] / weights[i], weights[i], values[i]) for i in range(n)]
    ratios.sort(reverse=True, key=lambda x: x[0])

    total_value = 0
    remaining_capacity = capacity
    selected_items = []

    for ratio, weight, value in ratios:
        if remaining_capacity >= weight:
            selected_items.append((weight, value))
            total_value += value
            remaining_capacity -= weight

    return total_value, selected_items

# Example usage:
weights = [2, 3, 5, 7, 1, 4, 6]
values = [10, 5, 15, 7, 8, 9, 4]
capacity = 15

result_value, result_items = greedy_knapsack(weights, values, capacity)
print("Total value:", result_value)
print("Selected items:", result_items)
