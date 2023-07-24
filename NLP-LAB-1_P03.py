import re
pattern = ':'
text = "This:is:chatgpt"
for word in text:
    match = re.search(pattern, text)

print(text.split())