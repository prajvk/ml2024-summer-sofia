N = int(input("\nPlease enter the number of elements N:"))

print(f"\nNow provide the values of the {N} elements one at a time\n")

numbers = []

for i in range(N):
    num = int(input(f"Number {i+1} = "))
    numbers.append(num)

X = int(input("\nEnter a number to search:"))

if X in numbers:
    print(numbers.index(X)+1)
else:
    print(-1)