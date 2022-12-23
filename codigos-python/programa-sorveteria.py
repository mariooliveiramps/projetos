print('Bem-Vindo a Sorveteria do Mario Rodrigues Reis Oliveira')
print('-'*44 + 'Cardápio' + '-'*44)
print('| ' + 'Código' + ' | ' + 'Descrição' + '            | ' + 'Tamanho P (500ml)' + ' | ' + 'Tamanho M (1000ml)' + ' | ' + 'Tamanho G (2000ml)' + '  |')
print('|   ' + 'TR' + '   | ' + 'Sabores Tradicionais' + ' | ' + 'R$ 6,00' + '           | ' + 'R$ 10,00' + '           | ' + 'R$ 18,00' + '            |')
print('|   ' + 'ES' + '   | ' + 'Sabores Especiais' + '    | ' + 'R$ 7,00' + '           | ' + 'R$ 12,00' + '           | ' + 'R$ 21,00' + '            |')
print('|   ' + 'PR' + '   | ' + 'Sabores Premium' + '      | ' + 'R$ 8,00' + '           | ' + 'R$ 14,00' + '           | ' + 'R$ 24,00' + '            |')
print('-'*96)
valorFinal = 0
while True:
  tamanho = input('Entre com o TAMANHO do pote desejada (P/M/G): ')
  tamanho = tamanho.upper() #Reconhecerá a entrada independente de digitar maiusculo ou minusculo
  if (tamanho != 'P') and (tamanho != 'M') and (tamanho != 'G'):
    print('!!!!!!!  TAMANHO INVÁLIDO  !!!!!!!')
    continue #Ao digitar um valor inválido recomeça o while

  codigo = input('Entre com o CÓDIGO do sabor desejado (TR/ES/PR): ')
  codigo = codigo.upper() #Reconhecerá a entrada independente de digitar maiusculo ou minusculo
  if (codigo != 'TR') and (codigo != 'ES') and (codigo != 'PR'):
    print('!!!!!!!  CÓDIGO INVÁLIDO  !!!!!!!')
    continue #Ao digitar um valor inválido recomeça o while

#Opções tamanho P
  if (tamanho == 'P') and (codigo == 'TR'):
    print('Você pediu um sorvete sabor TRADICIONAL P de R$ 6,00')
    valorFinal = valorFinal + 6 #O valor anterior é somado com 6, que é R$ 6,00

  elif (tamanho == 'P') and (codigo == 'ES'):
    print('Você pediu um sorvete sabor TRADICIONAL P de R$ 7,00')
    valorFinal = valorFinal + 7 #O valor anterior é somado com 7, que é R$ 7,00

  elif (tamanho == 'P') and (codigo == 'PR'):
    print('Você pediu um sorvete sabor TRADICIONAL P de R$ 8,00')
    valorFinal = valorFinal + 8 #O valor anterior é somado com 8, que é R$ 8,00

#Opções tamanho M
  if (tamanho == 'M') and (codigo == 'TR'):
    print('Você pediu um sorvete sabor ESPECIAL M de R$ 10,00')
    valorFinal = valorFinal + 10 #O valor anterior é somado com 10, que é R$ 10,00

  elif (tamanho == 'M') and (codigo == 'ES'):
    print('Você pediu um sorvete sabor ESPECIAL M de R$ 12,00')
    valorFinal = valorFinal + 12 #O valor anterior é somado com 12, que é R$ 12,00

  elif (tamanho == 'M') and (codigo == 'PR'):
    print('Você pediu um sorvete sabor ESPECIAL M de R$ 14,00')
    valorFinal = valorFinal + 14 #O valor anterior é somado com 14, que é R$ 14,00

#Opções tamanho G
  if (tamanho == 'G') and (codigo == 'TR'):
    print('Você pediu um sorvete sabor PREMIUM G de R$ 18,00')
    valorFinal = valorFinal + 18 #O valor anterior é somado com 18, que é R$ 18,00

  elif (tamanho == 'G') and (codigo == 'ES'):
    print('Você pediu um sorvete sabor PREMIUM G de R$ 21,00')
    valorFinal = valorFinal + 21 #O valor anterior é somado com 21, que é R$ 21,00

  elif (tamanho == 'G') and (codigo == 'PR'):
    print('Você pediu um sorvete sabor PREMIUM G de R$ 24,00')
    valorFinal = valorFinal + 24 #O valor anterior é somado com 24, que é R$ 24,00

  print('-'*54)
  outroPedido = input('Deseja pedir mais alguma coisa? (S/N): ')
  outroPedido = outroPedido.upper()
  if (outroPedido == 'S'):
    continue
  else:
    print('O total a ser pago é: R$ {:.2f}'.format(valorFinal))
    break #Aqui encerra o while