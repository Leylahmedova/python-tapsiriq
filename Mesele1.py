print("emeli secin!")
print("1.Toplama")
print("2.Cixma")
print("3.Vurma")
print("4.Bolme")

while True:
    
    emel = input("emeli daxil edin(1/2/3/4): ")

    if emel in ('1', '2', '3', '4'):
        num1 = float(input("1-ci ededi daxil edin: "))
        num2 = float(input("2-ci ededi daxil edin: "))

        if emel == '1':
            print(num1, "+", num2, "=", num1+num2)

        elif emel == '2':
            print(num1, "-", num2, "=", num1-num2)

        elif emel == '3':
            print(num1, "*", num2, "=", num1*num2)

        elif emel == '4':
            print(num1, "/", num2, "=", num1/num2)
    else:
        print("yerine yetirile bilmedi")
