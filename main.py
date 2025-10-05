import sys

from stats import get_num_words
from stats import get_num_unique_characters, sort_character_counts

def get_book_text(path=None):
    """Read and return the contents of the file at `path`.

    If `path` is None, use the default sample `books/frankenstein.txt`.
    """
    if not path:
        raise ValueError("path is required")
    with open(path, encoding="utf-8") as f:
        return f.read()

def main(path):
    # path: path to the book file (required)
    try:
        text = get_book_text(path)
    except FileNotFoundError:
        print(f"Error: file not found: {path}")
        return 1
    except Exception as e:
        print(f"Error reading file: {e}")
        return 1
    num_words = get_num_words(text)
    num_unique_characters, character_counts = get_num_unique_characters(text)
    sorted_report = sort_character_counts(character_counts)
    # Print the sorted report (one line per character: "char: count")
    for entry in sorted_report:
        print(f"{entry['char']}: {entry['num']}")
    print(f"Found {num_words} total words")
    return 0


if __name__ == "__main__":
    # Require exactly one argument: the path to the book file
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    sys.exit(main(book_path))
    