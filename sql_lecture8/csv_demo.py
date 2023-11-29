import csv

with open("favorites.csv", "r") as file:
    #csv.reader splits(",") -> list["string"]
    reader = csv.reader(file)
    for row in reader:
        favorite_language = row[1]
        print(favorite_language)
        