print("1/  programme pour trouver la somme des séries 1! / 1 + 2! / 2 + 3! / 3 + 4! / 4 + 5! / 5 en utilisant la fonction.")
def fact(n):
 x=1
 for i in range(2,n+1) :
  x*=i
 return x
som=fact(1)/1+fact(2)/2+fact(3)/3+fact(4)/4+fact(5)/5

print("la somme des séries 1! / 1 + 2! / 2 + 3! / 3 + 4! / 4 + 5! / 5 égale a =",som)

print("2/ programme  pour convertir le nombre décimal en nombre binaire en utilisant la fonction.")
def convertir(n):
 if n>1: 
  convertir(n//2)
  print(n%2)
nbr=int(input("entrer un nombre a convertir "))
convertir(nbr)
print(" ")
print("3/ programme pour calculer la somme des nombres de 1 à n en utilisant la récursivité.")
def somme(n):
 sum=0
 if(n==0):
  return 0
 else: 
  return n+somme(n-1)

nbr=int(input("le nombre "))
print("la somme est de",somme(nbr))

print("4/programme  pour imprimer la série Fibonacci en utilisant la récursivité.") 
def fibonacci(n):
 if n==0 or n==1:
    return n
 else:
  return fibonacci(n-2)+fibonacci(n-1)

nbr=int(input("entrer un nombre "))
print("les",nbr,"premiers termes de la série fibonacci sont:")
for i in range(nbr):
 print( fibonacci(i))

print("5/  programme  pour compter les chiffres d'un nombre donné en utilisant la récursivité.")
def compteur(nbr):
 if nbr<10:
  return 1
 else :
  return 1+compteur(nbr/10)
n=int(input("entrer un nombre"))
print(compteur(n))

print("6/ trois fonctions  pour trier un tableau selon les algorithmes : tri a bull, tri par sélection et tri par insertion.")
#tri par selection
def tri_select(tab):
 for i in range(len(tab)):
  # Trouver le min du tableau
  min = i
 for j in range(i+1, len(tab)):
     if tab[min] > tab[j]:
       min =j 
 
 tmp = tab[i]
 tab[i] = tab[min]
 tab[min] = tmp
 return tab
#tri a bulle
def tri_bulle(tab):
  n = len(tab)
 # Traverser tous les éléments du tableau
  for i in range(n):
   for j in range(0, n-i-1):
 # échanger si l'élément trouvé est plus grand que le suivant
     if tab[j] > tab[j+1] :
      tab[j], tab[j+1] = tab[j+1], tab[j]

#tri par isertion
def tri_insertion(tab): 
    # Parcour de 1 à la taille du tab
    for i in range(1, len(tab)): 
        k = tab[i] 
        j = i-1
        while j >= 0 and k < tab[j] : 
                tab[j + 1] = tab[j] 
                j -= 1
        tab[j + 1] = k
# Programme principale pour tester le code ci-dessus
tab = [8, 2, 5, 3, 21, 7, 6, 7]
tri_insertion(tab) 
print ("Le tableau trié est:")
for i in range(len(tab)): 
    print ("% d" % tab[i])
print("7/ fonction qui inverse les lettres d’une chaîne de caractères")

def inverse(ch):
    
    ch1=""
    for lettre in ch:
        ch1=lettre+ch1
    print (ch1) 


chaine=input("entrere une chaine a inverser  ")
print(inverse(chaine))

