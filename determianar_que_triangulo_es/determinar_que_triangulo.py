# Determiar  si un triagulos es obtuso, recto o agudo

print("---------------------------------------")
print("---Determiar-que-tipo-de-triagulo-es---")
print("---------------------------------------")

a=float(input("ingrese el angulo a: "))
b=float(input("ingrese el angulo b: "))
c=float(input("ingrese el angulo c: "))

# processing
if a + b + c == 180:
    T=("Si es un triangulo")
    if a == 90:
        R=("recto")
    elif b == 90:
        R=("recto")
    elif c == 90:
        R=("recto")
    elif a > 90:
        R=("obtuso")
    elif b > 90:
        R=("obtuso")
    elif c > 90:
        R=("obtuso")
    elif  a < 90:
        R=("agudo")
    elif  b < 90:
        R=("agudo")
    elif  c < 90: 
        R=("agudo")
else:
    T=("No es un triangulo")

print("------------------")
print("----RESULTADOS----")
print("¿Es un triangulo?: " + str(T))
print("Es un triangulo de tipo : " + str(R))
