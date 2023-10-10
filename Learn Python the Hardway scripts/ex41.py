import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

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

#Do they want to drill the phrases first ?
if len(sys.argv) == 2 and sys.argv[1] == "englsish":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

#load up the words from the website
for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word.strip(), encoding = "utf-8"))  

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

    return results

#keep going until they
try:
    while True:
        snippets = list(PHRASES.keys())
        random.shuffle(snippets)    

        for snippet in snippets:
            phrase = PHRASES[snippet] 
            question, answer = convert(snippet, phrase)   
            if PHRASE_FIRST:
                question, answer = answer, question

            print(question)
            input("> ")
            print(f"ANSWER: {answer}\n\n")

except EOFError:  
    print("\nBye")                       