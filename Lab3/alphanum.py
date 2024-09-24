s=input("ENTER A STRING : ")
s=s.lower()
alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
digits=['0','1','2','3','4','5','6','7','8','9']
flag=0
for ele in s:
    if ele not in alpha and ele not in digits:
        flag=1
print(not flag==1)