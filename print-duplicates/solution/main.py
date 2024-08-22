names = ["Morten", "Jensine", "Preben", "Ulla", "Ulla", "Jensine", "Børge"]

duplicates = []

for name in names:
    if names.count(name) > 1:
        if name not in duplicates:
            duplicates.append(name)

print(duplicates)
