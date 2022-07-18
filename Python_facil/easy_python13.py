#Python – Ciclo while
print("##### Ejemplo ciclo while ####")
i = 1
while i <= 10:
    print (i)
    i += 1

print("#####Ejemplo ciclo while y break ####")
x = 1
while x < 4: 
    print(x)
    if x == 3:
        break
    x += 1 

print("#####Ejemplo ciclo while y continue ####")
y = 0
while y < 8:
    y += 1
    if y == 5:
        continue
    print(y)