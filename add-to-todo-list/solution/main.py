todo_list = []

answer = input("Hvad vil du tiljøje din 'todo liste'? (indtast 'q' for at afslutt) ")

while answer != "q":
    todo_list.append(answer)
    answer = input(
        "Hvad vil du tiljøje din 'todo liste'? (indtast 'q' for at afslutt) "
    )

if todo_list:
    print("Her er din 'todo liste':")
    for item in todo_list:
        print("- " + item)
else:
    print("Du har ikke tilføjet nogle elementer til din 'todo liste' endnu.")
