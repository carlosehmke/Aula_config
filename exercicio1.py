#import datetime #biblioteca para trabalhar com datas.
from datetime import date

nome = "Carlos"
sobrenome = "Ehmke"
ano_nascimento = 1995
#ano_atual = datetime.date.today().year #função que pega o ano atual.
ano_atual = date.today().year #função que pega o ano atual.
idade = ano_atual-ano_nascimento
altura_metros = 1.78
maior_de_idade = idade >= 18

print('Nome:', nome)
print('Sobrenome:', sobrenome)
print('Idade:', idade)
print('Ano de nascimento:', ano_nascimento)
print('é maior de idade?:', maior_de_idade)
print('Altura em metros:', altura_metros)
