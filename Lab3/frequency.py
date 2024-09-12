s=input("ENTER THE STRING : ")
c=input("ENTER THE CHARACTER TO COUNT : ")
count=0
for ele in s:
    if ele == c:
        count+=1
print(f"COUNT OF {c} IN THE PROVIDED STRING IS {count}")