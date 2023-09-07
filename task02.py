import re

string = "Hello123 and goodbye03 gl0123"

print(re.findall("\d{1,3}", string))