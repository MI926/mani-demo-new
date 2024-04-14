# This function counts the number of vowels in a given string

# Define the vowels
vowel = ["a", "e", "i", "o", "u"]


def vowel_count(string):

    # Convert the string to a list
    string_list = list(string)

    # Initialize vowel count to 0
    vowel_count = 0

    # Loop through each character in the string
    for char in string_list:

        # Check if it is a vowel
        if char in vowel:

            # If a vowel, increment the count
            vowel_count += 1

    # Check if there are at least 5 vowels
    if vowel_count >= 5:

        # Print yes if there are at least 5 vowels
        print("yes")

    # Return the vowel count
    return vowel_count


# Get input string from user
input_string = input("Enter the string: ")

# Call vowel_count function on input string
vowel_count(input_string)
