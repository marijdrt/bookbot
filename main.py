import sys
from stats import (
  get_num_words,
  get_chars_count,
  sort_chars_count
)


def main():
  if not len(sys.argv) == 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  else:
    book_path = sys.argv[1]
    book_contents = get_book_text(book_path)
    num_words = get_num_words(book_contents)
    chars_count = get_chars_count(book_contents)
    chars_count_report = ''
    for item in sort_chars_count(chars_count):
      if not item["char"].isalpha():
        continue
      chars_count_report += f"{item["char"]}: {item["count"]}\n"
    print_report(book_path, num_words, chars_count_report)


def get_book_text(filepath):
  with open(filepath) as f:
    return f.read()


def print_report(book_path, num_words, chars_count_report):
  print(f"============ BOOKBOT ============\nAnalyzing book found at {book_path}...\n----------- Word Count ----------\nFound {num_words} total words\n--------- Character Count -------\n{chars_count_report}============= END ===============")

main()