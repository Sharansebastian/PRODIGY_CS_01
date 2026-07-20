def caesar_encrypt(message: str, shift: int) -> str:
    """Encrypt a message using the Caesar cipher with the given shift."""
    return _shift_message(message, shift)


def caesar_decrypt(message: str, shift: int) -> str:
    """Decrypt a message using the Caesar cipher with the given shift."""
    return _shift_message(message, -shift)


def _shift_message(message: str, shift: int) -> str:
    """Shift each letter in the message by `shift` positions, preserving
    case and leaving non-alphabetic characters unchanged."""
    result = []
    shift = shift % 26  # normalize shift to 0-25

    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26 + base
            result.append(chr(shifted))
        else:
            result.append(char)

    return ''.join(result)


def get_shift_value() -> int:
    """Prompt the user for a valid integer shift value."""
    while True:
        try:
            return int(input("Enter shift value (integer): ").strip())
        except ValueError:
            print("Invalid input. Please enter a whole number (e.g., 3, -5, 13).")


def main():
    print("=== Caesar Cipher Tool ===")
    print("1. Encrypt")
    print("2. Decrypt")

    while True:
        choice = input("Choose an option (1 or 2): ").strip()
        if choice in ('1', '2'):
            break
        print("Invalid choice. Please enter 1 or 2.")

    message = input("Enter your message: ")
    shift = get_shift_value()

    if choice == '1':
        output = caesar_encrypt(message, shift)
        print(f"\nEncrypted message: {output}")
    else:
        output = caesar_decrypt(message, shift)
        print(f"\nDecrypted message: {output}")


if __name__ == "__main__":
    main()
