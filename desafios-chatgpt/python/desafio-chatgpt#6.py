login_usuario = {}
tentativa_login = {}
tentativa_invalida = 0

cadastrar_nome = str(input("Digite o seu nome: "))
cadastrar_senha = str(input("Crie sua senha: "))
login_usuario[cadastrar_nome] = cadastrar_senha

for tentativa in range(4):
    tentativa_nome = str(input("Digite seu nome: "))
    tentativa_senha = str(input("Digite sua senha: "))

    tentativa_login[tentativa_nome] = tentativa_login.get(tentativa_nome, 0) + 1

    if tentativa_nome not in login_usuario:
        print("Esse usuário não existe.")
        tentativa_invalida += 1

    elif login_usuario[tentativa_nome] == tentativa_senha:
        print("Login feito com sucesso.")
        break

    else:
        print("Seu nome ou senha de usuários não são válidas. Tente novamente.")
        tentativa_invalida += 1

    if tentativa_invalida >= 3:
        print("Você tentou muitas vezes. Tente novamente mais tarde.")
        break

print(f"Essas é a quantidade de registro de tentativas de login: {tentativa_login}")