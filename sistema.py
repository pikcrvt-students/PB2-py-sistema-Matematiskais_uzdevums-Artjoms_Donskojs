'''
Autors: Artjoms Donskojs DP1-2
-------------------------------
Matematiskais uzdevums
'''

from time import sleep
import doctest


#Izvadam tekstu
print("Matematiskais uzdevums")
sleep(1)
print("----------------------------------------------------------------------------")
sleep(1)
print()
print("Es vēlos pārbaudīt grupas DP1-2 zināšānas par sadalīšānu reizinātājos tēmu")
sleep(1)
print()
print("Tas ir programmas 2. versija")
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
    atzime = 0
    parb_darb_punkt = 10/12
    print(parb_darb_punkt)
    parb_darb_piemeru_skaits = 12
    print("Parbaudes darbs.")
    sleep(1)
    print("Parbaudes darba piemēri:")
    sleep(1)
    parbaudes_darba_piemeri=['(k+20)^2-9','(t+16)^2-25','(m+18)^2-36','(d+14)^2-16','(n+11)^2-49','(c+14)^2-4','(n+14)^2-81','(t+15)^2-9','(k+18)^2-16','(k+17)^2-81','81y^2 - 9b^2','25x^2 - 64c^2']
    parbaudes_darba_atbildes=['(k+17)(k+23)','(t+11)(t+21)','(m+12)(m+24)','(d+10)(d+18)','(n+4)(n+18)','(c+12)(c+16)','(n+5)(n+23)','(t+12)(t+18)','(k+14)(k+22)','(k+8)(k+26)','(9y-3b)(9y+3b)','(5x-8c)(5x+8c)']
    for i in range(0,12):
        print(parbaudes_darba_piemeri[i])
        parb_atbilde = input("Ievadiet atbildi:")
        if parb_atbilde == parbaudes_darba_atbildes[i]:
            print("Pareiza atbilde!")
            atzime = atzime + parb_darb_punkt
        else:
            print("Nepareiza atbilde!")
        punkti = round(atzime,2)
        vertejums = round(atzime)
        print(f"Jūsu punktu skaits ir {punkti}")
    print(f'Jūsu vērtejums par parbaudes darbu ir {vertejums}')
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

'''
def numbers_sum(n):
    
   #This function returns the sum of all the argumets
   #Shell commands for testing
   #incoking the function followed by expected output:
   #>>> numbers_sum(1, 2, 3, 4, 5)
   #15
   #>>> numbers_sum(6, 7, 8)
   #21
    
    return sum(n)
doctest.testmod(name='numbers_sum', verbose=True)
'''

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
