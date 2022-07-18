# Secuencias de números
"""Es muy habitual hacer uso de secuencias de números en bucles. 
Python no tiene una instrucción específica para ello. Lo que sí aporta es una función range() 
que devuelve un flujo de números en el rango especificado. Una de las grandes ventajas es que la «lista»
generada no se construye explícitamente, sino que cada valor se genera bajo demanda. Esta técnica mejora
 el consumo de recursos, especialmente en términos de memoria.""" 

"""La técnica para la generación de secuencias de números es muy similar a la utilizada en los «slices» 
de cadenas de texto. En este caso disponemos de la función range(start, stop, step):"""

#start: Es opcional y tiene valor por defecto 0.

#stop: es obligatorio (siempre se llega a 1 menos que este valor).

#step: es opcional y tiene valor por defecto 1.

#range() devuelve un objeto iterable, así que iremos obteniendo
#los valores paso a paso con una sentencia for ... in 3. Veamos diferentes ejemplos de uso:

#Rango: [0,1,2] 
print("Inicio")
for i in range(0, 3):
    print(i)
print("Fin")
##################################
print("Inicio")
for o in range(3):
    print(o)
print("Fin")
##################################
#Rango: [1,3,5]
print("Inicio")
for e in range(1,6,2):
    print(e)
print("Fin")

##############################
#Rango: [2,1,0]
print("Inicio")
for ez in range(2,-1,-1):
    print(ez)
print("Fin")
