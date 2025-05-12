def dobra(lst):
    pos=0
    while pos<len(lst):
        lst[pos]*=2
        pos+=1
valores=[0,4,0,5,2,5]
dobra(valores)
print(valores)