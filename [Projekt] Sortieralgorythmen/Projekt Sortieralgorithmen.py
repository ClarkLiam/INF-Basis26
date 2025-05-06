#Projekt Sortieralgorithmen#

from random import randint
import cProfile


#Funktionen#
def zufall(n):
    liste = []
    for i in range(n):
        liste.append(random.randint(1,1000))
    return liste

def beste(n):
    liste = []
    for i in range(n):
        liste.append(i)
    return liste

def miese(n):
    liste = []
    for i in range(n,0,-1):
        liste.append(i)
    return liste

def ist_sortiert(liste):
    for i in range(len(liste)-1):
        if liste[i] > liste[i+1]:
            return False
    return True


#Funktionen#
#Bubble Sort (vergleich)#
def bubble_sort(liste):
    n = len(liste)
    for i in range(n):
        for j in range(0, n-i-1):
            if liste[j] > liste[j+1]:
                liste[j], liste[j+1] = liste[j+1], liste[j]
    return liste

#insertion Sort#

#selection Sort#

#Gnome Sort#
def gnome_sort(liste):
    n = len(liste)
    i = 0

    while i < n:
        if i == 0:
            i = i + 1
        if liste[i] >= liste[i-1]:
            i = i + 1
        else:
            liste[i], liste[i-1] = liste[i-1], liste[i]
            i = i - 1
    return liste

#Test Funktion#
def test_runtime(sort, type, n):
    liste = []
    if type == "zufall":
        liste = zufall(n)
    elif type == "beste":
        liste = beste(n)
    elif type == "miese":
        liste = miese(n)
    else:
        print("Falscher Typ")
        return
    
    print("Ist sortiert:", ist_sortiert(liste))
    
    if sort == "bubble":
        cProfile.run("bubble_sort(liste)")
    elif sort == "gnome":
        cProfile.run("gnome_sort(liste)")
    elif sort == "insertion":
        cProfile.run("insertion_sort(liste)")
    elif sort == "selection":
        cProfile.run("selection_sort(liste)")
    else:
        print("Falscher Sortieralgorithmus")
        return
    print("Ist sortiert:", ist_sortiert(liste))


#Test#
sort = input("Sortieralgorithmus auswählen: bubble, gnome, insertion, selection")
type = input("Listentyp auswählen: zufall, beste, miese")
n = int(input("Listengröße eingeben: "))
test_runtime(sort, type, n)