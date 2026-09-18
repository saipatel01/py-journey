n = int(input("Enter number: "))

for i in range(1, n + 1):
    # Print leading spaces
    for j in range(n - i):
        print(" ", end="")

    # Print stars with spaces
    for k in range(i):
        print("*", end=" ")
        
    print()