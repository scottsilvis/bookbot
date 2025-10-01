
from stats import count_words
from stats import char_count
from stats import sort_out
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    local_path = sys.argv[1]
    text = get_book_text(local_path)
    count = char_count(text)
    num_words = count_words(text)
    sorted_list = sort_out(count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {local_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in sorted_list:
        if i["char"].isalpha():
            print(f'{i["char"]}: {i["num"]}')
    print("============= END ===============")

main()