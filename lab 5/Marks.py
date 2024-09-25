names=input("ENTER THE NAME OF 5 STUDENTS : ").split()
marks=list(map(int,input("ENTER THE MARKS OF 5 STUDENTS : ").split()))
student={names[i]:marks[i] for i in range(len(names))}
high_performers=[i for i in student.keys() if student[i]>=85]
avergae_performers=[i for i in student.keys() if student[i]<85 and student[i]>=60]
low_performers=[i for i in student.keys() if student[i]<60]
print(f"NUMBER OF HIGH PERFORMERS : {len(high_performers)}")
print(f"HIGH PERFORMERS ARE ",end=" ")
print(*high_performers)
print(f"NUMBER OF AVERAGE PERFORMERS : {len(avergae_performers)}")
print(f"AVERAGE PERFORMERS ARE ",end=" ")
print(*avergae_performers)
print(f"NUMBER OF LOW PERFORMERS : {len(low_performers)}")
print(f"LOW PERFORMERS ARE ",end=" ")
print(*low_performers)
print(f"THE HIGHEST MARKS SCORED IS : {max(student.values())}")
print(f"PERSON WITH THE HIGHEST MARKS IS : {max(student.keys(), key=lambda x:student[x])}")
