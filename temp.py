__author__ = 'dragon'




mylist = []
for i in range(1, 10):
    temp = []
    temp.append(i)
    temp.append('name%d'%i)

    mylist.append(temp)


print mylist

