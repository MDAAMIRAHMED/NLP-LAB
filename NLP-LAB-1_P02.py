import re
pattern = 'is$'
text = "This isn't chatgpt. That is chatgpt"
cnt = 0
for word in text.split():
    match = re.search(pattern, word)
    if match is not None:
        cnt = cnt + 1

print(pattern + " occurred " + str(cnt) + " times")
