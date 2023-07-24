import re
plural = 'fruit'
match = re.search(r's$',plural)
if match is None:
    print("Parsing is not successful and is not a plural")
else:
    print("Parsing is successful and is a plural")