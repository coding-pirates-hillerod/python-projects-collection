shopping_list = []

answer = input(
    "Hvad vil du tilføje til din shopping liste? (tryk 'q' for at afslutte): "
)

while answer != "q":
    shopping_list.append(answer)
    answer = input(
        "Hvad vil du tilføje til din shopping liste? (tryk 'q' for at afslutte): "
    )

if shopping_list:
    print("\nDin shopping liste er:")
    for item in shopping_list:
        print(item)
else:
    print("Du har ikke tilføjet noget til din shopping liste.")
