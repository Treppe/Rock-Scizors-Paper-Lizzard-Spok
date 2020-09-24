import random


def name_to_number(name):
    '''
    Function converts the string name
    into corresponding number between 0 and 4
    '''
    if name == 'rock':
        return 0
    elif name == 'Spock':
        return 1
    elif name == 'paper':
        return 2
    elif name == 'lizard':
        return 3
    elif name == 'scissors':
        return 4
    else:
        print("Error: Invalid name")
        return None


def number_to_name(number):
    '''
    Function converts a number in the range 0 to 4
    into its corresponding name as a string.
    '''
    if number == 0:
        return 'rock'
    elif number == 1:
        return 'Spock'
    elif number == 2:
        return 'paper'
    elif number == 3:
        return 'lizard'
    elif number == 4:
        return 'scissors'


def rpsls(player_choice):
    ''' Function  determines and prints out the winner '''
    print
    print('Player chooses ' + player_choice)
    player_number = name_to_number(player_choice)

    # Error check. Just in case.
    if player_number is not None:
        comp_number = random.randrange(0, 5)
        comp_choice = number_to_name(comp_number)
        print('Computer chooses ' + comp_choice)

        # Difference between comp_number and player_number taken modulo five
        difference = (player_number - comp_number) - (
            ((player_number - comp_number) // 5) * 5)

        if difference == 1 or difference == 2:
            print('Player wins!')
        elif difference == 0:
            print('Player and computer tie!')
        else:
            print('Computer wins!')


# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")



