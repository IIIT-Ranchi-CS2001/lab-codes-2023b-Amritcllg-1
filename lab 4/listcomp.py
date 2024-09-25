l=list(map(int,input('ENTER THE ELEMENTS OF THE LIST : ').split()))
l.sort()
size=len(l)
median=0
mean=sum(l)/size
if size%2==1:
    median=l[((size+1)//2)-1]
else:
    median=(l[(size//2)-1]+l[(size//2)])/2
    
mode=0
f=float('-inf')
for ele in l:
    if l.count(ele)>f:
        f=l.count(ele)
        mode=ele
print(f"MEAN : {mean}, MEDAIN : {median}, MODE : {mode}")