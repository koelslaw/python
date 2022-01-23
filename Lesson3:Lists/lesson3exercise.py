myintlist = []
mystringlist = []

myintlist.append(1)
myintlist.append(3)
myintlist.append(5)

mystringlist.append("the")
mystringlist.append("is")
mystringlist.append("the")
mystringlist.append("list")

print(mystringlist)
print(myintlist)

for x in myintlist:
    print (x)


for x in mystringlist:
    print (x)


oneitem = myintlist[2]
print(oneitem)