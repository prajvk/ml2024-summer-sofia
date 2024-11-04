import module5_mod 
#NumberGames = 

def main():
    call_numbers = module5_mod.NumberGames()
    N = call_numbers.get_num_values_N()
    call_numbers.get_all_numbers(N)
    X = call_numbers.get_X()
    result = call_numbers.search_X(X)
    print(result)

if __name__ == "__main__":
    main()