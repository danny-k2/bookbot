import sys

from stats import word_count

from stats import character_count

from stats import character_sort

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[1]
    text = get_book_text(book)
    total_words = word_count(text)
    total_characters = character_count(text)
    sorted_characters = character_sort(total_characters)
    print_report(book, total_words, sorted_characters)

def get_book_text(file_to_path):
    with open(file_to_path) as f:
        data = f.read()
    return data


def print_report(book, total_words, sorted_characters):
    print("============BOOKBOT============")
    print(f"Analyzing book found at {book}...")
    print('----------- Word Count----------')
    print(f"Found {total_words} total words")
    print('--------- Character Count -------')
    for item in sorted_characters:
        if not item['character'].isalpha():
            continue
        print(f"{item['character']}: {item['num']}") 

    print("============= END ===============")

main()
