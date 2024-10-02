input_string = "aahjkehdowhjgsdjayiasg"

# Create an empty dictionary to store the frequency of each character
frequency = {}
s1= list(input_string)
# Iterate over each character in the string
for char in s1:
    # If the character is already in the dictionary, increment its count
    if char in frequency:
        frequency[char] += 1
    # If the character is not in the dictionary, add it with a count of 1
    else:
        frequency[char] = 1


output_string = ''.join([f"{char}{count}" for char, count in frequency.items()])
print(output_string)