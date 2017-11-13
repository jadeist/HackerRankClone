# -*- decoding: utf-8 -*-
import math

def numeros_primos(x):
    #Answer: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
    lista_primos = []
    list = x.replace(' ','').split(",")
    for num in range(2,101):
        if all(num%i!=0 for i in range(2,num)):
            lista_primos.append(num)
            
    if len(list) == len(lista_primos):
        for z in range(0,len(list)):
            if str(lista_primos[z]) != str(list[z]):
                return False
        return True
    else:
        return False
    
def area_triangulo(x):
    #Answer: 25.75 (Area = (base * altura) / 2)
    try:
        base = 10.3
        altura = 5
        area = (base * altura) / 2
        if float(area) == float(x):
            return True
        return False
    except:
        return False

def respuesta_usuario(x):
    #Answer: Electroencefalografista,23,Electrodomóstico,16
    list_user = x.replace(' ','').split(",")
    list = ['Electroencefalografista','Electrodomóstico','Arteriosclerosis','Otorrinolaringólogo','Otorrinolaringólogo']
    
    #palabra Max
    palabra_max = ""
    for i in list:
        if len(palabra_max) < len(i):
            palabra_max = i
    if str(list_user[0]).lower() != palabra_max.lower() or str(list_user[1]) != str(len(palabra_max)):
        return False

    #palabra Min
    list_min = list
    palabra_min = list_min.pop()     
    for i in list:
        if len(palabra_min) > len(i):
            palabra_min = i
    if str(list_user[2]).lower() != palabra_min.lower() or str(list_user[3]) != str(len(palabra_min)):
        return False    
    return True

def palindromos(x):
    #Answwer: anita lava la tina, a mi me mima
    list = ['Anita lava la tina','A mi me mima','Mi mama masa la masa en la mesa']
    palindromo = []
    for i in list:
        if i.replace(" ","").lower() == i.replace(" ","").lower()[::-1]:
            palindromo.append(i.lower())
    if x.lower() in palindromo:
        return True
    return False

def siguiente_viaje(x):
    #Answwer: 2019
    frecuencia_usa = 2
    frecuencia_europa = 5
    viaje_ambos = 2009
    siguiente_viaje = frecuencia_europa * frecuencia_usa + viaje_ambos
    if str(x) == str(siguiente_viaje):
        return True
    else:
        return False

def vasitos_necesarios(x):
    #Answwer: 12
    #fraccion equivalente
    # 1 1/2 = 3/2 = 3/2 * 4 = 12/8; (12/8) / (1/8) = (12 * 8) / (8 * 1) = 12
    try: 
        cantidad_leche = 1.5
        capacidad_vasitos = 0.125
        necesidad_vasitos = cantidad_leche / capacidad_vasitos
        if str(float(x)) != str(necesidad_vasitos):
            return False
        return True
    except:
        return False
    
def agua_evaporada(x):
    #Answwer: 131578
    try:
        capacidad_total = 2500000 / 0.95
        litros_a_evaporar = int(capacidad_total * 0.05)
        if int(x) != litros_a_evaporar:
            return False
        return True
    except:
        return False

def sentido_vida(x):
    #Answwer: 42
    if str(x) != str(42):
        return False
    return True

from _datetime import datetime, timedelta
def hora_en_bucarest(x):
    #Answwer: Rumania GMT+2; México GMT-6 ->
    datenow = datetime.now() + timedelta(hours = 8)
    if datenow.strftime("%Y-%m-%d %H:%M") == x:
        return True
    return False
    
def matriz(x):
    #Answwer: [[2, 9], [4, 4]]
    try:
        matriz1= [[2, 3],[4, 2]]         # matriz 2x2
        matriz2= [[1, 1],[3, 2]]
        matrizF= [[0, 0],[0, 0]] 
        
        for i in range(len(matriz1)):
            for j in range(len(matriz2)):
                matrizF[i][j]+= matriz1[i][j]*matriz2[j][i]
        
        if str(x) == str(matrizF):
            return True
        return False
    except:
        return False