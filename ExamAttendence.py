print("Please enter number of classes held")
Classheld=int(input())
print("Please enter number of classes attended")
ClassAttended=int(input())
if ClassAttended>Classheld:
    print("Your Held classes number should be less than attended class")
if ClassAttended < Classheld:
    Percentage= ClassAttended/Classheld*100
    if Percentage >75:
        print("Your total attedence Percentage is",Percentage)
        print("You Attendence is above 75 and allowed to sit in exam")
    else:
        print("Your Attendence Percentage",Percentage,"and not allowed to sit in exam")