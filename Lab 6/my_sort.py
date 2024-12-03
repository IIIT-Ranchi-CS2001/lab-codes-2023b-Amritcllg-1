import copy
def my_zip(a,b,c,strct):
    if strct:
        if len(a) == len(b) and len(b) == len(c):
            res=[]
            for i in range(len(a)):
                res.append((a[i],b[i],c[i]))
            return res
        else:
            return None 
    else:
        res=[]
        l=len(min(a,b,c,key=len))
        for i in range(l):
            res.append((a[i],b[i],c[i]))
        return res

    
customer_name=['Amrit','Aagman','Deepanshu','Ayush','Chirag']
customer_id=['1003','1005','1001']
shopping_points=[43,56,98,101]

def my_sort(l,Key):
    temp=copy.deepcopy(l)
    for i in range(len(l)):
        for j in range(len(l)-1-i):
            if temp[j][Key] > temp[j+1][Key]:
                temp[j],temp[j+1]=temp[j+1],temp[j]
    return temp

print(my_sort(my_zip(customer_name,customer_id,shopping_points,strct=False),Key=2))




    
