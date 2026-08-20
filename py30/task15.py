# Take a word as input and print it reversed (hint: use indexing/slicing).
#     Then check and print whether the word is a palindrome.

word=input("enter a word: ")
c = word[::-1]

if word == c:
    print(f"{word} is a palindrome")
else:
    print(f"{word} is not a palindrome")