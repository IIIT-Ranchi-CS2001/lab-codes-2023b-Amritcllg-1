l=list(map(int,input('ENTER THE ELEMENTS OF THE LIST : ').split()))
l.sort()
size=len(l)
meadin=0
mean=sum(l)/size
if size%2==0:
    meadin=l[size//2]
else:
    median=(l[size//2]+l[(size//2)+1])//2
    
count_dic={i:l.count(i) for i in set(l)}
mode=max(l,key=lambda x: count_dic.get(x,-1))
print(f"MEAN : {mean}, MEDAIN : {median}, MODE : {mode}")