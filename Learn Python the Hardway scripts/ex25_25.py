#this defines a function called break_words which takes a single argument
def break_words(stuff):
#this takes the argument given and splits the words in the sentence using the split method which splits a string a string into a list.   
    words = stuff.split(' ')
#this returns the result of the splitted sentence so it occurs whenever the function is called.    
    return words

#this defines a function which is called sort_words and takes a single argument
def sort_words(words):
#uses the sorted function make a sorted list  and then returns that sorted list to the function  
    return sorted(words)

#this defines the function print_first_words and gives it a single argument
def print_first_words(words):
#uses the an inbuilt py function pop to remove a specified part of the sentence given and stores it in a variable left of the = sign, in this case the given position is 0: which is the first object
    word = words.pop(0)
#this prints the word which was removed    
    print(word)

#this defines a function and names it print_last_word and also passes a single argument
def print_last_word(words):
#this uses the inbuilt py function pop to remove a specified part of the sentence given stores it in the variable left of the = sign, in this case the given position is -1: which is the last object   
    word = words.pop(-1)
#this prints out the word which was removed    
    print(word)

#this defines the function sort_sentence and passes a single argument to iy
def sort_sentence(sentence):
#this line uses our first function break_words which our sentence would be passed to as argument and will be splitted into various parts it's then stored in the variable left of the = sign  
    words = break_words(sentence)
#this calls a function we made before sort_words which sorts the words in our sentence the sort_words function in this case takes our words variable which was worked upon as it's content is words broken from the sentence the function now sorts the words which where broken and returns the result whenever the function is called.    
    return sort_words(words)

#this calls a function print_first_and_last and passes a single argument to it
def print_first_and_last(sentence):
#this uses a previously made funtion which breaks the words in our sentence into section and assigns it to a variable left of the = sign
    words = break_words(sentence)
#this uses a function made previously which prints the first word in a sentence, the temporary word variable which has been broken with the break word function is the content of the word variable which is then passed as argument, so this prints the first of the broken words  
    print_first_words(words)
#this uses a function made previously which prints the last word in a sentence, the temporary word variable which has been broken with the break word function is the content of the word variable which is then passed as argument, so this prints the last of the broken words  
    print_last_word(words)
#in all the above function(def print_first_and_last) prints the first and last of the broken functions    


#this calls a function print_first_and_last_sorted and passes a single argument to it
def print_first_and_last_sorted(sentence):
#this calls a previous function which we made called sort_sentence which breaks the sentence given to it and sorts it the argument passed undergos the same and it is then passed from the argument to the variable 
    words = sort_sentence(sentence)
#this prints the first words which have been broken and sorted    
    print_first_words(words)
#this prints the last word which was been broken and sorted.    
    print_last_word(words)    

