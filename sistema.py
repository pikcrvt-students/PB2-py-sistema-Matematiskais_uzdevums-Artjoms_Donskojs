'''
Autors: Artjoms Donskojs DP1-2
-------------------------------
Matematiskais uzdevums
'''

from time import sleep

#Izvadam tekstu
print("Matematiskais uzdevums")
sleep(1)
print("----------------------------------------------------------------------------")
sleep(1)
print()
print("Es vēlos pārbaudīt grupas DP1-2 zināšānas par sadalīšānu reizinātājos tēmu")
sleep(1)
print()
print("Tas ir programmas 1. versija")
sleep(1)
print()


#Definējam teoriju
def teorija():
    print()
    print()
    teorija=print("Izteiksmi sadalīt reizinātājos, jeb izveidot iekavas, var ar dažādiem paņēmieniem.\n\nKopīgā reizinātāja iznešana pirms iekavām. Lieto, ja visi izteiksmes locekļi satur vienu un to pašu reizinātāju.\n\nPiemērs:3x^2-7x^2=x(3-7x) \n8y^3+6y^2=y^2(8y+6) vai 2y^2(4y+3) \n\nSaīsināto reizināšanas formulu lietošana\n\nKvadrātu starpība: a^2-b^2=(a-b)(a+b)\nBinoma summas kvadrāts: a^2+2ab+b^2=(a+b)2=(a+b)(a+b)\nBinoma starpības kvadrāts: a^2-2ab+b^2-b)2-b-b)\n\nPiemērs-12x+9=(2x-2⋅2⋅3x+32-3)2-3-3-4x2-(2x)^2-2x)(z+2x-n^4=(v^2-(n^2)2-n^2)(v^2+n^2)")
    izvele() #Izvadam izveles funkciju, lai lietotājs vārētu izvēlēties nākamo dārbību

#Definējam piemērus
def piemeri():
    atzime=0
    print("Piemēri tēmai Sadalīšana reizinātājos:")#Sadali reizinātājos, izmantojot kvadrātu starpības formulu!\n1.)(m+12)^2-9\n2.)36x^2-16c^2\n3.)16y^2-100m^2\n4.)4z^2-36c^2\n5.)9z^2-36m^2
    piemeri=["1.)(m+12)^2-9","2.)36x^2-16c^2","3.)16y^2-100m^2","4.)4z^2-36c^2","5.)9z^2-36m^2"]
    atbildes=["m^2+24m+135","(6x-4c)(6x+4c)","(4y-10m)(4y+10m)","(2z-6c)(2z+6c)","(3z-6m)(3z+6m)"]
    for i in range(0,5): #Cikls ar skaitītāju
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
    izvele() #Izvadam izveles funkciju, lai lietotājs vārētu izvēlēties nākamo dārbību

#Definējam parbaudes darbu funkciju
def parbaudes_darbs():
    print("Vēl nav gatavs!!!")
    print()
    print()
    izvele() #Izvadam izveles funkciju, lai lietotājs vārētu izvēlēties nākamo dārbību

#Definējam close funkciju
def close():
    exit()

#Definējam error funkciju
def error():
    print("Nepareiza ievade!!!\n\nKļuda!!!")
    print()
    print()
    izvele()

#Definējam izveles funkciju
def izvele():
    print("Ja vēlāties izlāsit teoriju, uzrākstiet 't'; Ja vēlāties sākt pīldīt piemērus, uzrāksitet 'p'; Ja vēlāties sākt pīldīt parbaudes darbu, uzrākstiet 'a', Ja vēlāties izsledz programmu, uzrākstiet 'b' ")
    izvele=input('Atbilde: ')
    if izvele == "t": #Ja 't', tad izvadam teoriju
        teorija()
    if izvele == "p": #Ja 'p', tad izvadam piemērus
        piemeri()
        print()
        print()
    if izvele == "a": #Ja 'a', tad izvadam parbaudes darbu
        parbaudes_darbs()
        print()
        print()
    if izvele == "b": #Ja 'b', tad beidzam programmu
        close()
        print()
        print()
    else:
        error()
izvele() #Izvadam izveles funkciju, lai lietotājs vārētu izvēlēties nākamo dārbību
