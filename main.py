from stats import get_num_words

def get_book_text(path):
    with open(path, "r") as f:
        file_contents = f.read()
    return file_contents

def main():
    main_txt = get_book_text("books/frankenstein.txt")
    print(main_txt)
    print(f"{get_num_words(main_txt)} words are there in document")
main()


