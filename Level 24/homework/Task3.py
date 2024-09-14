num = int(input("enter your age: "))
num1 = int(input("enter how good you are at driving on a scale 1 to 10: ")) 

if num < 18:
    print("sorry you are not allowed to drive yet")
elif num >= 18 and num1 >= 1:
    print("you are allowed to drive already!")