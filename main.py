import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


from stats import count_words, char_frequency, sorted_list

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def main():
    path = sys.argv[1]  # relative path
    text = get_book_text(path)
    word_count = count_words(text)  # Capture the return value
    char_counts = char_frequency(text)
    sorted_chars = sorted_list(char_counts)  # Call the function with the char_counts
    
    # Now print the report in the required format
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    # Print each character and its count
    for char_dict in sorted_chars:
        if char_dict["char"].isalpha():  # Only print alphabetic characters
            print(f"{char_dict['char']}: {char_dict['num']}")
    
    print("============= END ===============")
    
main()