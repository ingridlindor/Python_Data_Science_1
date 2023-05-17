# Lista de desafios da aula 2

# COLETA E AMONSTRAGEM DE DADOS
print ('EX 1. Crie um programa que solicite à pessoa usuária digitar seu nome, e imprima “Olá, [NOME]!”')
nome=input ('Digite seu nome: ')
print (f'ola {nome}')

print('EX 2.Crie um programa que solicite à pessoa usuária digitar seu nome e idade, e imprima “Olá, [nome], você tem [idade] anos.”.')
nome=input('Digite seu nome: ')
idade=input("Digite a sua idade: ")
print(f'Olá,{nome} voce tem {idade} anos!')

print('EX 3.Crie um programa que solicite à pessoa usuária digitar seu nome, idade e altura em metros, e imprima “Olá, [nome], você tem [idade] anos e mede [altura] metros!”.')
nome=input('Digite seu nome: ')
idade=input("Digite a sua idade: ")
altura=input('Digite sua altura: ')
print(f'Olá {nome} voce tem {idade} anos e {altura} metros!')

# CALCULADORA COM OPERADORES
print('EX 4.Crie um programa que solicite dois valores numéricos à pessoa usuária e imprima a soma dos dois valores.')
n1=int(input('Digite um valor: '))
n2=int(input('Digite outro valor: '))
result= n1+n2
print(f'{n1} + {n2} = {result}')

print('EX 5. Crie um programa que solicite três valores numéricos à pessoa usuária e imprima a soma dos três valores.')
n1=int(input('Digite um valor: '))
n2=int(input('Digite outro valor: '))
n3=int(input('Digite outro valor: '))
result= n1+n2+n3
print(f'{n1} + {n2} + {n3} = {result}')

print('EX 6.Crie um programa que solicite dois valores numéricos à pessoa usuária e imprima a subtração do primeiro pelo o segundo valor.')
n1=int(input('Digite um valor: '))
n2=int(input('Digite outro valor: '))
result= n1-n2
print(f'{n1} - {n2} = {result}')

print('EX 7. Crie um programa que solicite dois valores numéricos à pessoa usuária e imprima a multiplicação dos dois valores.')
n1=int(input('Digite um valor: '))
n2=int(input('Digite outro valor: '))
result= n1 * n2
print(f'{n1} X {n2} = {result}')

print('EX 8. Crie um programa que solicite dois valores numéricos, um numerador e um denominador, e realize a divisão entre os dois valores. Deixe claro que o valor do denominador não pode ser 0.')
num=int(input('Digite um numero'))
den=int(input('Digite outro valor (esse valor NAO pode ser zero):'))
if den == 0:
    print('o segundo valor nao pode ser zero')
else:
    result = num/den
    print(f'{num} / {den} = {result}')
    
print('EX 9.Crie um programa que solicite dois valores numéricos, um operador e uma potência, e realize a exponenciação entre esses dois valores.')
ope=int(input('Digite o operador'))
pot=int(input('Digite a potência:'))

result = ope ** pot
contador=0

print(result)

print('EX 10. Crie um programa que solicite dois valores numéricos, um numerador e um denominador e realize a divisão inteira entre os dois valores. Deixe claro que o valor do denominador não pode ser 0.') 
num=int(input('Digite o numerador:'))
den=int(input('Digite o denominador:'))
if den == 0:
    print(' O segundo valor nao pode ser igual a zero. Por favor tente novamente')

else:
    resto = num / den 

    print(f' A divisão entre {num} e {den} é {resto}')

print('EX 11.Crie um programa que solicite dois valores numéricos, um numerador e um denominador, e retorne o resto da divisão entre os dois valores. Deixe claro que o valor do denominador não pode ser 0.')
num=float(input('Digite o numerador:'))
den=float(input('Digite o denominador:'))
if den == 0:
    print(' O segundo valor nao pode ser igual a zero. Por favor tente novamente')

else:
    resto = num % den 

    print(f' o resto da divisão entre {num} e {den} é {resto}')

print('EX 12. Crie um código que solicita 3 notas de um estudante e imprima a média das notas.') 
n1=float(input(' Digite a primeira nota: '))
n2=float(input(' Digite a segunda nota: '))
n3=float(input(' Digite a terceira nota: '))

media = (n1+n2+n3) /3 
media = round(media,2)

print( f'A média entre esses valores é igual a {media}')


print('EX 13. Crie um codigo que receba a media de um aluno e retorne se ele esta aprovado, de recuperaçao ou reprovado')
    #   aprovado media igual 6
    #   recuperacao media entre 6 e 4
    #   reprovado media menor que  4

media = float(input('Digite a média: '))

if media >= 6.0:
  print('O aluno está aprovado')
elif 6.0 > media >= 4.0:
  print(' O aluno está de Recuperação')
else:
  print('O aluno está Reprovado')

print('EX 14. Crie um código que calcule e imprima a média ponderada dos números 5, 12, 20 e 15 com pesos respectivamente iguais a 1, 2, 3 e 4.')
notas = [5, 12, 20, 15]
pesos = [1, 2, 3, 4]

# Verificar se o número de notas é igual ao número de pesos
if len(notas) != len(pesos):
    print("Error: O número de notas e pesos não é o mesmo.")
else:
    soma_notas = sum([nota * peso for nota, peso in zip(notas, pesos)])
    
    soma_pesos = sum(pesos)
    media_ponderada = soma_notas / soma_pesos

    print(f"A média ponderada é igual a {media_ponderada}")


# EDITANDO TEXTOS

print('EX 15. Crie uma variável chamada “frase” e atribua a ela uma string de sua escolha. Em seguida, imprima a frase na tela.')

frase= "é bom tanto estudo me dar algum resultado la na frente na moral nao aguento mais"
print(frase)

print('EX 16. Crie um código que solicite uma frase e depois imprima a frase na tela.')
frase = input(str('Escreva uma frase: '))
print(frase)

print('EX 17. Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase digitada mas com todas as letras maiúsculas.')
frase = input(str('Escreva uma frase: '))
frase_n = frase.upper()
print(frase_n)


print('EX 18.Crie uma variável chamada “frase” e atribua a ela uma string de sua escolha. Em seguida, imprima a frase sem espaços em branco no início e no fim.')
frase = " Deus é fiel "
frase_n =frase.strip()
print(frase_n)

print('EX 19.Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase sem espaços em branco no início e no fim.')
frase = input(str('Escreva uma frase: '))
frase_n =frase.strip()
print(frase_n)


print('EX 20. Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase sem espaços em branco no início e no fim e em letras minúsculas.')
frase = input(str('Escreva uma frase: '))
frase_n =frase.strip()
frase_n= frase_n.upper()
print(frase_n)



print('EX 21. Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase com todas as vogais “e” trocadas pela letra “f”.')
frase = input(str('Escreva uma frase: '))
frase_n =frase.replace("e","f")
print(frase_n)

print('EX 22. Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase com todas as vogais “a” trocadas pela caractere “@”.')
frase = input(str('Escreva uma frase: '))
frase_n =frase.replace("a","@")
print(frase_n)

print('EX 23. Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase com todas as consoantes “s” trocadas pelo caractere “$”.')
frase = input(str('Escreva uma frase: '))
frase_n =frase.replace("s","$")
print(frase_n)
