str = input()

for ch in str :
    if ch.isupper():
        print(ch.lower(),end="")
    else:
        print(ch.upper(), end="")
