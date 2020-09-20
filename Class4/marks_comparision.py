marks=int(input("Enter your marks: "))
#passing marks are 35
# print(marks>=35)

print("You have failed")
if marks>=35 and marks<=100:
    print("you have passed")
elif marks>=0 and marks<=35:
    print("you have failed")
    print("please enter correct marks")
