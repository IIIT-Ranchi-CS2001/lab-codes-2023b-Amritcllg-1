names=['Aagman','Gyan','Arya','Hariom','Deepanshu']
roll=['1','2','3','4','5']
marks=['45','56','54','87','23']
cc=marks.copy()
idx=[i for i in range(len(marks))]
initial=[(names[i],roll[i],marks[i]) for i in idx]
for i in range(len(marks)):
    for j in range(len(marks)-1):
        if marks[j]>marks[j+1]:
            marks[j],marks[j+1]=marks[j+1],marks[j]
            idx[j],idx[j+1]=idx[j+1],idx[j]
res=[(names[i],roll[i],cc[i]) for i in idx]
print(f"INITAIL lIST  : {initial}")
print(f"FINAL LIST IS {res}")
