s=input("ENTER A STRING : ")
count={i:s.count(i) for i in set(s)}
for ele in set(s):
    print(f"COUNT OF '{ele}' is : {count[ele]}")