
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    
    # print(f"word count {count}")
    # print(f"character count dict {char_count}")
    print(f"--- Begin report of books/frankenstein.txt ---")
    
    count = count_words(text)
    print(f"{count} words found in the document\n")

    char_count = count_chars(text)
    char_list = list_chars(char_count)
    char_list.sort(reverse=True, key=sort_on)
    # print(f"list of chars > {char_list}")

    for c in char_list:
        # print(f"item {c}")
        print(f"The '{c["char"]}' character was found {c["num"]} times")
    
    print(f"--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    words = text.lower()
    chars = {}
    for char in words:
        if char.isalpha():
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1
    return chars

def list_chars(dict):
    list = []
    for d in dict:
        list.append({"char": d, "num": dict[d] })
    return list

def sort_on(dict):
    return dict["num"]

main()