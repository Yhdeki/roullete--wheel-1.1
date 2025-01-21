import time
import random
from main import chips
print('Welcome to the roullete game in the Derizino!')
Red = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36,0]
Black = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35,0]
def game_of_roullete():
    global chips
    global Black
    global Red
    while True:
        if chips == 0:
            print('You lost all your chips, goodbye!')
            exit()
        print(f"You have {chips}$")
        bet_of_player = input(f"How much would you like to bet? ")
        try:
            bet_of_player = int(bet_of_player)
        except ValueError:
            print(f"{bet_of_player} is not a number, write a number!")
        if bet_of_player > chips:
            print("You don't have enough money")
        else:
            print("These are the options you can bet on:\n'1 to 12','13 to 24','25 to 36' which means the numbers between them including them\n'odd' or 'even'\na specific number including 0\n'1+3'or '2+3' or '3+3' which means the numbers 1,2,3 and you keep adding 3 until 34,35,36\nred or black\n'1 to 18','19 to 36' which means the numbers between them including them")
            option = input(f"On what option would you like to bet {bet_of_player}$? ")
            chips -= bet_of_player
            choices = [Red, Black]
            spin = random.choice(choices)
            number = random.choice(spin)
            print('Spinning...')
            time.sleep(1.25)
            print('The number is...')
            time.sleep(0.5)
            if number == 0:
                print(number)
            elif number in Red:
                print(f"{number} Red")
            else:
                print(f"{number} Black")
            if option.lower() in ['1 to 12','13 to 24','25 to 36']:
                if option.lower() == '1 to 12':
                    if number in [1,2,3,4,5,6,7,8,9,10,11,12]:
                        print('You were right!')
                        chips += 3 * bet_of_player
                    else:
                        print('You lost')
                elif option.lower() == '13 to 24':
                    if number in [13,14,15,16,17,18,19,20,21,22,23,24]:
                        print('You were right!')
                        chips += 3 * bet_of_player
                    else:
                        print('You lost')
                else:
                    if number in [25,26,27,28,29,30,31,32,33,34,35,36]:
                        print('You were right!')
                        chips += 3 * bet_of_player
                    else:
                        print('You lost')
            elif option.lower() in ['red','black',Red,Black]:
                if option.lower() == 'red':
                    if number == 0:
                        print("You were wrong.")
                    elif number in Red:
                        print("You were right!")
                        chips += 2 * bet_of_player
                    else:
                        print("You were wrong.")
                elif option.lower() == 'black':
                    if number == 0:
                        print("You were wrong.")
                    elif number in Black:
                        print("You were right!")
                        chips += 2 * bet_of_player
                    else:
                        print("You were wrong.")
                elif option.lower() in Red or Black:
                    if number == option:
                        print("No way! You won!")
                        chips += 35 * bet_of_player
                    else:
                        print("You lost.")
            elif option.lower() in ['odd','even']:
                if option.lower() == 'odd':
                    if number % 2 == 1:
                        print('You were right!')
                        chips += 2 * bet_of_player
                    else:
                        print('You lost')
                else:
                    if number % 2 == 0:
                        print('You were right!')
                        chips += 2 * bet_of_player
                    else:
                        print('You lost')
            elif option.lower() in ['1+3','2+3','3+3']:
                if option.lower() == '1+3':
                    if number % 3 == 1:
                        print('You were right!')
                        chips += 3 * bet_of_player
                    else:
                        print('You lost')
                elif option.lower() == '2+3':
                    if number % 3 == 2:
                        print('You were right!')
                        chips += 3 * bet_of_player
                    else:
                        print('You lost')
                else:
                    if number % 3 == 0:
                        print('You were right!')
                        chips += 3 * bet_of_player
                    else:
                        print('You lost')
            elif option.lower() in ['1 to 18','19 to 36']:
                if option.lower() == '1 to 18':
                    if number in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]:
                        print('You were right!')
                        chips += 2 * bet_of_player
                    else:
                        print('You lost')
                else:
                    if number in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]:
                        print('You lost')
                    else:
                        print('You were right!')
                        chips += 2 * bet_of_player
            else:
                print(f"That is not an real option, write the option as shown at the start. Without the '' of course.")
while True:
    game_of_roullete()
    qui_t = input('Do you want to exit the game?(y/n) ')
    if qui_t.lower() == 'n':
        print('Starting another game...')
        time.sleep(0.25)
    elif qui_t.lower() == 'y':
        import main
    else:
        print("You can either write 'n' or 'y'")