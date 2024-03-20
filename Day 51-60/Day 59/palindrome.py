
print("Palindrome Checker")
word = input("Enter a word\n> ")

def palindrome(word):
    word = word.lower().replace(" ","")
    if len(word)<=1:
        return True
    if word[0] != word[-1]:
        return False
    return palindrome(word[1:-1])

print(palindrome(word))