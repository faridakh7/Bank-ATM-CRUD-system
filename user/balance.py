import json


def getDataFormJsonFile(_fileName):
    with open(_fileName, "r") as connect:
        return json.load(connect)


data = getDataFormJsonFile("..db.json")


def showAllData():
    for d in data['userList']:
        print(f"Hesab nomresi:{d['Hesab nomresi']} | Ad:{d['Ad']} | Soyad:{d['Soyad']} | Balans:{d['Depozit']} ")


showAllData()
