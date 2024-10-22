import collections

def main():
    path = 'books/frankenstein.txt'
    with open(path) as f:
        text = f.read()
        words = text.split()
        print(f"Number of words in the text: {len(words)}")

def counting_words():
    path = 'books/frankenstein.txt'
    with open(path) as f:
        text = f.read()
        words = text.split()
        lower_words = [word.lower() for word in words]
        word_count = collections.Counter(lower_words)
        return word_count['frankenstein']

def counting_letters():
    path = 'books/frankenstein.txt'
    with open(path) as f:
        text = f.read()
        lower_text = text.lower()
        letter_count = collections.Counter(c for c in lower_text if c.isalpha())
        return letter_count

if __name__ == "__main__":
    print("--- Begin report of books/frankenstein.txt ---")
    main()
    print(f"Occurrences of 'frankenstein': {counting_words()}")
    letter_counts = counting_letters()
    letter_counts_list = [(letter, count) for letter, count in letter_counts.items()]
    for letter, count in sorted(letter_counts_list):
        print(f"The {letter} character was found: {count} times")

print("--- End report ---")
    