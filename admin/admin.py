import json
from closeApp import *

def getDataFormJsonFile(_fileName):
    with open(_fileName, "r") as connect:
        return json.load(connect)


data = getDataFormJsonFile("db.json")


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
            print("Bitdi")
            return
    else:
        print("Yalnız 1-3  arası bir secim edə bilərsiniz!")
        back()

def control():
    username = input("Username: ").lower()
    password = input("Password: ").lower()

    if username == "admin":
        if password == "admin":
            def success():
                global back
                firstCommand = input("""
                Aşağıdakı Əmrlərdən Birini Secin:
                1.Müştərilərin hesabları görmək
                2.Müştərinin qeydiyyatlını ləğv etmək
                3.Geri qayıtmaq
                4.Çıxış

                         Seciminizi Daxil edin:  """).strip()
                if firstCommand.isnumeric() and 0 < int(firstCommand) < 5:
                    option = int(firstCommand)
                    if option == 1:
                        for db in data['userList']:
                            print(
                                f"* Hesab nomresi: {db['Hesab nomresi']} *  Ad: {db['Ad']}  * Soyad: {db['Soyad']} * Balans: {db['Depozit']}AZN")
                        back()
                    if option == 2:
                        finder=False
                        idnumb = int(input("Silmək istədiyiniz müştərinin hesab nömrəsini daxil edin:  "))
                        for db in data['userList']:
                            if db['Hesab nomresi'] == idnumb:
                                data['userList'].pop(data['userList'].index(db))
                                finder=True
                                print(f"{idnumb} -Nömrəli ID databaseden silindi")
                                back()
                                break
                        with open("db.json", "w") as connect:
                            json.dump(data, connect)
                        if finder==False:
                            print(f"{idnumb} -Hesab Nömrəli müştəri tapılmadi")
                            back()

                    if option == 3:
                        from main import start
                        start()
                    if option == 4:
                        from closeApp import programbitdi
                        programbitdi()

                else:
                    print("Yalnız 1-4  arası bir secim edə bilərsiniz!")
                    success()

            success()

        else:
            print("Password Sehvdir")
            control()
    else:
        print("Username Sehvdir")
        control()
