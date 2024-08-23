# Funktion til at tjekke for palindrom
def is_palindrome(s):
    return s == s[::-1]


# Få input fra brugeren
string = input("Indtast en tekst: ")

# Check palindrom
if is_palindrome(string):
    print(f"{string} er et palindrom.")
else:
    print(f"{string} er ikke et palindrom.")
