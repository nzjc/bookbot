## Book Bot 
import sys

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    print("Begin report of books/frankenstein.txt...")
    print("------------------------------------------------")
    print(f"This thing has {countWords(file_contents)} words in it.. Wow!")
    print("Here are the letters and symbols used in the book in order.. neat!")
    for k,v  in countLetters(file_contents).items():
        print(f"The letter {k} appears {v} number of times!")

def countWords(string):
    words = string.split()
    return len(words)

def countLetters(string):
    string = string.lower()
    result = {}
    for char in string:
        if char.isalpha():
            if char not in result:
                result[char] = 1
            else:
                result[char] +=1 
    return result

if __name__ == '__main__':
    sys.exit(main()) 