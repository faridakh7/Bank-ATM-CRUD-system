from admin.admin import *
from user.user import *
from register import *
from  closeApp import *



def start():
    firstCommand = input("""
    Aşağıdakı Əmrlərdən Birini Secin:
    1.Hesaba Daxil olmaq
    2.Bankdan qeydiyyatdan keçmək
    3.Admin girisi
    4.Çıxış

Seciminizi Daxil edin:  """).strip()
    if firstCommand.isnumeric() and 0 < int(firstCommand) < 5:
        option = int(firstCommand)

        if option == 1:
            getProductbyName()
        if option == 2:
            userRegister()
        if option == 3:
            control()
        if option == 4:
            programbitdi()
    else:
        print("Yalnız 1-4  arası bir secim edə bilərsiniz!")
        start()


start()
