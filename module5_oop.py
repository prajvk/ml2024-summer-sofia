class NumberGames:
    def __init__(self):
        self.numbers = []

    def get_num_values_N(self):
        while True:
            try:
                N = int(input("Enter the number of values N: "))
                if N > 0:
                    return N
                else:
                    print("Number of elements cannot be negative or 0. Please enter a positive integer greater than 0.")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

    def get_all_numbers(self, N):
        print(f"Please enter {N} numbers one by one")
        for i in range(N):
            while True:
                try:
                    num = int(input(f"Enter number {i+1}: "))
                    self.numbers.append(num)
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid integer.")

    def get_X(self):
        while True:
            try:
                X = int(input("Enter an integer X: "))
                return X
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

    def search_X(self, X):
        self.X = X
        if self.X in self.numbers:
            return self.numbers.index(X) + 1
        else:
            return -1

def main():
    call_numbers = NumberGames()
    N = call_numbers.get_num_values_N()
    call_numbers.get_all_numbers(N)
    X = call_numbers.get_X()
    result = call_numbers.search_X(X)
    print(result)

if __name__ == "__main__":
    main()
