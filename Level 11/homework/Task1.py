#დაწერეთ პროგრამა, რომელიც იღებს ორი ადამიანის ასაკს და განსაზღვრავს ვინ არის უფროსი.

print("Enter any two numbers of age: ")
n1 = int(input("Enter age of the first person: "))
n2 = int(input("Enter age of the second person: "))
if n1 > n2:
    print("first person is older.")
elif n1 < n2:
    print("second person is older.")
elif n1 == n2:
    print("they are the same age.")