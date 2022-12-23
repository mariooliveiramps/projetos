print('Bem-vindo a loja do Mario Rodrigues Reis Oliveira')
preco = float(input('Entre com valor do produto: '))
quantidade = int(input('Entre com valor do quantidade: '))

valorFinal = preco * quantidade

if (0 <= quantidade < 11): #quantidade >= 0 and quantidade < 11
  valorComFrete = valorFinal + 30 #Custo do frete de R$30
  print('O valor sem frete foi: R$ {:.2f}'.format(valorFinal))
  print('O valor com frete foi: R$ {:.2f}  (frete de R$ 30)'.format(valorComFrete))
elif (11 <= quantidade < 101): #quantidade >= 11 and quantidade < 101
  valorComFrete = valorFinal + 60 #Custo do frete de R$60
  print('O valor sem frete foi: R$ {:.2f}'.format(valorFinal))
  print('O valor com frete foi: R$ {:.2f}  (frete de R$ 60)'.format(valorComFrete))
elif (101 <= quantidade < 1001): #quantidade >= 101 and quantidade < 1001
  valorComFrete = valorFinal + 120 #Custo do frete de R$120
  print('O valor sem frete foi: R$ {:.2f}'.format(valorFinal))
  print('O valor com frete foi: R$ {:.2f}  (frete de R$ 120)'.format(valorComFrete))
else: #quantidade >= 1001 
  valorComFrete = valorFinal + 240 #Custo do frete de R$240
  print('O valor sem frete foi: R$ {:.2f}'.format(valorFinal))
  print('O valor com frete foi: R$ {:.2f}  (frete de R$ 240)'.format(valorComFrete))