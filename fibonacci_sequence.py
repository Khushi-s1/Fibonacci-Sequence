def generate_fibonacci_sequence(num_terms):
    # Initialize first two terms of the Fibonacci sequence
    fib_sequence = [0, 1]

    # Generate Fibonacci sequence
    for i in range(2, num_terms):
        next_term = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_term)

    return fib_sequence

def main():
    try:
        num_terms = int(input("Enter the number of terms for Fibonacci sequence: "))

        if num_terms <= 0:
            print("Please enter a positive integer.")
            return

        fibonacci_sequence = generate_fibonacci_sequence(num_terms)

        print(f"Fibonacci sequence up to {num_terms} terms:")
        print(fibonacci_sequence)

    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
