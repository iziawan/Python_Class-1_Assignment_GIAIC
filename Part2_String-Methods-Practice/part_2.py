# ** 1. Full name manipulation**

full_name = "Fiza Awan"
print(full_name.upper())  # Uppercase
print(full_name.lower())  # Lowercase
print(full_name.title())  # Capitalize first letters


# ** 2. Messy text cleanup**

messy_text = "  Python programming is fun!  "
clean_text = messy_text.strip()
updated_text = clean_text.replace("fun", "amazing")
count_i = clean_text.count("i")

print(clean_text)
print(updated_text)
print("Count of 'i':", count_i)


# ** 3. Sentence manipulation**

sentence = "The quick brown fox jumps over the lazy dog"
words_list = sentence.split()
joined_sentence = "-".join(words_list)
is_starting_with_the = sentence.startswith("The")
fox_position = sentence.find("fox")

print(words_list)
print(joined_sentence)
print("Starts with 'The':", is_starting_with_the)
print("Position of 'fox':", fox_position)

