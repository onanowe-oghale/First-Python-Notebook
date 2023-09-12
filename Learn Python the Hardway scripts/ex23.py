#Strings, Bytes and Characer Encodings

#This imports the full system module from the python library
import sys

#this names the variables on the left which unpacks command-line argumrnts passed to the script, and assigns the lists argv from the sys module called earlier
script, input_encoding, error = sys.argv

#defines a function called main three arguments passed into it which would read the lines form the file and do the error handling.
def main(language_file, encoding , errors): 
#reads singular lines in the language_file and assigns it to the line variable    
    line = language_file.readline()
#this helps makes a decision if there is content in the line which is the file.
    if line:
#this calls the print_line function passing the line, encoding and error handling methods as arguments        
        print_line(line, encoding, errors)
#this calls the main function which reads the file line by line again and again until there is an empty string      
        return main(language_file, encoding , errors)
    
#defines a function with three arguments and the function's name is print_line. This is responsible for encoding the line and decoding it to a string and it prints the bytes and the decoded string with a separator.
def print_line(line , encoding , errors):
#removes leading and trailing whitespace from each line in the line file and assigns it a variable of next_lang    
    next_lang = line.strip()
#encodes the content of each line into bytes (DBES) and assigns it the raw_bytes   
    raw_bytes = next_lang.encode(encoding , errors=errors)
#decodes the bytes into strings DBES.......    
    cooked_string = raw_bytes.decode(encoding , errors = errors)
#this prints the encoded bytes and the decoded strings in the utf passed in the command line, the bytes on the left of the <===> while the string on the left
    print(raw_bytes, "<===>" , cooked_string) #<===> is a seperator

#opens the file to be read mode it also specifies it should be done in UTF-8 encoding and passes it into a variable called languages
languages = open("languages.txt" , encoding="utf-8")

#function main runs with three arguments the languages opening the file, the input encoding and the error handling (error) as argument
main(languages, input_encoding, error)