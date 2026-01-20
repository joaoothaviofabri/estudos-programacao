def validar_login(tentativa, login):
      return tentativa == login

registro_login = []
login_valido =login_invalido = 0

cadastro_usuario = str(input("Digite o nome de usuário: "))
cadastro_senha = str(input("Crie sua senha: "))
login_usuario = (cadastro_usuario, cadastro_senha)

for tentativa in range(3):
      tentativa_usuario = str(input("Digite o nome de usuário: "))
      tentativa_senha = str(input("Digite sua senha: "))

      login = (tentativa_usuario, tentativa_senha)
      registro_login.append(login)

      validacao_login = validar_login(login, login_usuario)
      if validacao_login:
            print("Login feito com sucesso.")
            login_valido += 1
            break

      elif login_invalido >= 2:
            print("Você tentou muitas vezes. Tente novamente mais tarde.")
            break

      else:
            print("Seu nome ou senha estão errado. Tente novamente.")
            login_invalido += 1

print("-" * 20)
print(f"Houveram {len(registro_login)} tentativas de login.")
print(f"{login_valido} tentativas de login válidas.")
print(f"{login_invalido} tentativas de login inválidos.")
print(f"As tentativas de login foram: {registro_login}")

if login_invalido >= 3:
      print(f"Comportamento suspeito")