# dictionary pake {} ngaksesnya pake []
# refer dictionary pake key nya alias text, kalo list kan pake angka

users = {
    "id": 1,
    "name": "Leanne Graham",
    "username": "Bret",
    "email": "Sincere@april.biz",
    "address": {
        "street": "Kulas Light",
        "suite": "Apt. 556",
        "city": "Gwenborough",
        "zipcode": "92998-3874",
        "geo": {
              "lat": "-37.3159",
              "lng": "81.1496"
            }
        }
} # key json harus text gabisa angka

print(users)
print(users["id"])
print(users["name"])
print(users["username"])
print(users["email"])
print(users["address"])
print(users["address"]["street"])
print(users["address"]["geo"])
print(users["address"]["geo"]["lat"])
print(users["address"]["geo"]["lng"])

print(users)
print(type(users))
print('\nUbah dict ke json')
import json
result = json.dumps(users)
print(result)
print(type(result)) # str = string

with open('result.json', 'w') as file:
    json.dump(users, file)
