import random
from palavras import palavras
import string

def obter_palavras_validas(palavras):
    palavra = random.choice(palavras)
    while '-' in palavra or ' ' in palavra:
        palavra = random.choice(palavras)

    return palavra.upper()

def forca():
    palavra = obter_palavras_validas(palavras)
    letra_palavra = set(palavra)
    alfabeto = set(string.ascii_uppercase)
    letras_usadas = set()

    lives = 7

    while len(letra_palavra) > 0 and lives > 0:
        print('Você tem', lives, 'vidas restantes e usou estas letras: ', ' '.join(letras_usadas))

        lista_palavras = [letra if letra in letras_usadas else '-' for letra in palavra]
        print('Palavra atual: ', ' '.join(lista_palavras))

        letra_usuario = input('Adivinhe uma letra: ').upper()

        if letra_usuario in alfabeto - letras_usadas:
            letras_usadas.add(letra_usuario)
            if letra_usuario in letra_palavra:
                letra_palavra.remove(letra_usuario)
            else:
                lives -= 1
                print('\nSua letra,', letra_usuario, 'não está na palavra.')

        elif letra_usuario in letras_usadas:
            print('\nVocê já usou essa letra. Tente outra.')

        else:
            print('\nIsso não é uma letra válida. Tente novamente.')

    if lives == 0:
        print('Você perdeu. A palavra era', palavra)
    else:
        print('Parabéns! Você adivinhou a palavra', palavra, '!!')

if __name__ == '__main__':
    forca()
