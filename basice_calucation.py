# this funcation are use basice calcuation add,sub,div,modu,and 
# user any two number input and perforam to mathematics operations 
number_1=int(input('ENTER THE FIRST NUMBER==>'))
number_2=int(input("ENTER THE SECOND NUMBER==>"))
choise=input("ENTER THE SOME ONLY ONE SYMBLE THAT  PERFORM MATHMATICS OPERATIONS LIKE=(+),(-),(*),(/) ")
if choise == "+":
    print("ANSWER==>",number_1 + number_2)
elif choise == "-":
    print("ANSWER==>",number_1 - number_2)
elif choise == "*":
    print("ANSWER==>",number_1 * number_2)
elif choise=="/":
    if number_2 !=0:
     print("ANSWER==>",number_1 / number_2)
    else:
        print("Division by zero is not allowed.")
else:
    print("YOU NOT ENTER ANY SYMBLE")


