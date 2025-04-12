from stats import count_words
from stats import count_characters
from stats import sort_character_counts
import sys

def get_books_text(filepath):
    with open(filepath) as f:
      return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_books_text(book_path)

    num_words = count_words(text)
    num_chars = count_characters(text)
    sort_chars = sort_character_counts(num_chars)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for entry in sort_chars:
        char = entry['char']
        count = entry['count']
        if char.isprintable() and not char.isspace():
            print(f"{char}: {count}")

    print("============= END ===============")

main()