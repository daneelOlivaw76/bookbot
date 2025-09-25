import string

from stats import count_words
from stats import count_chars

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    print(f"Found {word_count} total words")
    char_count = count_chars(text)
    print(char_count)
    print_report(book_path, char_count)

def get_book_text(path):
    with open(path) as f:
        return f.read() 

def print_report(book_path, char_count):
    sorted_dict = dict(sorted(char_count.items()))
    print(f"--- Begin report of {book_path} ---")
    for item in sorted_dict:
        if(item.isalpha()):
            print(f"The {repr(item)} character was found {char_count[item]} times.")

    print(f"--- End report ---")

main()