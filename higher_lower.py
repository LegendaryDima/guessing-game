import random

game_on = None

guesses = None

secret = None

def difficulty_level_easy():
    global secret
    global game_on
    secret = int(random.randrange(0,100))
    while game_on:
        guess = int(input('Guess a number from 1 to 100. '))
        if guess > secret:
            print('your guess is too high. Try again.')
        elif guess < secret:
            print('your guess is too low. Try again.')
        elif guess == secret:
            print('You win!')
            play_again()

def difficulty_level_hard():
    global guesses
    global secret
    guesses = 3
    secret = int(random.randrange(0,100))
    for i in range(guesses + 1):
        if i == guesses:
            print('Game over, too many guesses.')
            break
        else: 
        guess = int(input('Guess a number from 1 to 100. '))
            if guess > secret:
                print('Your guess is too high. Try again.')
            elif guess < secret:
                print('Your guess is too low. Try again.')
            else:
                print('You win!')
                break
    play_again()
    
def start_game():
    global game_on
    game_on = True
    level = input('Welcome. Type easy, hard, or quit. ')
    if level == 'easy':
        difficulty_level_easy()
    elif level == 'hard':
        difficulty_level_hard()
    elif level == 'quit':
        game_on = False
        
def play_again():
    global game_on
    game_on = True      
    play = input('Play again? Yes or No. ')
    if play == 'yes':  
        start_game()
    else:     
        game_on = False
        print('Thanks for playing. :)')
        
start_game()
