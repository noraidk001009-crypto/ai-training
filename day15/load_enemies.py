import json

with open("assignment/enemies.json", "r", encoding="utf-8") as file:
    enemies = json.load(file) #python can understand the data

for enemy in enemies:  #list
    print(enemy["name"], "HP", enemy["hp"], "ATK", enemy["atk"])#print the data


#utf-8是一个解码工具