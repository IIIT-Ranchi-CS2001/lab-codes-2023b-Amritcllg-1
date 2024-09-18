course_code=['CS2001','MA2001','CS2005','CS2007','HS2001']
course_name=['Python','MATHEMATICS-III','THEORY OF COMPUTATION','FUDAMENTALS OF ALGORITHMS','MANAGMENT']

l=list(zip(course_code,course_name))
res=[]
for ele in l:
    res.append(ele[0]+' : '+ele[1])


print(f"INITIAL LIST OF COURSE CODES IS : {course_code}")
print(f"INITIAL LIST OF COURSE NAMES IS : {course_name}")
print(f"FINAL LIST IS : {res}")
