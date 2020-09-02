from admin.admin import  *
from user.user import  *


def start():
    firstCommand = input("""
    Aşağıdakı Əmrlərdən Birini Secin:
    1.Hesaba Daxil olmaq
    2.Bankdan qeydiyyatdan keçmək
    3.Admin girisi
    4.Çıxış

Seciminizi Daxil edin:  """).strip()
    if firstCommand.isnumeric() and 0 < int(firstCommand) < 4:
        option = int(firstCommand)

        if option == 1:
            onlyUser()
        if option == 2:
            print("Bankdan qeydiyyatdan keçmək")
        if option == 3:
            control()
        if option == 4:
            def programbitdi():
                print("Program muveffeqiyyətlə dayandırıldı")
                return

            programbitdi()
    else:
        print("Yalnız 1-4  arası bir secim edə bilərsiniz!")
        start()





start()
