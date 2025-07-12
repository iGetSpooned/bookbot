import sys

def get_num_words(text):
    words = text.split()
    return len(words)
# counts the number of words in a given text

def number_of_characters(text):
    char_count = {}
    for char in text.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count
# counts the number of characters in a given text   

def char_count_list(char_count):
    char_list = [{"char": char, "num": count} for char, count in char_count.items()]
    char_list.sort(key=lambda d: d["num"], reverse=True)
    return char_list
# converts the character count dictionary to a list of dictionaries with sorted counts

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    filepath = sys.argv[1]

