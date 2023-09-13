import sys
script, input_encoding, error = sys.argv

def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)

def print_line(line, encoding, errors):
    raw_bytes = line
    cooked_bytes = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_bytes)

languages = open("languages.txt", 'rb')  # Open the file in binary mode ('rb')

main(languages, input_encoding, error)
