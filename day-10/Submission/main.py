import json

name = input("Enter your name: ")
age = input("Enter your age: ")
fav = input("Enter your favorite food: ")

user_data = {
    "Name" : name,
    "Age" : age,
    "Favorite_Food" : fav,
}

content = json.dumps(user_data, indent=2)

with open('output.json', 'w') as file:
    file.write(content)