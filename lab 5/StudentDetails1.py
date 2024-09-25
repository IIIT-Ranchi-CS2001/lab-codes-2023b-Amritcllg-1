names=['Aagman','Gyan','Arya','Hariom','Deepanshu']
roll=['1','2','3','4','5']
marks=['45','56','54','87','23']

l=list(zip(names,roll,marks))
print(l)
l.sort(key=lambda x:x[2])
print(l)