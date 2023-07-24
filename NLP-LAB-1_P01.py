import re
pattern = "[^abc]"
text = "def"
match = re.search(pattern, text)
if match is not None:
    print("matched")
else:
    print("Not matched")