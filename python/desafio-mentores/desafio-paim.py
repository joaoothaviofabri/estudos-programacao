from datetime import datetime

def validar_login(tentativa, login):
      return tentativa == login

def registro_txt(login_nome, login_senha):
      registro_horario = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
      
      with open('registro_login.txt', 'a', encoding='utf-8') as f:
            f.write(f"[{registro_horario}] " + "Usuário: " + f"{login_nome}" + "\n")
            f.write(f"[{registro_horario}] " + "Senha: " + f"{login_senha}" + "\n")


registro_tentativa = []
tentativa_valida = tentativa_invalida = 0

cadastro_nome = str(input("Digite seu nome: "))
cadastro_senha = str(input("Crie sua senha: "))
login_usuario = (cadastro_nome, cadastro_senha)

for tentativa in range(5):
      tentativa_nome = str(input("Digite o nome de usuário: "))
      tentativa_senha = str(input("Digite sua senha: "))

      registro_tentativa_txt = (registro_txt(tentativa_nome, tentativa_senha))
      tentativa_login = (tentativa_nome, tentativa_senha)
      registro_tentativa.append(tentativa_login)

      validacao_login = validar_login(tentativa_login, login_usuario)
      if validacao_login:
            print("Login feito com sucesso.")
            tentativa_valida += 1
            break

      elif tentativa_invalida >= 2:
            print("Você tentou muitas vezes. Tente novamente mais tarde.")
            break

      else:
            print("Seu nome ou senha de login são inválidos. Tente novamente.")
            tentativa_invalida += 1

print(f"O total de tentativas de login foram {len(registro_tentativa)}.")
print(f"O total de tentativas válidas foi {tentativa_valida}.")
print(f"O total de tentativas inválidas foi {len(registro_tentativa)}.")
print(f"Todas as tentativas de login foram: {registro_tentativa}")
if tentativa_invalida > 2:
      print(f"Comportamento de login suspeito.")