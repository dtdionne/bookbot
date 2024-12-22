# define functions - DD
def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents
    
def word_count(main):
    cnt = 0
    words = main().split()
    for i in words:
        cnt +=1
    #print(f"This book has {cnt} words")
    return cnt
    
def lower(main):
    #print("converting all uppercase letters to lowercase...")
    lowered_string = main().lower()
    return lowered_string

def letter_count(lower):
    dict1 = {}
    itter = lower(main)
    tally = 1
    #print("processing book and skipping non-letters...")
    for i in itter:
        if i.isalpha():
            #print("isAlpha")
            if i in dict1:
                tally = dict1[i]
                tally +=1
                dict1[i] = tally
            else:
                dict1[i] = tally
    #print("and done!")
    #print(dict1)
    return dict1

def output(letter_count):
    dict2 = letter_count(lower)
    count = 0
    #print(count)
    for i in dict2:
        count = dict2[i]
        print(f"The '{i}' character was found {count} times.")

# entry point
main()
word_count(main)
letter_count(lower)
print("--- Begin report of books/frankenstein.txt ---")
print(f"{word_count(main)} words found in the document")
print("")
output(letter_count)
print("--- end report ---")