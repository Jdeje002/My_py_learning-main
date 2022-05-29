### check if a word is a palindrome

print("Check if a word is a palindrome")

imput_word = input("Enter a word: ")

def is_palindrome(word):
    if word == word[::-1]:
        print("%s is a palindrome" % word)
    else:
         print("%s is NOT a palindrome" % word)



is_palindrome(imput_word)
