#------------------------------ Função metragem_limpeza() --------------------------------
def metragem_limpeza():
  print('*'*86)
  print('-'*25,' Menu 1 de 3 - ','Metragem Limpeza','-'*27)
  while True:
    try:
      metragemL = float(input('Entre com a metragem da casa (m²): ')) #Como não há exigencias para que seja tipo int, coloquei float para aceitar valores com casas decimais
      if (metragemL >= 30) and (metragemL < 300):
        print('É necessário contratar 1 pessoa')
        return 60 + 0.3 * metragemL
      elif(metragemL >= 300) and (metragemL < 700):
        print('É necessário contratar 2 pessoas')
        return 120 + 0.5 * metragemL
      else:
        print('!! Não aceitamos casas com metragem menor que 30m² ou maior que 700m² !!')
    except ValueError: #Caso o usuário 
      print('!! Por favor entrar com numeros inteiros !!')
#----------------------------------------------------------------------------------------

#-------------------------------- Função tipo_limpeza() ---------------------------------
def tipo_limpeza():
  print('*'*86)
  print('-'*25,' Menu 2 de 3 - ','Tipo de Limpeza','-'*28)
  while True:
    opcaoL = input('Entre com o tipo de limpeza: \n' +
                   'B – Básica - Indicada para sujeiras semanais ou quinzenais \n' +
                   'C – Completa - Indicada para sujeiras antigas e/ou não rotineiras \n' +
                   '>>')
    opcaoL = opcaoL.upper()
    if (opcaoL == 'B'):
      print('Você selecionou a limpeza BÁSICA')
      return 1.00
    elif (opcaoL == 'C'):
      print('Você selecionou a limpeza COMPLETA')
      return 1.30
    else:
      print('!!!!!!!  Opção Inválida  !!!!!!!')
      continue #Retorna para o inicio do laço

#----------------------------------------------------------------------------------------

#------------------------------ Função adicional_limpeza() ------------------------------
def adicional_limpeza():
  print('*'*86)
  print('-'*25,' Menu 3 de 3 - ','Adicional de Limpeza','-'*23)
  acumular = 0
  while True:
    adicionalL = input('0- Não desejo mais nada (encerrar) \n' +
                       '1- Passar 10 peças de roupas - R$ 10.00 \n' +
                       '2- Limpeza de 1 Forno/Micro-ondas - R$ 12,00 \n' +
                       '3- Limpeza de 1 Geladeira/Freezer - R$ 20,00 \n' +
                       '>>')
    if (adicionalL == '0'):
      return acumular
    elif (adicionalL == '1'):
      acumular = acumular + 10
      continue #volta ao inicio do laço
    elif (adicionalL == '2'):
      acumular = acumular + 12
      continue #volta ao inicio do laço
    elif (adicionalL == '3'):
      acumular = acumular + 20
      continue #volta ao inicio do laço
    else:
      print('!!!!!!!  Opção Inválida  !!!!!!!')
#----------------------------------------------------------------------------------------

#Incio do programa principal
print('Bem-Vindo ao programa de serviços de Limpeza do Mario Rodrigues Reis Oliveira')
metragem = metragem_limpeza()
tipo = tipo_limpeza()
adicional = adicional_limpeza()
total = (metragem * tipo) + adicional
print('TOTAL: R$ {:.2f} (metragem: {:.2f}m² * tipo: {:.2f} + adicional: {:.2f})'.format(total, metragem, tipo, adicional))