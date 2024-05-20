def convert_to_lowercase(text):
    lowercase_text = text.lower()
    return lowercase_text

def split_text(text):
    word_list = text.split()
    return word_list

def count_words(word_list):
    word_count = len(word_list)
    return word_count

def remove_duplicates(word_list):
    unique_words = list(set(word_list))
    return unique_words

input_text = "This is An Example TEXT with some duplicate words this This."
lowercase_text = convert_to_lowercase(input_text)
word_list = split_text(lowercase_text)
num_words = count_words(word_list)
unique_words = remove_duplicates(word_list)
print("Unique words:", unique_words)