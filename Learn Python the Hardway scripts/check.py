import random
from urllib.request import urlopen
import sys
WORD_URL = "http://learncodethehardway.org/words.txt"  
WORDS = []
PHRASES = {
    "class %%%(%%%):":
    "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)" :
    "class %%% has-a __init__ that takes self and *** params.",
    "class %%%(object):\n\tdef ***(self, @@@)":
    "class %%% has-a function *** that takes self and @@@ params.",
    "*** = %%%()":
    "Set *** to an instance of class %%%.",
    "***.***(@@@)":
    "From *** get the *** function, call it with params self, @@@.",
    "***.*** = '***'":
    "From *** get the *** attribute and set it to '***'."
    }

# do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

# load up the words from the website
for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word.strip(), encoding="utf-8"))

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
# this is how you duplicate a list or string
48 result = sentence[:]
49
50 # fake class names
51 for word in class_names:
52 result = result.replace("%%%", word, 1)
53
54 # fake other names
55 for word in other_names:
56 result = result.replace("***", word, 1)
57
58 # fake parameter lists
 for word in param_names:
 result = result.replace("@@@", word, 1)

62 results.append(result)
63
64 return results
65
66
67 # keep going until they hit CTRL-D
68 try:
69 while True:
70 snippets = list(PHRASES.keys())
71 random.shuffle(snippets)
72
73 for snippet in snippets:
74 phrase = PHRASES[snippet]
75 question, answer = convert(snippet, phrase)
76 if PHRASE_FIRST:
77 question, answer = answer, question
78
79 print(question)