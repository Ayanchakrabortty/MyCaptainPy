
try:
    input_list = input("Enter a list of integers separated by spaces: ")
    input_list = list(map(int, input_list.split()))
 
    positive_integers = [num for num in input_list if num > 0]
    if positive_integers:
        print("Positive integers in the list:", positive_integers)
    else:
        print("No positive integers in the list.")
except ValueError:
    print("Invalid input. Please enter a valid list of integers.")
