guessing_number=18
countoften=1
while countoften<=10:
    print("guess the number")
    userinput=int(input())
    if userinput>18:
         print("the value is high")
    elif userinput<18:
         print("the value is low") 
    elif userinput==18:
         print("very good  you are win")
         print("you are won",countoften,"life") 
    print(10-countoften,"life's left")   
    countoften=countoften+1   
if countoften>10:
    print("you lose")
