def validar_login(nome, senha, login):
    return login.get(nome) == senha 

contas = {}
registro_tentativas = []
tentativa_valida = tentativa_invalida = 0

for cadastro_conta in range(2):
    cadastro_nome = str(input("Digite o seu nome: "))
    cadastro_senha = str(input("Crie sua senha: "))
    contas[cadastro_nome] = cadastro_senha

for login in range(5):
    tentativa_nome = str(input("Digite o seu nome de usuário: "))
    tentativa_senha = str(input("Digite sua senha: "))
    tentativa_login_tupla = (tentativa_nome, tentativa_senha)
    registro_tentativas.append(tentativa_login_tupla)

    validacao_login = validar_login(tentativa_nome, tentativa_senha, contas)
    if validacao_login:
        print("Login feito com sucesso.")
        tentativa_valida += 1
        break

    elif tentativa_invalida >= 3:
        print("Você tentou muitas vezes. Tente novamente mais tarde.")
        break

    else:
        print("Seu nome ou senha de login não são válidos. Tente novamente.")
        tentativa_invalida += 1

print(f"O quantidade total de tentativas de login foi {len(registro_tentativas)} tentativas.")
print(f"A quantidade de tentativas válidas foi {tentativa_valida}.")
print(f"A quantidade de tentativas inválidas foi {tentativa_invalida}.")
print(f"As tentativas de login foram: {registro_tentativas}.")
if tentativa_invalida >= 3:
    print("Comportamento suspeito.")