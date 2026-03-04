login_usuario = {}
tentativa_invalida = 0
suspeito = False

cadastrar_nome = str(input("Digite o seu nome: "))
cadastrar_senha = str(input("Crie sua senha: "))
login_usuario[cadastrar_nome] = cadastrar_senha

for tentativa in range(1, 4):

    tentativa_nome = str(input("Digite seu nome: "))
    tentativa_senha = str(input("Digite sua senha: "))

    if tentativa_nome not in login_usuario:
        print("Não existe nenhuma conta com esse nome de usuário.")
        suspeito = True
        break

    elif login_usuario[tentativa_nome] == tentativa_senha:
        print("Login feito com sucesso.")
        break

    else:
        print("Nome de usuário ou senha inválidos. Tente novamente.")
        tentativa_invalida += 1

    if tentativa_invalida >= 2:
        print("Você tentou muitos vezes. Tente novamente mais tarde.")
        suspeito = True
        break

if suspeito:
    print("Comportamento suspeito detectado.")