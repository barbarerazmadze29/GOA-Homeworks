middle_score = int(input("enter middle score: "))
final_score = int(input("enter middle score: "))
project_score = int(input("enter middle score: "))

answer = ((middle_score + final_score + project_score) / 3)

if answer >= 70:
    print("great job! you passed!")
else:
    print("I'm sorry.. you have failed your exems ")