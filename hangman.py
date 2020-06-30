import random


# seleccionador de palabra ---------------------------------------

def select_word (words):
    random.shuffle(words)
    word=[c for c in words[0]]
    return(word)

# seleccionador de palabra ---------------------------------------


# creador de blanks ------------------------------------

def underscores (word):
    blanks= "_"*len(word)
    blanks=[i for i in blanks]
    return blanks

# creador de blanks ------------------------------------

# va haciendo el blank con letras -----------------------------

def show (word,blanks,correct_letters):   
    for i in range(len(word)):
        if word[i] in correct_letters:
            blanks[i]=word[i]
    x=" ".join(blanks)
    print(x)         

# va haciendo el blank con letras -----------------------------
        
pictures =[    ( """


         ___________   
        |          |
        |          
        |          
        |         
        /\\
                         """), 

( """


         ___________   
        |          |
        |          O
        |          
        |         
        /\\
                         """),( """


         ___________   
        |          |
        |          O
        |          |
        |         
        /\\
                         """) ,      ( """


         ___________   
        |          |
        |          O
        |         /|
        |         
        /\\
                         """),    ( """


         ___________   
        |          |
        |          O
        |         /|\ 
        |         
        /\\
                         """) ,    ( """


         ___________   
        |          |
        |          O
        |         /|\ 
        |         / 
        /\\
                         """) ,   ( """


         ___________   
        |          |
        |          O
        |         /|\ 
        |         / \\
        /\\
                         """) ]                                                                        
            
  