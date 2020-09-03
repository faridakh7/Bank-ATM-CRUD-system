import json
from closeApp import *
def getDataFormJsonFile(_fileName):
    with open(_fileName, "r") as connect:
        return json.load(connect)


data = getDataFormJsonFile("db.json")


def getProductbyName():
    hesabNomresi = int(input("\nHesab nomresin daxil edin:  "))
    finder = False
    for db in data['userList']:
        if db['Hesab nomresi'] == hesabNomresi:
            def onlyUser():
                xususiEmr = input("""
                Aşağıdakı Əmrlərdən Birini Secin:
                1.Balance
                2.Pul çəkmək
                3.Depozit Qoymaq
                4.Geri qayitmaq

                    Seciminizi Daxil edin:  """).strip()
                if xususiEmr.isnumeric() and 0 < int(xususiEmr) < 5:
                    option = int(xususiEmr)

                    if option == 1:
                        print(
                            f"\n* Hesab nomresi: {db['Hesab nomresi']}\n* Ad: {db['Ad']}\n* Soyad: {db['Soyad']}\n* Balans: {db['Depozit']} AZN ")
                        onlyUser()
                    if option == 2:
                        def drawMoneys():
                            drawMoney = int(input("Cəkmək istədiyiniz miqdari daxil edin: "))
                            if db['Depozit'] > drawMoney:
                                db['Depozit'] = db['Depozit'] - drawMoney
                                print(f"Hesabinizdan {drawMoney}AZN deyerinde mebleg cixildi!")

                            else:
                                print("Balansinizda kifayet qeder mebleg yoxdur")
                                drawMoneys()

                            with open("db.json", mode="w") as connect:
                                json.dump(data, connect)

                        def back():
                            lastEmr = input("""
                                                          1.Geri Qayitmaq
                                                          2.Əsas Menuya Qayıtmaq
                                                          3.Programdan cıxmaq

                                                                  Seciminizi Daxil edin:  """).strip()
                            if lastEmr.isnumeric() and 0 < int(lastEmr) < 4:
                                options = int(lastEmr)
                                if options == 1:
                                    onlyUser()
                                if options == 2:
                                    from main import start
                                    start()
                                if options == 3:
                                    programbitdi()
                            else:
                                print("Yalnız 1-3  arası bir secim edə bilərsiniz!")
                                back()

                        drawMoneys()
                        back()

                    if option == 3:
                        def toDepositeMoney():
                            pushMoney = int(input("Depozit qoymaq istədiyiniz məbləgi daxil edin: "))
                            db['Depozit'] = db['Depozit'] + pushMoney
                            print(f"Hesabınıza {pushMoney}AZN əlavə edildi!")
                            print(f"Balans {db['Depozit']}")

                            with open("db.json", mode="w") as connect:
                                json.dump(data, connect)

                        def back():
                            lastEmr = input("""
                                   1.Geri Qayitmaq
                                   2.Əsas Menuya Qayıtmaq
                                   3.Programdan cıxmaq

                                           Seciminizi Daxil edin:  """).strip()
                            if lastEmr.isnumeric() and 0 < int(lastEmr) < 4:
                                options = int(lastEmr)
                                if options == 1:
                                    onlyUser()
                                if options == 2:
                                    from main import start
                                    start()
                                if options == 3:
                                    programbitdi()
                            else:
                                print("Yalnız 1-3  arası bir secim edə bilərsiniz!")
                                back()
                        toDepositeMoney()
                        back()

                    if option == 4:
                        from main import start
                        start()
                else:
                    print("Yalnız 1-4  arası bir secim edə bilərsiniz!")
                    onlyUser()

            onlyUser()

            finder = True
            break
    if finder == False:
        print(f"{hesabNomresi} -axtarişina uygun nəticə tapılmadı")
        getProductbyName()
