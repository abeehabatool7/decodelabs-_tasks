"""
DecodeLabs - Industrial Training Kit
Project 3: Enterprise Random Password Generator

Goal: Ask the user for a password length and generate a random,
complex password using letters, numbers, and symbols.

Key concepts demonstrated:
- Library integration: string (character pools) + secrets (secure randomness)
- secrets.choice() instead of random.choice() -> cryptographically secure,
  not predictable (random's Mersenne Twister is not safe for passwords)
- ''.join(list) instead of string += char in a loop -> O(N) instead of O(N^2)
- Input validation (Phase 1: environmental requirements)
- NIST SP 800-63-4 (2024): prioritize length; min 15 recommended for
  high-security contexts, so we default/nudge users toward longer passwords
"""

import string
import secrets


def generate_password(length: int) -> str:
    """Generate a cryptographically secure random password of given length."""
    # Character pool: letters + digits + punctuation
    character_pool = string.ascii_letters + string.digits + string.punctuation

    # Use secrets.choice (not random.choice) for each character,
    # then join all at once for efficiency
    password = ''.join(secrets.choice(character_pool) for _ in range(length))
    return password


def get_valid_length() -> int:
    """Phase 1: Input validation - keep asking until we get a valid integer."""
    while True:
        raw = input("Enter desired password length (min 8, recommended 15+): ").strip()
        try:
            length = int(raw)
        except ValueError:
            print("  ⚠ Please enter a whole number.\n")
            continue

        if length < 8:
            print("  ⚠ For basic security, length must be at least 8.\n")
            continue

        if length < 15:
            print("  ℹ Note: NIST 2024 guidelines recommend 15+ characters")
            print("    for high-security contexts. Proceeding anyway.\n")

        return length


def main():
    print("=" * 45)
    print("   DECODELABS RANDOM PASSWORD GENERATOR")
    print("=" * 45)

    length = get_valid_length()
    password = generate_password(length)

    print("\n" + "-" * 45)
    print(f"Generated Password ({length} chars):")
    print(f"  {password}")
    print("-" * 45)


if __name__ == "__main__":
    main()
