
print("bienvenidos al grupo 8S12")
print("Ingrese los caracteres")
cadena=input()
#codigo para calcular la moda    
repetir = 0                                                                         
for i in cadena:                                                                              
    aparece = cadena.count(i)                                                             
    if aparece > repetir:                                                       
        repetir = aparece                                                       
                                                                                         
moda = []                                                                               
for j in cadena:                                                                              
    aparece = cadena.count(j)                                                             
    if aparece == repetir and j not in moda:                                   
        moda.append(j)                                                                  
                                                                                         
print ("moda:", moda)


dOrder=sorted(cadena)

n=len(dOrder)
middle=n/2

# codigo para calcular la mediana

from statistics import mean

# codigo para calcular la media aritmetica

from statistics import median
