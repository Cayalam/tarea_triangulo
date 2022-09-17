# Determinar si un triangulo es isoseles, equilatero o escaleno

print("----------------------------------------")
print("----Segun-sus-lados-que-triangulo-es----")
print("----------------------------------------")

a=float(input("igrese la longitud del lado a: "))
b=float(input("igrese la longitud del lado b: "))
c=float(input("igrese la longitud del lado c: "))

# Processing
if a == b == c :
    x=("un triangulo equilatero")
elif (a == b) !=c and (a == c) !=b and (b == c) !=a:
    x=("un triangulo isosceles")
elif a != b and a != c and b != c :
    x=("un triagulo escaleno")

print("-------------------")
print("----RESULTADOS-----")
print("Segun sus longitudes pertenece a: " + str(x))