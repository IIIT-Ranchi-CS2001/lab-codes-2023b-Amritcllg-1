s=input("ENTER A SENTENCE : ")
s=s.lower()
temp=""
count=0

for i in range(len(s)+1):
    if i == len(s):
        if temp == temp[::-1]:
            count+=1
        break
    elif s[i] == " ":
        if temp == temp[::-1]:
            count+=1
        temp=""
    else:
        temp+=s[i]
        
print(f"COUNT OF PALINDROME WORDS ARE : {count}")
    
    
#shortcut
# count=0
# l=s.split()
# for ele in l:
#     if ele == ele[::-1]:
#         count+=1
# print(f"COUNT OF PALINDROME WORDS ARE : {count}")
