def break_the_words(made):
    words = made.split(' ')
    return words

def we_sorted(words):
    return sorted(words)

def print_first_man(sentence):
    words = sentence.pop(0)
    print(words)

def print_last_man(sentence):
    words = sentence.pop(-1)
    print(words)

def sort_we(sentence):
    words = break_the_words(sentence)
    words = we_sorted(words)
    return words

def print_firstandlast_man(sentence):
    words = break_the_words(sentence)
    print_first_man(words)
    print_last_man(words)        

def print_firstandlastsorted_man(sentence) :
    words = sort_we(sentence)
    print_first_man(words)
    print_last_man(words)   