s=input("ENTER THE STRING : ").split(' ')
letter=list(filter(lambda x:x.isalpha(),s))
numbers=list(filter(lambda x:x.isnumeric(),s))
alphanumeric=list(filter(lambda x:x.isalnum(),s))
letter=list(map(lambda x:x.upper(),letter))
numbers=list(map(lambda x:int(x)**2,numbers))
print(letter)
print(numbers)
print(alphanumeric)