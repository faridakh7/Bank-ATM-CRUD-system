import json
from user.user import *


def getDataFormJsonFile(_fileName):
    with open(_fileName, "r") as connect:
        return json.load(connect)




data = getDataFormJsonFile("../db.json")

for db in data['userList']:
    if db['Hesab nomresi'] == hesabNomresi:
        def drawMoneys():
            drawMoney = int(input("Cəkmək istədiyiniz miqdari daxil edin: "))
            if db['Depozit'] > drawMoney:
                db['Depozit'] = db['Depozit'] - drawMoney
            # else:
            #     print("Balansinizda o qeder mebleg yoxdur")

with open("db.json", "w") as connect:
    json.dump(data, connect)
    print(f"Hesabinizdan XXXAZN deyerinde mebleg cixildi!")
drawMoneys()