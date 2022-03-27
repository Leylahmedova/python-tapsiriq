'''Mesele 2-(8-13 arasi uzunlugda parol teyin etmek)'''
password = input("Sifreni daxil edin: ")

if len(password)>8 and len(password)<13:
        print("Sifre duzgundur:")
else:
        print("sifrenin uzunlugu 8 simvoldan az ve 13 simvoldan cox olmamalidir. Zehmet olmasa yeniden cehd edin!")
        
mesele3
password = input("Enter password: ")
parol = input("Parolu daxil edin: ")
num=1
while(num<3):
    if parol==password:
        print("Parol dogrudur")
        break
    else:
        print("Parol dogru deyil ")
        prol=input("Parolu yeniden daxil edin: ")
        num+=1

