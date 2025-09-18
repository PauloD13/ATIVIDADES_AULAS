
from funcoes import menu, create, read, update, delete, saudacao

saudacao()

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
            input('Saindo do sistema...')
            break
        case _:
            print('Selecione uma opção')

SystemExit(print(f'Até a proxima.'))