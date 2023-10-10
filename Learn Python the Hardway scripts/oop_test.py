#imports the necssary modules 
#random for generatting random values,
import random
#urlopen rom urllib.request for opening URLS 
from urllib.request import urlopen
#sys for interacting with the python interpreter.
import sys

#this defines the URL to be open which the words would load from
WORD_URL = "http://learncodethehardway.org/words.txt"
#an empty list to store those words
WORDS = []

#defines a dictionary where keys are the placeholders for the code snippets and values are the code snippets descriptions
PHRASES = {
    "Class %%%(%%%)": #key 1
    "Make class %%% that is a %%%.",
    "Class %%%(object):\n\tdef__init__(self, ***)": #key2 
    "Class %%% is an object and has a function init which takes parameters self and ***",
    "Class%%%(object):\n\tdef ***(self, @@@)": #Key 3
    "Class %%% is an object which takes has a function *** that takes paramters self and @@@",
    "*** = %%%()": #Key 4
    "Set *** to be an instance of class %%%",
    "***.***(@@@)":#Key 5
    "from *** get function *** with parameters @@@",
    "***.*** ='***'" : #key 6
    "from *** get the attribut *** and assign it to variable ***"
}

#Checks if the script is run with the argument "english"
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

#load up the words from the website
#fetch words from the given URL and populating the WORDS list 
for word in urlopen(WORD_URL).readlines():
    #strips the whitespaces and convert the strings with UTF-8 encoding
    WORDS.append(str(word.strip(), encoding = "utf-8"))  

#defining a function 'convert' that takes a code snippet and its description, then converts them into a question and answer.
def convert(snippet, phrase):
    class_names = [w.capitalize() for w in 
                    random.sample(WORDS, snippet.count("%%%"))]  
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1,3)
        param_names.append(', '.join(
            random.sample(WORDS, param_count)))

    for sentence in snippet, phrase:
        #this is how you duplicate a list or string
        result = sentence[:]     

        #fake class names
        for word in class_names:
            result = result.replace("%%%", word, 1)

        #fake other names
        for word in other_names:
            result = result.replace("***", word, 1)

        #fake paramters lists
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)    

    return results

#keep going until they
try:
#runs a loop indefinitely for each snippet, converting it into a question and an answer using the convert function
# if 'PHRASE_FIRST' is true, swapping the question and answer
#printing the question, waiting for user input, and then printing the answer    
    while True:
        snippets = list(PHRASES.keys())
        random.shuffle(snippets)    

        for snippet in snippets:
            phrase = PHRASES[snippet] 
            question, answer = convert (snippet, phrase)   
            if PHRASE_FIRST:
                question, answer = answer, question

            print(question)

            input("> ")
            print(f"ANSWER: {answer}\n\n")

#Handling the end-of-file error (Usually triggered by pressing Ctrl-D and printing a goodbye message)
except EOFError:  
    print("\nBye")                       





#class attributes are class variables that are inherited by every object of a class. The value of class attrributes remain the same for every new object defined outside the __init__ function.

#instance attributes are defined by the init()    