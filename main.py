def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_letters = get_num_char(text)
    report_data = dict_report(num_letters)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    print()
    for dict in report_data:
        print(f"The '{dict['letter']}' character was found {dict['num']} times")
    print("--- End report ---")
    


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_num_char(text):
    dict_letters = {}
    for letter in text.lower():
        if not letter in dict_letters:
            dict_letters[letter] = 1
        else:
            dict_letters[letter] += 1
    
    return dict_letters

def sort_on(dict):
    return dict["num"]

def dict_report(dict_letters):
    
    list_alpha_letters = []
    for char in dict_letters:
        if char.isalpha():
            #dict_alpha_letters = {}
            #dict_alpha_letters["letter"] = char
            #dict_alpha_letters["num"] = int(dict_letters[char])
            #list_alpha_letters.append(dict_alpha_letters)
            list_alpha_letters.append({"letter": char, "num": dict_letters[char]})
    #print(list_alpha_letters)
    list_alpha_letters.sort(reverse = True, key = sort_on)

    return list_alpha_letters


    

            

main()