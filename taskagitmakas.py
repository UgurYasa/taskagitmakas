import random

def taş():
    if seçme == 1 :
        if bilgisayarin_sectigi == 1 :
            print("Bilgisayarla yenişemediniz !!!")
        elif bilgisayarin_sectigi == 2 :
            print("Taş makası kırar ")
            print("Siz Kazandınız !!!")
        elif bilgisayarin_sectigi == 3:
            print("Kağıt taşı sarar ")
            print("Bilgisayar Kazandı!!!")
def makas():
    if seçme == 2:
        if bilgisayarin_sectigi == 1:
            print("Taş makası kırar ")
            print("Bilgisayar Kazandı!!!")
        elif bilgisayarin_sectigi == 2:
            print("Bilgisayarla yenişemediniz !!!")
        elif bilgisayarin_sectigi == 3:
            print("Makas kağıdı keser")
            print("Siz Kazandınız !!!")

def kağıt():
    if seçme == 3:
        if bilgisayarin_sectigi == 1:
            print("Kağıt taşı sarar ")
            print("Siz Kazandınız !!!")
        elif bilgisayarin_sectigi == 2:
            print("Makas kağıdı keser")
            print("Bilgisayar Kazandı!!!")
        elif bilgisayarin_sectigi == 3:
            print("Bilgisayarla yenişemediniz !!!")




while True:
    seçenek = ["","taş","makas","kağıt"]

    print("-"*30+"TAŞ KAĞIT MAKAS OYUNUNA HOŞGELDİNİZ"+"-"*30)

    seçme = int(input("1 - > TAŞ\n2 - > MAKAS\n3 - > KAĞIT\n4- > ÇIKIŞ\n - - - >> "))

    bilgisayarin_sectigi = random.randint(1,3)
    print(f"Bilgisayarın seçtiği alet :{seçenek[bilgisayarin_sectigi]} ")
    print(f"Seçtiğiniz alet :{seçenek[seçme]} ")

    taş()
    kağıt()
    makas()
    if seçme == 4:break



