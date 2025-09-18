#importando as funções
from funcoes import menu, create, read, update, delete, saudacao

#saudação, por fins de estetica
saudacao()

#laço de repetição para o menu e opções
while True:
    match menu():
        case 1:
            create()
        case 2:
            read()
        case 3:
            update()
        case 4:
            delete()
        case 5:
            input('Saindo do sistema... ')
            break
        case _:
            input('Selecione uma opção ')

SystemExit(print(f'Até a proxima.'))