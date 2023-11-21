def hangmanError(guesses: int):
    stages = [
        """
           --------
           |      |
           |      O
           |     \|/
           |      |
           |     / \
           -
        """,
        """
           --------
           |      |
           |      O
           |     \|/
           |      |
           |     / 
           -
        """,
        """
           --------
           |      |
           |      O
           |     \|/
           |      |
           |      
           -
        """,
        """
           --------
           |      |
           |      O
           |     \|
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |    
           |    
           |     
           -
        """,
        """
           --------
           |      |
           |      
           |    
           |    
           |     
           -
        """
    ]
    return stages[guesses]

guess = 6

import getpass
movieName = (getpass.getpass("Movie Name: ")).lower()

filler = []
provided = set()
for a in movieName.split():
    [filler.append('_') for _ in a], filler.append(' ')
filler.pop(-1)
print(''.join(filler))

print(hangmanError(guess))
while(guess!=0):
    rs = (input("Enter the value: ")[0]).lower()
    if rs in movieName:
        if rs in provided:
            print("You already given that value.")
        else:
            provided.add(rs)
            value = [int(i) for i, letter in enumerate(movieName) if letter == rs]
            if value:
                for i in value:
                    filler[i]=rs
            else:
                print("You have to provide input.")
    else:
        guess-=1
        print(hangmanError(guess))
    if ''.join(filler) == movieName:
        print(f"You have successfully guessed the movie name: {movieName}")
        exit()
    else:
        print(f"Filled: {''.join(filler)}\nProvided Values: {','.join(provided)}")
