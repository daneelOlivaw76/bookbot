def count_chars(text):
    char_count = {}
    for c in text:
        low = c.lower()
        if low in char_count:
            char_count[low] += 1
        else:
            char_count[low] = 1
    return char_count

def count_words(text):
    words = text.split()
    return len(words)