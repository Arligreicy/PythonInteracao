import datetime

# Função para obter uma saudação baseada na hora do dia
def obter_saudacao():
    hora_atual = datetime.datetime.now().hour
    if hora_atual < 12:
        return "Bom dia"
    elif hora_atual < 18:

        
        return "Boa tarde"
    else:
        return "Boa noite"

# Programa que interage com o usuário e aplica regras de comparação

# Solicitar o nome do usuário
nome = input("Digite seu nome: ")

# Validar a entrada da idade
while True:
    try:
        idade = int(input("Digite sua idade: "))
        if idade < 0:
            print("Por favor, insira uma idade válida (não negativa).")
        else:
            break
    except ValueError:
        print("Por favor, insira um número inteiro válido.")

# Exibir mensagem com nome e idade
print(f"{obter_saudacao()}, {nome}. Você tem {idade} anos de idade.")

# Aplicar regras de comparação para determinar a categoria etária
if idade < 18:
    print("Você é um menor de idade.")
elif idade < 65:
    print("Você é um adulto.")
else:
    print("Você é um idoso.")

# Mensagem de despedida
print("Obrigado por interagir! Tenha um ótimo dia!")
