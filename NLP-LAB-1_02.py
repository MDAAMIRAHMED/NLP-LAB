punctuations = '''!@#$%^&*()-_{}[];:'"/?<>,.~'''
my_str = "Hi, I am 'chat-gpt'"
no_punct = ""

for char in my_str:
    if char not in punctuations:
        no_punct = no_punct + char
print(no_punct)
print(no_punct.split())
