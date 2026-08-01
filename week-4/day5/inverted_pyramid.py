n = int(input("Enter number: "))

for i in range(n):
    for j in range(i):
        print(" ", end="")

    # Print stars
    for k in range((2 * n - 1) - (2 * i)):
        print("*", end="")

    # Move to next line
    print()