def validar_login(tentativa, login):
      return tentativa == login

def registro_cadastro(nome, senha):
      with open('cadastro_usuario.txt', 'a', encoding='utf-8') as f:
            f.write(nome, senha, "\n")

def validacao_cadastro(nome, senha):
      with open('cadastro_usuario.txt', 'r', encoding='utf-8') as f:
            for linha in f:
                  linha_limpa = linha.strip()
                  if not linha_limpa:
                        continue

                  linha_separacao = linha_limpa.split(",")

                  if nome == linha_separacao[0] and senha == linha_separacao[1]:
                        return True

            return False

def registro_login(login_nome, login_senha):
      with open('registro_login.txt', 'a', encoding='utf-8') as f:
            f.write(login_nome, login_senha,"\n")

while True:
      print("-" * 20)
      print("[ 1 ] Cadastrar")
      print("[ 2 ] Login")
      print("[ 3 ] Sair")
      print("-" * 20)

      opcao_usuario = int(input())

      if opcao_usuario == 1:
            cadastro_nome = str(input("\nDigite seu nome: "))
            cadastro_senha = str(input("Crie sua senha: "))
            login_usuario = (cadastro_nome, cadastro_senha)
            registro_cadastro(cadastro_nome, cadastro_senha)
            print("\nConta criada.")

      elif opcao_usuario == 2:
            for tentativa in range(1, 5):
                  tentativa_nome = str(input("Digite seu nome de usuario: "))
                  tentativa_senha = str(input("Digite sua senha: "))

                  registro_login(tentativa_nome, tentativa_senha)
                  tentativa_login = (tentativa_nome, tentativa_senha)

                  validacao_login = validacao_cadastro(tentativa_nome, tentativa_senha)
                  if validacao_login:
                        print("Login feito com sucesso.")
                        break

                  elif tentativa > 3:
                        print("Você tentou muitas vezes. Tente novamente mais tarde.")
                        break

                  else:
                        print("Seu nome ou senha de usuário não são válidos. Tente novamente.")
      elif opcao_usuario == 3:
            break

print("Programa Encerrado.")