import getpass

def luhn_check(card_number):
    # Convert the card number to a list of integers
    digits = [int(x) for x in card_number if x.isdigit()]

    # Double every second digit, starting from the right
    for i in range(len(digits) - 2, -1, -2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9

    # Sum all the digits
    total = sum(digits)

    # Check if the sum modulo 10 equals 0
    return total % 10 == 0

if __name__ == "__main__":
    card_number = getpass.getpass("Enter card number: ")

    if luhn_check(card_number):
        print("Valid Luhn Check!")
    else:
        print("Invalid Luhn Check!")
