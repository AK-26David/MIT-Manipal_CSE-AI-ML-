def water_jug_dfs(capacity_a, capacity_b, target):
    visited_states = set()

    def dfs(state):
        if state in visited_states:
            return False

        visited_states.add(state)

        a, b = state

        # Check if the target is reached
        if a == target or b == target:
            print(f"Found a solution: ({a}, {b})")
            return True

        # Actions: Fill Jug A, Fill Jug B, Empty Jug A, Empty Jug B,
        # Pour water from Jug A to Jug B, Pour water from Jug B to Jug A

        # Fill Jug A
        if a < capacity_a:
            if dfs((capacity_a, b)):
                print(f"Fill Jug A: ({a}, {b}) -> ({capacity_a}, {b})")
                return True

        # Fill Jug B
        if b < capacity_b:
            if dfs((a, capacity_b)):
                print(f"Fill Jug B: ({a}, {b}) -> ({a}, {capacity_b})")
                return True

        # Empty Jug A
        if a > 0:
            if dfs((0, b)):
                print(f"Empty Jug A: ({a}, {b}) -> (0, {b})")
                return True

        # Empty Jug B
        if b > 0:
            if dfs((a, 0)):
                print(f"Empty Jug B: ({a}, {b}) -> ({a}, 0)")
                return True

        # Pour water from Jug A to Jug B
        if a > 0 and b < capacity_b:
            pour_amount = min(a, capacity_b - b)
            if dfs((a - pour_amount, b + pour_amount)):
                print(f"Pour from Jug A to Jug B: ({a}, {b}) -> ({a - pour_amount}, {b + pour_amount})")
                return True

        # Pour water from Jug B to Jug A
        if b > 0 and a < capacity_a:
            pour_amount = min(b, capacity_a - a)
            if dfs((a + pour_amount, b - pour_amount)):
                print(f"Pour from Jug B to Jug A: ({a}, {b}) -> ({a + pour_amount}, {b - pour_amount})")
                return True

        return False

    start_state = (0, 0)
    if not dfs(start_state):
        print("No solution found.")

if __name__ == "__main__":
    capacity_jug_a = int(input("Enter the capacity of Jug A: "))
    capacity_jug_b = int(input("Enter the capacity of Jug B: "))
    target_amount = int(input("Enter the target amount of water: "))

    water_jug_dfs(capacity_jug_a, capacity_jug_b, target_amount)
