# Dados 3 numeros a,b,c verificar si pueden formar los lados de un triangulo

print("--------------------------------------------------------")
print("-----Dado-3-numeros-vereficar-si-forman-un-triangulo----")
print("--------------------------------------------------------")

print ("a=lado 1 ")
print ("b= lado 2 ")
print ("c= lado 3 ")

a= float(input("por favor ingresa el valor de a: "))
b=float(input("por favor ingresa el valor de b: "))
c= float(input("por favor ingresa el valor de c: "))



#input 

if a + b >= c and b + c >= a and a + c >= b:

    t=("Si,lo es")
else:
    t=("No lo es")

print("------------------")
print("----RESULTADOS----")
print("¿es realmente un triangulo? " + str(t))