#დაწერეთ პროგრამა, რომელიც მოუწოდებს მომხმარებელს შეიყვანოს ნივთების რაოდენობა, რომლის შეძენაც სურს.
# დარწმუნდით, რომ მომხმარებელი შეიყვანს დადებითი რიცხვს.
# თითოეული ნივთისთვის, შესთავაზეთ მომხმარებელს შეიყვანოს ფასი.
# დარწმუნდით, რომ მომხმარებელი შეიყვანოს დადებითი რიცხვს პროდუქტის ფასისთვის.
# გამოთვალეთ და აჩვენეთ ყველა ელემენტის მთლიანი ღირებულება.
print("Here you can buy max 10 items!")
num1 = input("Welcome to the store! please enter the number of the idems you want to buy!:")
if int(num1) < 0:
    print("please enter positive number!")
elif int(num1) > 10:
    print("Here you can buy max 10 items!")
else:
    print("processing")

if int(num1) == 1:
    num2 = input("please enter the prices of the items you want to buy!:")
elif int(num1) == 2:
    num3 = input("enter the price of the first item:")
    num4 = input("enter the price of the next item:")
    print( int(num3) + int(num4))
elif int(num1) == 3:
    num5 = input("enter the price of the first item")
    num6 = input("enter the price of the next item:")
    num7 = input("enter the price of the next item:")
    print( int(num5) + int(num6)+ int(num7))
elif int(num1) == 4:
     num8 = input("enter the price of the first item")
     num9 = input("enter the price of the next item:") 
     num10 = input("enter the price of the next item:")
     num11 = input("enter the price of the next item:")
     print( int(num8) + int(num9)+ int(num10) + int(num11))
elif int(num1) == 5:
     num12 = input("enter the price of the first item:")
     num13 = input("enter the price of the next item:")
     num14 = input("enter the price of the next item:")
     num15 = input("enter the price of the next item:")
     num16 = input("enter the price of the next item:")
     print( int(num12) + int(num13)+ int(num14) + int(num15) + int(num16))
elif int(num1) == 6:
     num17 = input("enter the price of the first item:")
     num18= input("enter the price of the next item:")
     num19= input("enter the price of the next item:")
     num20= input("enter the price of the next item:")
     num21= input("enter the price of the next item:")
     num22= input("enter the price of the next item:")
     print( int(num17) + int(num18)+ int(num19) + int(num20) + int(num21) + int(num22))
elif int(num1) == 7:
      num23 = input("enter the price of the first item:")
      num24= input("enter the price of the next item:")
      num25= input("enter the price of the next item:")
      num26= input("enter the price of the next item:")
      num27= input("enter the price of the next item:")
      num28= input("enter the price of the next item:")
      num29= input("enter the price of the next item:")
      print( int(num23) + int(num24)+ int(num25) + int(num26) + int(num27) + int(num28) + int(num29))
elif int(num1) == 8:
      num30= input("enter the price of the first item:")
      num31= input("enter the price of the next item:")
      num32= input("enter the price of the next item:")
      num33= input("enter the price of the next item:")
      num34= input("enter the price of the next item:")
      num35= input("enter the price of the next item:")
      num36= input("enter the price of the next item:")
      num37= input("enter the price of the next item:")
      print( int(num30) + int(num31)+ int(num32) + int(num33) + int(num34) + int(num35) + int(num36) + int(num37))
elif int(num1) == 9:
      num38= input("enter the price of the first item:")
      num39= input("enter the price of the next item:")
      num40= input("enter the price of the next item:")
      num41= input("enter the price of the next item:")
      num42= input("enter the price of the next item:")
      num43= input("enter the price of the next item:")
      num44= input("enter the price of the next item:")
      num45= input("enter the price of the next item:")
      num46= input("enter the price of the next item:")
      print( int(num38) + int(num39)+ int(num40) + int(num41) + int(num42) + int(num43) + int(num44) + int(num45) + int(num46))
elif int(num1) == 10:
      num47= input("enter the price of the first item:")
      num48= input("enter the price of the next item:")
      num49= input("enter the price of the next item:")
      num50= input("enter the price of the next item:")
      num51= input("enter the price of the next item:")
      num52= input("enter the price of the next item:")
      num53= input("enter the price of the next item:")
      num54= input("enter the price of the next item:")
      num55= input("enter the price of the next item:")
      num56= input("enter the price of the next item:")
      print( int(num47) + int(num48)+ int(num49) + int(num50) + int(num51) + int(num52) + int(num53) + int(num54) + int(num55) + int(num56))
else:
     print(".")
      
      
     