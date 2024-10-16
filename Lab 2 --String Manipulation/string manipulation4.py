name=input("ENTER THE NAME OF THE STUDENT : ")
roll=int(input("ENTER THE ROLL NO. OF THE STUDENT : "))
marks=int(input("ENTER THE MARKS OF THE STUDENT IS MATHS : "))

print(f"Name : {name}")
print(f"Roll no. : {roll}")
print(f"Marks : {marks}")
remark=''
grade=0

if marks>=90:
    grade=10
    remark='OUTSTANDING'
if marks>=80 and marks<90:
    grade=9
    remark='VERY GOOD'
if marks>=70 and marks<80:
    grade=8
    remark='GOOD'
if marks>=60 and marks<70:
    grade=7
    remark='AVERAGE'
if marks>=50 and marks<60:
    grade=6
    remark='PASS'
if marks<50:
    grade=0
    remark='FAIL'
    
print(f"Grade Point : {grade}")
print(f"Remark : {remark}")

