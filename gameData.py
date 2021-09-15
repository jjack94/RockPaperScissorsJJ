import variables
import random
import time


def intro():
    # seed creates random numbers to be used to pick random weapons if needed for cpu
    random.seed()
    print("Welcome to rock,paper scissors-hope you are ready for friendly game with a computer ")
    time.sleep(1)
    print("Select your weapon by inputting the first letter of your choice ")
    variables.user_weapon = input("CHOOSE YOUR WEAPON: Rock---Paper---Scissors ").lower()
    # allows case of input to be made into lower case if it is caps
    if variables.user_weapon in variables.valid_weapons:
        score()
    else:
        print("Please select a valid choice")
        time.sleep(1)
        intro()


# blocks for CPU actions
# cpu should make decisions based on how often a weapon was played in order to try to beat player by counters
# otherwise it will just select one randomly

def score():
    # tracking of weapon choices
    if variables.user_weapon == "p":
        variables.paper_used += 1
    elif variables.user_weapon == "s":
        variables.scissors_used += 1
    else:
        variables.rock_used += 1

    # track cpu choices
    if variables.cpu_weapon == "p":
        variables.cpu_paper_used += 1
    elif variables.cpu_weapon == "s":
        variables.cpu_scissors_used += 1
    else:
        variables.cpu_rock_used += 1

    if (variables.rock_used > variables.paper_used) and (variables.rock_used > variables.scissors_used):
        variables.cpu_weapon = "p"  # paper is used to counter rock if rock is used more than all

    elif (variables.paper_used > variables.scissors_used) and (variables.paper_used > variables.rock_used):
        variables.cpu_weapon = "s"  # scissors is used to counter paper if paper used more

    elif (variables.scissors_used > variables.paper_used) and (variables.scissors_used > variables.rock_used):
        variables.cpu_weapon = "r"  # rock used if scissors used more than all

    else:
        variables.cpu_weapon = random.choice(["r", "p", "s"])
        # selects random weapon if no favorite is detected
    decider()


def decider():
    if variables.user_weapon == variables.cpu_weapon:
        print("Looks like this one is a tie! ")
        print("Both players chose the same option")
        variables.score_tie += 1

    elif variables.user_weapon == "r":
        if variables.cpu_weapon == "p":
            print("YOU WIN! Rock beats paper.")
            variables.score_user += 1
        else:
            print("YOU LOSE! Paper beats rock.")
            variables.score_cpu += 1

    elif variables.user_weapon == "p":
        if variables.cpu_weapon == "r":
            print("YOU WIN! Paper beats rock.")
            variables.score_user += 1
        else:
            print("YOU LOSE! Scissors beats paper.")
            variables.score_cpu += 1

    elif variables.user_weapon == "s":
        if variables.cpu_weapon == "p":
            print("YOU WIN! Scissors beats paper.")
            variables.score_user += 1
        else:
            print("YOU LOSE! Rock beats scissors")
    retry()


def retry():
    # prompt user to keep playing or exit
    print("Would you like to continue?? Don't let the machines win!!! Press y or Y")
    print("If not, input q or Q to quit to results")
    variables.play_cont = input().lower()
    if variables.play_cont == "q":
        end()
    else:
        intro()


def end():
    # print statements for results
    # user stats
    print('THE RESULTS ARE IN:')
    print("WINS: " + str(variables.score_user))
    print("LOST: " + str(variables.score_cpu))
    print("TIES: " + str(variables.score_tie))
    print("YOUR WEAPON STATS ")
    print("# of times rock was chosen: " + str(variables.rock_used))
    print("# of times paper was chosen: " + str(variables.paper_used))
    print("# of times scissors was chosen: " + str(variables.scissors_used))
    # cpu stats
    print("CPU WEAPON STATS ")
    print("# of times rock was chosen: " + str(variables.cpu_rock_used))
    print("# of times paper was chosen: " + str(variables.cpu_paper_used))
    print("# of times scissors was chosen: " + str(variables.cpu_scissors_used))
    time.sleep(3)
    print("Hope you had fun and thanks for playing -----James ")
