import hangman

words=[ "caballo","perro","raton","hamburguesa","asado","azul","rojo","gris","serpiente","hipopotamo","cocodrilo"]
correct_letters=[]
wrong_letters=[]
word=hangman.select_word (words)
word=[i for i in word]
blanks=(hangman.underscores(word))


while len(wrong_letters) < 6 :

    if len(wrong_letters)==0 and len(correct_letters)==0:
        print( f"""

        Bienvenido al Ahorcado ! !!!

- Tu paralabra tiene  {len(word)} Letras

 {" _ "*len(word)}

 """)

    print( f"Wrong Letters: {wrong_letters}")

    guess=input("""

Adivina la letra :  """

         )

    if  guess.isalpha():
        guess=guess.lower().strip()
        print("´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´",)
        if guess in word:
            correct_letters.append(guess)
            print(f"CORRECTO ! La letra {guess} esta en tu palabra !")
        else:
            wrong_letters.append(guess)
            print(" Esta letra no esta en tu palabra ! !")

    else:
        print(" Solo puedes ingresar letras")

    hangman.show(word,blanks,correct_letters)

    if len (wrong_letters)>0:
        print (hangman.pictures[len(wrong_letters)])

    if len(wrong_letters) == 6:
        print( f"Perdiste !! tu palabra era {word}")

    elif blanks== word:
        print (" EN HORA BUENA ! GANASTE !")
        break
