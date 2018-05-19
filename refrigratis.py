'''
Created on 1 de set de 2016

@author: Hugo
'''

lista3 = []
lista2 = []
lista4 = []

def metodo1(entrada,lista2):
    if entrada>=3:
        entrada = entrada/3
        lista2.append(entrada)
        if entrada<2 and entrada>=1.5:
            entrada = int(entrada+1)
            if entrada ==2:
                entrada+=1
        if int(entrada) == 2:
            entrada = int(entrada+1)
        metodo1(entrada, lista2)

def metodo1Exato(entrada,lista3):
    if entrada>=3:      
        entrada = entrada/3
        lista3.append(entrada)
        if entrada == 2:
            entrada+=1
        metodo1Exato(entrada, lista3)

entrada=input()
lista = entrada.split(' ')

for i in lista:
    k = int(i)
    if k%3 !=0:
        lista2.append(k)
        metodo1(k, lista2)
        soma2=sum(lista2)
        lista4.append(soma2)
    elif k%3 ==0:
        lista3.append(k)
        metodo1Exato(k, lista3)
        soma3=int(sum(lista3))
        lista4.append(soma3)

for i in lista4:
    j = int(i)
    print(j, end=' ')
