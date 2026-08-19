co = float(input('Digite o valor do cateto oposto: '))

ca = float(input('Digite o valor do cateto adjacente: '))

hipo = float (input('Por fim, informe o valor da hipotenusa: '))

seno = co / hipo
cos = ca / hipo
tang = co / ca

print(f'Valor seno: {seno}')
print(f'Valor cosseno: {cos}')
print(f'Valor tangente: {tang}')

