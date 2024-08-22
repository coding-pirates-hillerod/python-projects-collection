from random import randint

min_number = 1
max_number = 10
max_guesses = 3
guesses = 0
number_not_guessed = True

number_to_guess = randint(1, 10)

print(f"Kan du gætte det rigtige tal mellem {min_number} og {max_number}?\n")

while number_not_guessed and guesses < max_guesses:
    guess = int(input("Hvad er dit gæt? "))

    if guess < number_to_guess:
        print(f"Tallet du skal gætte er højere end {guess}\n")
    elif guess > number_to_guess:
        print(f"Tallet du skal gætte er mindre end {guess}\n")
    else:
        number_not_guessed = False

    guesses += 1


if number_not_guessed:
    print(
        f"Beklager .. Du formåede desværre ikke at gætte det rigtige tal: {number_to_guess}"
    )
else:

    print(f"\nSådan! Du gættede at det rigtige tal er {number_to_guess}")
