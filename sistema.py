'''
Autors: Artjoms Donskojs DP1-2
'''



print("Matematiskais uzdevums")
print("----------------------------------------------------------------------------")
print()
print("Es vēlos pārbaudīt grupas DP1-2 zināšānas par sadalīšānu reizinātājos tēmu")
print()
print("Tas ir programmas 1. versija")
print()



def teorija():
    print()
    print()
    teorija=print("Izteiksmi sadalīt reizinātājos, jeb izveidot iekavas, var ar dažādiem paņēmieniem.\nKopīgā reizinātāja iznešana pirms iekavām. Lieto, ja visi izteiksmes locekļi satur vienu un to pašu reizinātāju.\nPiemērs:3x^2-7x^2=x(3-7x) \n8y^3+6y^2=y^2(8y+6) vai 2y^2(4y+3) \nSaīsināto reizināšanas formulu lietošana\nKvadrātu starpība: a^2-b^2=(a-b)(a+b)\nBinoma summas kvadrāts: a^2+2ab+b^2=(a+b)2=(a+b)(a+b)\nBinoma starpības kvadrāts: a^2-2ab+b^2-b)2-b-b)\nPiemērs-12x+9=(2x-2⋅2⋅3x+32-3)2-3-3-4x2-(2x)^2-2x)(z+2x-n^4=(v^2-(n^2)2-n^2)(v^2+n^2)")
    izvele()

def piemeri():
    atzime=0
    print("Piemēri tēmai Sadalīšana reizinātājos:")#Sadali reizinātājos, izmantojot kvadrātu starpības formulu!\n1.)(m+12)^2-9\n2.)36x^2-16c^2\n3.)16y^2-100m^2\n4.)4z^2-36c^2\n5.)9z^2-36m^2
    piemeri=["1.)(m+12)^2-9","2.)36x^2-16c^2","3.)16y^2-100m^2","4.)4z^2-36c^2","5.)9z^2-36m^2"]
    atbildes=["m^2+24m+135","(6x-4c)(6x+4c)","(4y-10m)(4y+10m)","(2z-6c)(2z+6c)","(3z-6m)(3z+6m)"]
    for i in range(0,5):
        print(piemeri[i])
        piem_atbilde=input("Ievadiet atbildi:")
        if piem_atbilde == atbildes[i]:
            print("Pareiza atbilde!")
            atzime = atzime + 1
        else:
            print("Nepareiza atbilde!")
        print(f"Jūs atbildējat pareizi uz {atzime} piemēriem no 5.")
    print(f'Jūsu vērtejums par piemēriem ir {atzime*2}')
    print()
    print()
    izvele()

def parbaudes_darbs():
    print("Vēl nav gatavs!!!")
    print()
    print()
    izvele()

def close():
    while close():
        break

def izvele():
    print("Ja vēlāties izlāsit teoriju, uzrākstiet 't'; Ja vēlāties sākt pīldīt piemērus, uzrāksitet 'p'; Ja vēlāties sākt pīldīt parbaudes darbu, uzrākstiet 'a', Ja vēlāties izsledz programmu, uzrākstiet 'b' ")
    izvele=input('Atbilde: ')
    if izvele == "t":
        teorija()
    if izvele == "p":
        piemeri()
        print()
        print()
    if izvele == "a":
        parbaudes_darbs()
        print()
        print()
izvele()
