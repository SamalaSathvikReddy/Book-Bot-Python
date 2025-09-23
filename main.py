import sys
import stats

def get_book_text(path):
    with open(path, "r") as f:
        file_contents = f.read()
    return file_contents


def get_stats(path):
    main_text = get_book_text(path)
    print("============ BOOKBOT ============") 
    print(f"Analyzing the book found at {path}....")
    word_count = stats.get_num_words(main_text)
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    freq = stats.char_count(main_text)
    print("--------- Character Count -------") 
    
    for i in freq:
        if i[0].isalpha() == True: 
            print(f"{i[0]} : {i[1]}")
    print("============= END ===============")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    get_stats(sys.argv[1])     
    
main()


