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

    
customer_name=['A','B','C','D','E']
customer_id=['1001','1002','1003']
shopping_points=[43,56,98,101]

print(my_zip(customer_name,customer_id,shopping_points,strct=False))
