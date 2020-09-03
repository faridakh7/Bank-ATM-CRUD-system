import json

from closeApp import programbitdi


def getDataFormJsonFile(_fileName):
    with open(_fileName, "r") as connect:
        return json.load(connect)


data = getDataFormJsonFile("db.json")

print("Aşağıda Qeyd olunan Formu Doldurun\n")



def userRegister():
    hesabNomresi = int(input("Hesab Nomresini daxil edin:  "))
    # if checkExists(hesabNomresi, data['userList']):
    #     # var
    # else:
    #     #yoxdu
    for db in data['userList']:
        if db['Hesab nomresi'] != hesabNomresi:
            if hesabNomresi > 99 and hesabNomresi < 999:

                regName = input("Adınız:  ")
                regSurname = input("Soyadınız:  ")
                regDepozit = int(input("Qoymaq istədiyiniz Depozit:  "))

                userList = {
                    "Hesab nomresi": hesabNomresi,
                    "Ad": regName,
                    "Soyad": regSurname,
                    "Depozit": regDepozit
                }

                data['userList'].append(userList)
                with open("db.json", mode="w") as connect:
                    json.dump(data, connect)
                print("\n* * * Müvəffəqiyyətlə qeydiyyatdan keçdiniz * * *")
                print(
                    f"* Hesab nomresi: {hesabNomresi}\n* Ad: {regName}\n* Soyad: {regSurname}\n* Balans: {regDepozit}AZN")

                def back():
                    lastEmr = input("""                         
                                     1.Əsas Menuya Qayıtmaq
                                     2.Programdan cıxmaq
            
                                            Seciminizi Daxil edin:  """).strip()
                    if lastEmr.isnumeric() and 0 < int(lastEmr) < 4:
                        options = int(lastEmr)

                        if options == 1:
                            from main import start
                            start()
                        if options == 2:
                            programbitdi()
                    else:
                        print("Yalnız 1-3  arası bir secim edə bilərsiniz!")
                        back()

                back()
            else:
                print("100-999 Arası bir Hesab Nömrəsi əlavə edin")
                userRegister()
        else:
            print("EYNIDIRRR!!!!")


userRegister()
