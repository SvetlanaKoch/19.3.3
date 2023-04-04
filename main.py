import requests
import json

import v2 as v2

#Создаю питомца

new_pet = {
"id": 2225865,
"category": {"id": 2,"name": "Cat"},
"name": "Lama",
"photoUrls": ["string"],
"tags": [{"id": 0,"name": "string"}],
"status": "available"
}
res = requests.post(f"https://petstore.swagger.io/v2/pet",
                                  headers = {'accept': 'application/json', 'Content-Type': 'application/json'},
                                  data = json.dumps(new_pet, ensure_ascii=False))
print(res.status_code)
print(res.text)
print(res.json())

#Получаю данные по id

pet_id = 2225865

res = requests.get(f'https://petstore.swagger.io/v2/pet/{pet_id}', headers = {'accept': 'application/json'} )

print(res.status_code)
print(res.text)
print(res.json())

#Изменяю данные

update_pet = {
"id": 2225865,
"category": {"id": 2,"name": "Dog"},
"name": "Bob",
"photoUrls": ["string"],
"tags": [{"id": 0,"name": "string"}],
"status": "available"
}

res = requests.put('https://petstore.swagger.io/v2/pet', headers = {'accept': 'application/json', 'Content-Type': 'application/json'},
                                  data = json.dumps(update_pet, ensure_ascii=False))

print(res.status_code)
print(res.text)
print(res.json())

#Удаляю

pet_id_delete = 2225865

res = requests.delete(f'https://petstore.swagger.io/v2/pet/{pet_id_delete}', headers = {'accept': 'application/json'})
print(res.status_code)
print(res.text)
print(res.json())