import sys

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
        return contents
def main():
        book_text = get_book_text(sys.argv[1])
        words = get_num_words(book_text)
        dictionary = number_of_characters(book_text)
        sorted_dictionary = char_count_list(dictionary)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at")
        print("----------- Word Count ----------")
        print(f"Found {words} total words")
        print("--------- Character Count -------")
        for item in sorted_dictionary:
            char = item['char']
            count = item['num']
            if char.isalpha():
                print(f"{char}: {count}")
        print("============= END ===============")
from stats import get_num_words
from stats import char_count_list
from stats import number_of_characters
main()
