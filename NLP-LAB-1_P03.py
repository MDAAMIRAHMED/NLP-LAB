import re
pattern = '[abc]'
text = "This:is:chatgpt"
result = re.split(pattern, text)
print(result)