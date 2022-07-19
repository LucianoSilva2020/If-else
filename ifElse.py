altura = float(input('Digite a altura do reservatório:'))
largura = float(input('Digite a largura do reservatório:'))
comprimento = float(input('Digite o comprimento do reservatório:'))
consumo = float(input('Digite seu consumo diario em litros:'))
mes = 30
capacidadeTotalEmLitros = altura * largura * comprimento
autonomia = capacidadeTotalEmLitros / mes

print(f'A capacidade total do seu reservatório é de {capacidadeTotalEmLitros}L')
print(f'A autonomia do seu reservatório é de {autonomia}L por dia.')

if consumo > autonomia:
    print('Você ultrapassou seu limite diario.')
elif consumo == autonomia:
    print('Hoje você chegou a seu limite diario, cuidado para não ultrapassa-lo.')
elif consumo <= autonomia:
    print('Parabéns, seu consumo hoje foi moderado')    