import sys

from stats import get_num_words
from stats import times_each_char
from stats import sort_results


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[1]
    text = get_book_text(book)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}")
    print("----------- Word Count ----------")
    print(get_num_words(text))
    print("--------- Character Count -------")
    output = sort_results(times_each_char(text))
    for key, value in output:
        print(f"{key}: {value}")
    print("============= END ===============")


main()
