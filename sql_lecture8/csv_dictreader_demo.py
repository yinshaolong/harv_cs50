import csv

with open("favorites.csv", "r") as file:
    reader = csv.DictReader(file)
    categories = {}
    for row in reader:
        favorite = row["language"]
        if favorite in categories:
            categories[favorite] += 1
        else:
            categories[favorite] = 1
            
    for key, value in categories.items():
        print(f"{key}: {value}")
