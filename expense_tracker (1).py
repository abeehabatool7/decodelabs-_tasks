"""
DecodeLabs - Industrial Training Kit
Project 2: Expense Tracker

Goal: Continuously accept expense entries from the user, add them up
using the Accumulator Pattern, and display the running/final total.

Key concepts demonstrated:
- Accumulator pattern (total = total + new_expense)
- State initialized OUTSIDE the loop (so it isn't wiped each iteration)
- Defensive coding with try/except to handle invalid (non-numeric) input
- A sentinel value ('done'/'quit') to break out of the loop gracefully
"""


def main():
    # --- Phase 1: Initialization (state lives OUTSIDE the loop) ---
    total = 0.0
    expense_count = 0

    print("=" * 40)
    print("   DECODELABS EXPENSE TRACKER")
    print("=" * 40)
    print("Enter an expense amount and press Enter.")
    print("Type 'done' (or 'quit') when you're finished.\n")

    # --- Phase 2: The Logic Skeleton (continuous audit loop) ---
    while True:
        user_input = input("Enter expense (or 'done' to finish): ").strip()

        # --- The Kill Switch: sentinel value check ---
        if user_input.lower() in ("done", "quit", "exit"):
            break

        # --- The Gatekeeper / Defensive Coding ---
        try:
            expense = float(user_input)
        except ValueError:
            print("  ⚠ Invalid input. Please enter a numeric amount.\n")
            continue

        if expense < 0:
            print("  ⚠ Expense cannot be negative. Try again.\n")
            continue

        # --- The Accumulator Pattern: State(new) = State(old) + Input ---
        total += expense
        expense_count += 1
        print(f"  ✓ Added {expense:.2f}. Running total: {total:.2f}\n")

    # --- Phase 3: Output (decoupled from the processing logic) ---
    print("=" * 40)
    print(f"Total expenses entered : {expense_count}")
    print(f"TOTAL SPENT            : {total:.2f}")
    print("=" * 40)


if __name__ == "__main__":
    main()
