def water_jug_bfs(capacity_a, capacity_b, target):
    visited_states = set()
    queue = [(0, 0, [])]

    while queue:
        current_state = queue.pop(0)
        a, b, path = current_state

        if current_state[:2] in visited_states:
            continue

        visited_states.add(current_state[:2])

        if a == target or b == target:
            print(f"Found a solution: ({a}, {b})")
            print("Path:", path)
            return

        # Actions: Fill Jug A, Fill Jug B, Empty Jug A, Empty Jug B,
        # Pour water from Jug A to Jug B, Pour water from Jug B to Jug A

        # Fill Jug A
        if a < capacity_a:
            queue.append((capacity_a, b, path + [f"Fill Jug A: ({a}, {b}) -> ({capacity_a}, {b})"]))

        # Fill Jug B
        if b < capacity_b:
            queue.append((a, capacity_b, path + [f"Fill Jug B: ({a}, {b}) -> ({a}, {capacity_b})"]))

        # Empty Jug A
        if a > 0:
            queue.append((0, b, path + [f"Empty Jug A: ({a}, {b}) -> (0, {b})"]))

        # Empty Jug B
        if b > 0:
            queue.append((a, 0, path + [f"Empty Jug B: ({a}, {b}) -> ({a}, 0)"]))

        # Pour water from Jug A to Jug B
        if a > 0 and b < capacity_b:
            pour_amount = min(a, capacity_b - b)
            queue.append((a - pour_amount, b + pour_amount, path + [f"Pour from Jug A to Jug B: ({a}, {b}) -> ({a - pour_amount}, {b + pour_amount})"]))

        # Pour water from Jug B to Jug A
        if b > 0 and a < capacity_a:
            pour_amount = min(b, capacity_a - a)
            queue.append((a + pour_amount, b - pour_amount, path + [f"Pour from Jug B to Jug A: ({a}, {b}) -> ({a + pour_amount}, {b - pour_amount})"]))

    print("No solution found.")

if __name__ == "__main__":
    capacity_jug_a = int(input("Enter the capacity of Jug A: "))
    capacity_jug_b = int(input("Enter the capacity of Jug B: "))
    target_amount = int(input("Enter the target amount of water: "))

    water_jug_bfs(capacity_jug_a, capacity_jug_b, target_amount)
