import dearpygui.dearpygui as dpg
import re
import os

def delete_all_files():
    try:
        os.remove('elogios.txt')
        os.remove('ofensas.txt')
    except FileNotFoundError:
        pass

def erase_all_files():
    with open('elogios.txt', 'w') as file:
        file.write('')
    with open('ofensas.txt', 'w') as file:
        file.write('')

good_words = ['lindo', 'linda', 'bonito', 'bonita', 'maravilhoso', 'maravilhosa', 'incrível', 'fantástico', 'fantástica', 'espetacular', 'genial', 'sensacional', 'admirável', 'fantabuloso', 'fantabulosa', 'bravo', 'excepcional', 'gostoso', 'gostosa', 'gosto', 'gato', 'gata', 'gatinho', 'gatinha']
bad_words = ['caralho', 'porra', 'puta', 'pariu', 'merda', 'cu', 'foder', 'fuder', 'viado', 'cacete', 'odeio', 'ódio', 'feio', 'foda-se', 'fodase', 'desgraçado', 'desgraçada']

while True:
    msg = str(input("digite a mensagem: "))
    splitted = re.split(r'[ ,]', msg)

    if msg == 'sair':
        print('saindo...')
        break

    elif msg == 'apagar':
        delete_all_files()
    
    elif msg == 'limpar':
        erase_all_files()

    for word in splitted:
        if word in good_words:
            with open('elogios.txt', 'a') as file:
                file.write(msg + '\n')
                break 
    
        elif word in bad_words:
            with open('ofensas.txt', 'a') as file:
                file.write(msg + '\n')
                break

#eventualmente botar isso num GUI
#se fizer um elogio com palavrão ele não vai saber detectar direito, corrigir isso
#https://www.geeksforgeeks.org/python-os-remove-method/ - link de onde eu vi a biblioteca os.remove
