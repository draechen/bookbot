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

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        wordcount = count_words(file_contents)
        file_char_count = count_char(file_contents)
        print(" --- Begin report of books/frankenstein.txt ---")
        print(f"{wordcount} words found in the document")
        for key, value in file_char_count.items():
            if key.isalpha():
                print(f"The '{key}' character was found {value} times")    
    return

main()