# Verbose Version (to be made concise)

def remove_punctuation(text):
    translator = str.maketrans('', '', string.punctuation)
    result = text.translate(translator)
    return result

def convert_to_lowercase(text):
    result = text.lower()
    return result

def split_text(text):
    result = text.split()
    return result

def find_palindromes(word_list):
    palindromes = []
    for word in word_list:
        if word == word[::-1]:
            palindromes.append(word)
    return palindromes

def word_frequencies(word_list):
    frequency = {}
    for word in word_list:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency

# Input Text
input_text = "Madam Arora teaches malayalam. She also teaches civic concepts. Madam is great!"

# Processing
cleaned_text = remove_punctuation(input_text)
lowercase_text = convert_to_lowercase(cleaned_text)
word_list = split_text(lowercase_text)
palindromes = find_palindromes(word_list)
frequencies = word_frequencies(word_list)

# Print Results
print("Palindromes:", palindromes)
print("Word Frequencies:", frequencies)
