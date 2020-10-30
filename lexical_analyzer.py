import re
from hash_table import HashTable
from PIF import PIF

pif = PIF()
st = HashTable()

reserved_words =[]
input_file = "p1err.txt"

allowed_characters ="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"

with open("token.in.txt", "r") as file:
    read_tokens = [x for x in file.read().split("\n") if len(x) != 0]
    for tok in read_tokens:
        reserved_words.append(tok)

def isConstant(token):
    try:
        int(token)
        return True

    except ValueError:
        return False



def isIdentifier(token):
    for char in token:
        if char not in allowed_characters:
            return False
    return re.match("^[0-9\"']", token) is None or re.match('^"[a-zA-Z0-9]+"', token) is not None or re.match("^'[a-zA-Z0-9]'", token) is not None


with open(input_file, "r") as file:
     line_nr = 1
     line = file.readline()
     while line:
         groupOfWords = re.split('([^"\'a-zA-Z0-9])', line)
         words = list(filter(lambda x: x is not None and x != '', map(lambda x: x.strip(), groupOfWords)))

         for word in words:
             if word in reserved_words:
                 pif[word] = -1
             elif isConstant(word):
                 position = st.add(word)
                 pif[word] = position
             elif isIdentifier(word):
                 position=st.add(word)
                 pif[word] = position
             else:
                 raise Exception("Lexical error. Invalid " + word + " on line "+ str(line_nr))
         line = file.readline()
         line_nr += 1

     print(st, "\n")
     print(pif)

     print("The program is lexically correct!")

