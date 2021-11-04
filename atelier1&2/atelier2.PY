print("exercice1")
list1=[3, 6, 9, 12, 15, 18, 21]
list2=[4, 8, 12, 16, 20, 24, 28]
list3=[]
for count, i in enumerate(list1):
    if count % 2 == 1:
        list3.append(i)
for count, i in enumerate(list2):
    if count % 2 == 0:
        list3.append(i)
print(list3)

print("exercice2")
list=[11, 45, 8, 23, 14, 12, 78, 45, 89]
list1=list[:3]
list1.reverse()
list2=list[3:6]
list2.reverse()
list3=list[6:9]
list3.reverse()
print(list1,list2,list3)

print("exercice3")
dict={}
liste=[11, 45, 8, 11, 23, 45, 23, 45, 89]
com = {}.fromkeys(liste,0)
for valeur in liste:
 com[valeur] += 1
print(com)

print("exercice4")

setA={23, 42, 65, 57, 78, 83, 29}
setB={57, 83, 29, 67, 73, 43, 48}
print("le 1er set",setA)
print("le 2eme set",setB)
intersection=(setA & setB)
print("intersection ",intersection)
supp=setA-intersection
print("Set 1 apres suppression :",supp)

