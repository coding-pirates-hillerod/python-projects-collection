def is_palindrome(s):
    return s == s[::-1]


# Input string
string = input("Indtast en tekst: ")

# Check palindrome
if is_palindrome(string):
    print(f"{string} er et palindrom.")
else:
    print(f"{string} er ikke et palindrom.")
