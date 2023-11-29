import csv



with open("favorites.csv", "r") as file:
    reader = csv.DictReader(file)
    counts = {}
    for row in reader:
        favorite = row["language"]
        if favorite in counts:
            counts[favorite] += 1
        else:
            counts[favorite] = 1

def get_value(language):
    return counts[language]
#lambda parameter: return value
for key, value in sorted(counts.items(), key=lambda language: counts[language], reverse=True):
    print(f"{key}: {value}")
