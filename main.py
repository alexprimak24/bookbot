import sys
from stats import get_num_words, unique_characters_count, open_file, handle_sort_dictionary

def main():

    if(len(sys.argv) < 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path_to_file = sys.argv[1]
        file_text = open_file(path_to_file) 

        num_words = get_num_words(file_text)
        characters_count = unique_characters_count(file_text) 
        sorted_dictionary = handle_sort_dictionary(characters_count)

        print("============ BOOKBOT ============")
        print("Analyzing book found at books/frankenstein.txt...")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for entry in sorted_dictionary:
            if(entry['char'].isalpha()):
                print(f"{entry['char']}: {entry['num']}")
        print("============= END ===============")

main()