def count_words(contents):
    splitcontents = contents.split()
    count = len(splitcontents)
    return count

def count_char(contents):
    set_char = set()
    countchar = {}
    for char in contents:
        lcasechar = char.lower()
        if lcasechar not in set_char:
            set_char.add(lcasechar)
            countchar[lcasechar] = 1
        else:
            countchar[lcasechar] += 1
    return countchar

def sort_on(dict):
    return dict["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def main():
    with open(path) as f:
        file_contents = f.read()
        wordcount = count_words(file_contents)
        file_char_count = count_char(file_contents)
        sorted_char_count = chars_dict_to_sorted_list(file_char_count)
        print(f"--- Begin report of {path} ---")
        print(f"{wordcount} words found in the document")
        for item in sorted_char_count:
            if item["char"].isalpha():
                print(f"The '{item["char"]}' character was found {item["num"]} times")    
    return

path = "books/frankenstein.txt"
main()