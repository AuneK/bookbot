book = "books/frankenstein"

def word_count(s):
    words = s.split()
    return len(words)

def letter_count(s):
    letters = {}
    lowered_string = s.lower()
    for char in lowered_string:
        try:
            letters[char] +=1
        except:
            letters[char] = 1
    return letters
def sort_on(dict):
    return dict[1]
def report(s):
    print (f"--- Begin report of {book} ---")
    print (f"{word_count(s)} words found in the document")
    print ("")
    l= list(letter_count(s).items())
    l.sort(reverse=True, key=sort_on)
    for i in l:
        if (i[0].isalpha()):
            print (f"The '{i[0]}' character was found {i[1]} times")
    

    print ("--- End report ---")
    pass
    
    


def main():
    with open (book) as f:
        file_contents = f.read()
        #print (file_contents)
        #print (word_count(file_contents))
        #print (letter_count(file_contents))
        report(file_contents)



main()