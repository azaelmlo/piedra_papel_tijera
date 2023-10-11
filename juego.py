import random


print('hola, quieres jugar un piedra papel o tijeras y apostar unos creditos, ten 300 credito')




options = ('piedra', 'papel', 'tijera')
rounds = 1

credit = 300
apuesta = 0
intentos = 0

res_cont = 'no'


while credit > 0:

    if intentos > 4:
        print('vuelve cuando quieras jugar')
        break

    if res_cont == 'si':
        break

    apuesta = int(input('¿Cúantos creditos quieres apostar? '))

    if apuesta > credit:
        print('no tienes esos creditos para apostar')
        break

    computer_win = 0 
    user_win = 0

    while True: 
        if credit < 0: 
            break

        if intentos > 4: 
            break

        print('*' * 10)
        print('Round ', rounds)
        print('*' * 10)

        print('MARCADOR ', 'Computadora: ', computer_win, ' TU: ', user_win)

        user_option = input('elije piedra papel o tijera: ')
        user_option = user_option.lower()

        rounds += 1

        if not user_option in options:
            print('esa opción no esta permitida')
            intentos += 1
            continue

        computer_option = random.choice(options)

        if user_option == computer_option:
            print('la computadora también elijio ', computer_option)
            print('empate')
        elif user_option == 'piedra':
            if computer_option == 'papel':
                print('la computadora elijio ', computer_option)
                print('pierdes esta')
                computer_win += 1
            else:
                print('la computadora elijio ', computer_option)
                print('ganaste')
                user_win += 1
        elif user_option == 'papel':
            if computer_option == 'piedra':
                print('la computadora elijio ', computer_option)
                print('ganas')
                user_win += 1
            else:
                print('la computadora elijio ', computer_option)
                print('pierdes')
                computer_win += 1
        elif user_option == 'tijera':
            if computer_option == 'piedra':
                print('la computadora elijio ', computer_option)
                print('pierdes')
                computer_win += 1
            else:
                print('la computadora elijio ', computer_option)
                print('ganas')
                user_win += 1
        
        if computer_win == 2:
            print('*' * 10)
            print('LA CASA GANA')
            print('MARCADOR ', 'Computadora: ', computer_win, ' TU: ', user_win)
            credit -= apuesta
            print('Tienes: ', credit)
            computer_win = 0 
            user_win = 0
            continua = input('Abandonas? si / no: ')
            res_cont = continua.lower()
            break
            
            
            

        if user_win == 2:
            print('*' * 10)
            print('GANASTE EL JUEGO')
            print('MARCADOR ', 'Computadora: ', computer_win, ' TU: ', user_win)
            credit += apuesta
            print('Tienes: ', credit)
            computer_win = 0 
            user_win = 0
            computer_win = 0 
            user_win = 0
            continua = input('Abandonas? si / no: ')
            res_cont = continua.lower()
            break 

print('todo acabo')


        
    

    
    
    
            
        
        

 