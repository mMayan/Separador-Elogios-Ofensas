import re

good_words = ['lindo', 'linda', 'bonito', 'bonita', 'maravilhoso', 'maravilhosa', 'incrível', 'fantástico', 'fantástica', 'espetacular', 'genial', 'sensacional', 'admirável', 'fantabuloso', 'fantabulosa', 'bravo', 'excepcional', 'gostoso', 'gostosa', 'gosto', 'gato', 'gata', 'gatinho', 'gatinha']
bad_words = ['caralho', 'porra', 'puta', 'pariu', 'merda', 'cu', 'foder', 'fuder', 'viado', 'cacete', 'odeio', 'ódio', 'feio', 'foda-se', 'fodase', 'desgraçado', 'desgraçada']

while True:
    msg = str(input("digite a mensagem: "))
    splitted = re.split(r'[ ,]', msg)

    for word in splitted:
        if word in good_words:
            with open('elogios.txt', 'a') as file:
                file.write(msg + '\n')
                break 
    
        elif word in bad_words:
            with open('ofensas.txt', 'a') as file:
                file.write(msg + '\n')
                break




#dar um jeito de fazer com que o código apague os arquivos de texto quando eu quiser com a palavra "apagar"
#eventualmente botar isso num GUI
#se fizer um elogio com palavrão ele não vai saber detectar direito, corrigir isso






