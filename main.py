import string


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    #word_wount = count_words(text)
    char_count = count_chars(text)
    #print(char_count)
    print_report(book_path, char_count)

def count_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read() 
    
def count_chars(text):
    char_count = {}
    for c in text:
        low = c.lower()
        if low in char_count:
            char_count[low] += 1
        else:
            char_count[low] = 1
    return char_count

def print_report(book_path, char_count):
    print(f"--- Begin report of {book_path} ---")
    for item in char_count:
        print(f"The {repr(item)} character was found {char_count[item]} times.")

    print(f"--- End report ---")

main()