import re

string = "Hello and goodbye03 gl"

print(re.search("\w+\d\W", string))
