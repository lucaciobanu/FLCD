import re
from hash_table import HashTable
from PIF import PIF

pif = PIF()
st = HashTable()

reserved_words =[]
input_file = "p1.txt"

allowed_characters ="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"
allowed_string_constant_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

with open("token.in.txt", "r") as file:
    read_tokens = [x for x in file.read().split("\n") if len(x) != 0]
    for tok in read_tokens:
        reserved_words.append(tok)

def isIntConstant(token):
    try:
        int(token)
        return True

    except ValueError:
        return False

def isStringConstant(token):
    if token[0] == "\"" and token[len(token) - 1] == "\"":
        actualToken = token[-1:len(token) -1]
        for char in actualToken:
            if char not in allowed_string_constant_characters:
                return False
        return True
    return False

def isCharConstant(token):
    if token[0] == "'" and token[len(token) - 1] =="'":
        if token[1] not in allowed_string_constant_characters:
            return False
        return True
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

         i = 0
         while i < len(words) - 1:
             if words[i] == "=" and words[i+1] == "=":
                 words[i] = "=="
                 del words[i+1]
             if words[i] == "<" and words[i+1] == "=":
                 words[i] = "<="
                 del words[i+1]
             if words[i] == ">" and words[i+1] == "=":
                 words[i] = ">="
                 del words[i+1]
             if words[i] == "!" and words[i+1] == "=":
                 words[i] = "!="
                 del words[i+1]
             if words[i] == "+" and words[i+1] == "=":
                 words[i] = "+="
                 del words[i+1]
             if words[i] == "-" and words[i+1] == "=":
                 words[i] = "-="
                 del words[i+1]
             if words[i] == "&" and words[i+1] == "&":
                 words[i] = "&&"
                 del words[i+1]
             if words[i] == "|" and words[i+1] == "|":
                 words[i] = "||"
                 del words[i+1]
             if words[i] == "<" and words[i+1] == "<":
                 words[i] = "<<"
                 del words[i+1]
             if words[i] == ">" and words[i+1] == ">":
                 words[i] = ">>"
                 del words[i+1]
             if words[i] == "-" and isIntConstant(words[i+1]):
                 words[i] = "-" + words[i+1]
                 del words[i+1]

             i += 1

         for word in words:
             if word in reserved_words:
                 pif[word] = -1
             elif isIntConstant(word):
                 position = st.add(word)
                 pif[word] = position
             elif isStringConstant(word):
                 position = st.add(word)
                 pif[word] = position
             elif isCharConstant(word):
                 position = st.add(word)
                 pif[word] = position
             elif isIdentifier(word):
                 position=st.add(word)
                 pif[word] = position
             else:
                 raise Exception("Lexical error. Invalid " + word + " on line "+ str(line_nr))
         line = file.readline()
         line_nr += 1

     with open("st.out", "w") as file:
         file.write(str(st))

     with open("pif.out", "w") as file:
         file.write(str(pif))

     print("The program is lexically correct!")













