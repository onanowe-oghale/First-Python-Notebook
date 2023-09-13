import sys

script , IO_file, error = sys.argv

def main (languages_IO ,encoded , errorz):
    line = languages_IO.readline()

    if line:
        print_line(line , encoded , errorz)
        return main (languages_IO , encoded , errorz)

def print_line(line, encoded, errorz):
    lang_io = line.strip()
    raw_bytes = lang_io.encode(encoded , errorz)
    de_string = raw_bytes.decode(encoded , errorz)
    print(raw_bytes , "<===>",de_string )

language = open("languages.txt", encoding= "utf-8") 

main(language , IO_file , error)
