def my_max(a):
    res=float('-inf')
    for ele in a:
        if res<ele:
            res=ele 
    return res

print(my_max([-1,-2,-5,-6,-2]))
print(my_max((1,24,3,9,4,5)))
print(my_max({18,2,34,2,14,8}))