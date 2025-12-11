name=str(input("enter your name."))
std=int(input("enter your class."))
sec=str(input("enter your section."))
marks=float(input("enter your marks."))
if marks>100 and marks<0:
    print("error.")
elif marks<50:
    print("you are fail.")
elif marks>50 and marks<60:
    print("you are pass with good marks.")
elif marks>60 and marks<80:
    print("you are pass with very good marks.")	
elif marks>80 and marks<100:
    print("you are pass with outstanding marks.")
    