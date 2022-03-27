'''mesele3'''
password = input("Enter password: ")
parol = input("sifreni daxil edin: ")
num=1
while(num<3):
    if parol==password:
        print("sifre dogrudur")
        break
    else:
        print("sifre dogru deyil ")
        prol=input("sifreni yeniden daxil edin: ")
        num+=1

