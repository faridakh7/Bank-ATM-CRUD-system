import json


def getDataFormJsonFile(_fileName):
    with open(_fileName, "r") as connect:
        return json.load(connect)


data = getDataFormJsonFile("../db.json")

hesabNomresi = int(input("Hesab nomresin daxil edin:  "))
def getProductbyName():
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
                            f"\n* Hesab nomresi:{db['Hesab nomresi']}\n* Ad:{db['Ad']}\n* Soyad:{db['Soyad']}\n* Balans:{db['Depozit']} ")
                        onlyUser()
                    if option == 2:
                        def drawMoneys():
                            drawMoney = int(input("Cəkmək istədiyiniz miqdari daxil edin: "))
                            if db['Depozit'] > drawMoney:
                                db['Depozit'] = db['Depozit'] - drawMoney
                            # else:
                            #     print("Balansinizda o qeder mebleg yoxdur")

                            with open("db.json", "w") as connect:
                                json.dump(data, connect)
                                print(f"Hesabinizdan {drawMoney}AZN deyerinde mebleg cixildi!")
                    drawMoneys()

                    if option == 3:
                        print("Emr 3")
                        onlyUser()
                    if option == 4:
                        from main import start
                        start()
                else:
                    print("Yalnız 1-4  arası bir secim edə bilərsiniz!")
                    onlyUser()

            onlyUser()
            # print(f"\n* Hesab nomresi:{db['Hesab nomresi']}\n* Ad:{db['Ad']}\n* Soyad:{db['Soyad']}\n* Balans:{db['Depozit']} ")

            finder = True
            break
    if finder == False:
        print(f"{hesabNomresi} -axtarişina uygun nəticə tapılmadı")
        getProductbyName()


getProductbyName()
