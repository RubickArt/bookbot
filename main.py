def main():
    
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_dict = get_char_dict(text)
    char_list = dict_to_list(char_dict)

    # print(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")

    for item in char_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item["char"]}' character was found {item["num"]} times")
    print("--- End report ---")

    
def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_num_words(book):
    words = book.split()
    return len(words)

def get_char_dict(book):
    char_dict = {}
    lowered_book = book.lower()
    for word in lowered_book:
        for char in word:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    return char_dict


def sort_on(dict):
    return dict["num"]

def dict_to_list(dict):
    char_list = []
    for char in dict:
        char_list.append({"char": char, "num": dict[char]})
    char_list.sort(reverse=True, key=sort_on)
    return char_list



main()