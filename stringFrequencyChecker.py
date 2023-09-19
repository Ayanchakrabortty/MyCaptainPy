def most_frequent(input_string):
   
    letter_frequency = {}

    for char in input_string:
        if char.isalpha():
            char = char.lower()  
            if char in letter_frequency:
                letter_frequency[char] += 1
            else:
                letter_frequency[char] = 1

    sorted_frequency = sorted(letter_frequency.items(), key=lambda x: x[1], reverse=True)
    for item in sorted_frequency:
        print(f"{item[0]} = {item[1]} ")
input_string = input("Enter a string: ")


most_frequent(input_string)
