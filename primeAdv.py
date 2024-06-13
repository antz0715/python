def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_primes(limit):
    """Generate a list of prime numbers up to a specified limit."""
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def main():
    while True:
        print("\nPrime Number Checker and List Generator")
        print("1. Check if a number is prime")
        print("2. Generate a list of prime numbers up to a limit")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            number = int(input("Enter a number to check if it is prime: "))
            if is_prime(number):
                print(f"{number} is a prime number.")
            else:
                print(f"{number} is not a prime number.")
        
        elif choice == '2':
            limit = int(input("Enter the limit to generate prime numbers up to: "))
            primes = generate_primes(limit)
            print(f"Prime numbers up to {limit}: {primes}")
        
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
