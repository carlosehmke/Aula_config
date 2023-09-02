#Aula para exercitar a tipagem

# Tipos primiticos

#Tudo em Python é um objeto

#O operador + é poliformico, ou seja, ele pode somar números ou concatenar strings, exercendo duas funções diferentes.


import math

a = 123;

b = 12.123;

d= a+b

c = "Estou praticando tipagem";
e = "Agora";

f = c+e

teste = False
teste2 = False

Pi = math.pi


if teste==True:
    print('teste bobo')

elif(teste==False):
    print('teste bobo faslo')

else:
    print(Pi)


print("A soma de a+b é igual a:", a+b);
print("A tipagem de a é:", type(a));
print("A tipagem de b é:", type(b));
print("A tipagem de c é:", type(c));
print("A tipagem de d é:", type(d));

print(f);
print("A tipagem de f é:", type(f));

# coerção ou conversão

Conv = str(teste)
print(type(Conv), Conv)



