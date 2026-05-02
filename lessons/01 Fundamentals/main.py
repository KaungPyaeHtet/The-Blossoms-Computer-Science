def predict_number():
    print("Think of a number between 1 and 10. I'll predict it!")
    print()

    low = 1
    high = 10
    attempts = 0

    while low <= high:
        guess = (low + high) // 2
        attempts += 1

        print(f"Is your number {guess}?")
        answer = input("Enter 'y' for yes, 'h' if higher, 'l' if lower: ").strip().lower()

        if answer == 'y':
            print(f"\nI predicted your number in {attempts} attempt(s)!")
            return
        elif answer == 'h':
            low = guess + 1
        elif answer == 'l':
            high = guess - 1
        else:
            print("Please enter 'y', 'h', or 'l'.")
            attempts -= 1

    print("\nHmm, something went wrong. Are you sure you picked a number between 1 and 10?")


predict_number()
