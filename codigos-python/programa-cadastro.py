#------------------------------- Variáreis Globais -----------------------------------
li_funcionarios = [] #Lista de funcioarios
id_funcionario = 0
#-------------------------------------------------------------------------------------

#------------------------------ Cadastrar funcionario --------------------------------
def cadastrar_funcionario(id):
  print('*'*70)
  print('-'*20, ' Menu Cadastrar Funcionário ', '-'*20)
  print('ID do funcioário {}'.format(id))
  nome = input('Por favor entre com o NOME: ')
  setor = input('Por favor entre com o SETOR: ')
  salario = float(input('Por favor entre com o SÁLARIO (R$): '))
  dic_funcionario = {'id' : id,               #Dicionario funcionário
                     'nome' : nome,
                     'setor' : setor,
                     'salario' : salario}
  li_funcionarios.append(dic_funcionario.copy())
#-------------------------------------------------------------------------------------

#------------------------------ Consultar funcionario --------------------------------
def consultar_funcionarios():
  while True:
    print('*'*70)
    print('-'*20, ' Menu Consultar Funcionário ', '-'*20)
    menu_consultar = input('Escolha a opção desejada:\n' +
                          '1. Consultar Todos os Funcionários\n' +
                          '2. Consultar Funcionário por Id\n' +
                          '3. Consultar Funcionário(s) por Setor\n' +
                          '4. Retornar\n' +
                          '>> ')
    if menu_consultar == '1':
      print('-'*21, ' Funcionários Cadastrados ', '-'*22)
      for funcionario in li_funcionarios: #funcionario vai varrer toda a lista de funcionários
        print('-'*70)
        for key, value in funcionario.items():  #varrer todos os cojuntos key e value do dicionario funcionario
          print('{}: {}'.format(key, value))
        print('-'*70)
    elif menu_consultar == '2':
      print('-'*21, ' Buscar Funcionários por ID ', '-'*21)
      busca = int(input('Digite o ID do funcionário: '))
      for funcionario in li_funcionarios:
        if funcionario['id'] == busca: #Verifica se no campo codigo do dicionario tem o valor igual ao id de busca
          print('-'*70)
          for key, value in funcionario.items():  #varrer todos os cojuntos key e value do dicionario funcionario
            print('{}: {}'.format(key, value))
          print('-'*70)
    elif menu_consultar == '3':
      print('-'*20, ' Buscar Funcionários por Setor ', '-'*20)
      busca = input('Digite o SETOR do(s) funcionário(s): ')
      for funcionario in li_funcionarios:
        if funcionario['setor'] == busca: #Verifica se no campo codigo do dicionario tem o valor igual ao id de busca
          print('-'*70)
          for key, value in funcionario.items():  #varrer todos os cojuntos key e value do dicionario funcionario
            print('{}: {}'.format(key, value))
          print('-'*70)
    elif menu_consultar == '4':
      return #Sai da função consultar e volta para o programa principal
    else:
      print('!!!!! Opção inválida !!!!!')
      continue
#-------------------------------------------------------------------------------------

#------------------------------- Remover funcionario ---------------------------------
def remover_funcionario():
  print('-'*24, ' Remover Funcionários ', '-'*24)
  remover = int(input('Digite o ID do funcionário a ser removido: '))
  for funcionario in li_funcionarios:
    if funcionario['id'] == remover:
      li_funcionarios.remove(funcionario)
      print('Funcionário Removido')
#-------------------------------------------------------------------------------------

#--------------------------- Incio do programa principal -----------------------------
print('Bem-Vindo ao controle de funcionarios do Mario Rodrigues Reis Oliveira')
while True:
  print('*'*70)
  print('-'*26, ' Menu Principal ', '-'*26)
  menu_principal = input('Escolha a opção desejada:\n' +
                         '1. Cadastrar Funcionário\n' +
                         '2. Consultar Funcionário(s)\n' +
                         '3. Remover Funcionário\n' +
                         '4. Sair\n' +
                         '>> ')
  if menu_principal == '1':
    id_funcionario = id_funcionario + 1
    cadastrar_funcionario(id_funcionario)
  elif menu_principal =='2':
    consultar_funcionarios()
  elif menu_principal =='3':
    remover_funcionario()
  elif menu_principal =='4':
    break #Encerra o programa
  else:
    print('!!!!! Opção inválida !!!!!')
    continue