
def remove_punctuation(text):
    return text.translate(str.maketrans('', '', string.punctuation))

def convert_to_lowercase(text):
    return text.lower()

def split_text(text):
    return text.split()

def find_palindromes(word_list):
    return [word for word in word_list if word == word[::-1]]

def word_frequencies(word_list):
    return {word: word_list.count(word) for word in set(word_list)}

# Combined One-Liner for Processing
input_text = "Madam Arora teaches malayalam. She also teaches civic concepts. Madam is great!"
word_list = split_text(convert_to_lowercase(remove_punctuation(input_text)))
palindromes = find_palindromes(word_list)
frequencies = {word: word_list.count(word) for word in set(word_list)}

# Print Results
print("Palindromes:", palindromes)
print("Word Frequencies:", frequencies)
