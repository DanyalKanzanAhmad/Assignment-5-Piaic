def is_prime(n):

    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def main():
    name = input("Hi! What's your name? ")

    print(f"Hey man, {name}! Please enter three your favorite numbers.")
    numbers = []
    for i in range(1, 4):
        num = int(input(f"Enter number {i}: "))
        numbers.append(num)

    even_odd_info = [(num, "even" if num % 2 == 0 else "odd") for num in numbers]

    print(f"\nThank you, {name}! You've entered the numbers: {numbers}.")

    print("\nHere's whether each of your numbers is even or odd:")
    for num, even_odd in even_odd_info:
        print(f"The number {num} is {even_odd}.")

    print("\nLet's see the squares of your favorite numbers:")
    for num in numbers:
        square = num**2
        print(f"The square of {num} is {square}.")

    total_sum = sum(numbers)
    print(f"\nThe sum of your favorite numbers is: {total_sum}.")

    if is_prime(total_sum):
        print(
            f"Wow, {name}! The sum of your numbers is {total_sum}, which is a prime number! That's awesome!"
        )
    else:
        print(
            f"The sum of your numbers is {total_sum}. It's not a prime number, but it's still a great choice!"
        )


if __name__ == "__main__":
    main()
