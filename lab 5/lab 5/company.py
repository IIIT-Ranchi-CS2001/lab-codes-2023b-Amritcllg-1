names=input("ENTER THE NAME OF 5 EMPLOYEES : ").split()
salary=list(map(int,input("ENTER THE SALARIES OF 5 EMPLOYEES : ").split()))
employee={names[i]:salary[i] for i in range(len(names))}
for i in range(len(salary)):
    for j in range(len(salary)-1):
        if salary[j]>salary[j+1]:
            salary[j],salary[j+1]=salary[j+1],salary[j]
            names[j],names[j+1]=names[j+1],names[j]
for i in range(len(names)):
    print(f"{i+1}. {names[i]} : Rs. {salary[i]}")