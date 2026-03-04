from datetime import datetime
from time import sleep

def existe_cadastro():
      with open('cadastro_usuario.txt', 'r', encoding='utf-8') as f:
            for linha in f:
                  if linha.strip():
                        return True

            return False

def registro_cadastro(nome, senha):
      with open('cadastro_usuario.txt', 'a', encoding='utf-8') as f:
            f.write(nome + ",")
            f.write(senha + "\n")

def validacao_cadastro(nome):
      with open('cadastro_usuario.txt', 'r', encoding='utf-8') as f:
            for linha in f:
                  linha_limpa = linha.strip()
                  if not linha_limpa:
                        continue

                  linha_separacao = linha_limpa.split(",")

                  if nome == linha_separacao[0]:
                        return True

            return False

def validar_login(nome, senha):
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
      registro_horario = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

      with open('registro_login.txt', 'a', encoding='utf-8') as f:
            f.write(f"[{registro_horario}] " + "Usuário: " + f"{login_nome}" + " Senha: " + f"{login_senha}" + "\n")

if __name__ == "__main__":

      while True:

            open('cadastro_usuario.txt', 'a', encoding='utf-8')
            open('registro_login.txt', 'a', encoding='utf-8')

            print("-" * 20)
            print("[ 1 ] Cadastrar")
            print("[ 2 ] Login")
            print("[ 3 ] Sair")
            print("-" * 20)

            opcao_usuario = int(input("Escolha uma opção: "))
            print("-" * 20)

            if opcao_usuario == 1:
                  cadastro_nome = str(input("Digite seu nome: ")).strip()
                  cadastro_senha = str(input("Crie sua senha: ")).strip()
                  print("-" * 20)

                  validar_cadastro = validacao_cadastro(cadastro_nome)
                  if validar_cadastro:
                        print("ERRO!!!")
                        print("Esse nome de usuário já foi utilizado por outro usuário!")

                  else:
                        registro_cadastro(cadastro_nome, cadastro_senha)
                        print("Conta criada.")

            elif opcao_usuario == 2:

                  if not existe_cadastro():
                        print("Não existe nenhuma cadastro no banco de dados ainda.")
                        print("Faça um cadastro primeiro.")
                        print("-" * 20)
                        continue

                  login_sucesso = False

                  for tentativa in range(1, 4):
                        tentativa_nome = str(input("Digite seu nome de usuario: ")).strip()
                        tentativa_senha = str(input("Digite sua senha: ")).strip()
                        registro_login(tentativa_nome, tentativa_senha)
                        print("-" * 20)

                        validacao_login = validar_login(tentativa_nome, tentativa_senha)
                        if validacao_login:
                              print("Login feito com sucesso.")
                              login_sucesso = True
                              print("-" * 20)
                              break

                        elif tentativa >= 3:
                              print("Você tentou muitas vezes. Tente novamente mais tarde. (Bloqueado por 15 segundos.)")
                              sleep(15)
                              break

                        else:
                              print("Seu nome ou senha de usuário não são válidos. Tente novamente.")
                              print("-" * 20)

                  if login_sucesso:
                        break

            elif opcao_usuario == 3:
                  print("Programa Encerrado.")
                  print("-" * 20)
                  break