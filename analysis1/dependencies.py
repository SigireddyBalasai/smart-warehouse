import csv

def valuen(files,arg1,arg2,opening=0,close=0):

    f = open(f"{files}.csv",mode = 'r')
    lista = []
    listb = []
    listc = []
    reader = csv.reader(f)
    list1 = list(reader)
    if(close==0):
     b = len(list1)
    else:
     b = close
    in1 = list1[0].index(arg1)
    in2 = list1[0].index(arg2)
    for i in range(opening+1,b):
        lista.append(list1[i][in1])
        listb.append(list1[i][in2])
    listc.append(lista)
    listc.append(listb)
    f.close()
    return listc