def validacao_login(tentativa, login):
      return tentativa == login

login_invalido = 0

registro_usuario = str(input("Digite o nome de usuário: "))
registro_senha = str(input("Crie sua senha: "))

login_usuario = (registro_usuario, registro_senha)

for tentativa in range(0, 5):
      print("-" * 20)
      login_nome = str(input("Digite o nome de usuário: "))
      login_senha = str(input("Digite sua senha: "))
      tentativa_login = (login_nome, login_senha)

      validacao = validacao_login(tentativa_login, login_usuario)
      if validacao:
            print("Login feito com sucesso.")
            break

      elif login_invalido >= 3:
            print("Suas tentativas de login acabaram! Tente novamente mais tarde.")
            break

      else:
            print("O nome ou senha de login não são validos, tente novamente.")
            login_invalido += 1

print("-" * 20)
print("Programa encerrado")
print("-" * 20)