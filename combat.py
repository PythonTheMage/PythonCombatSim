import time
import random
import os
import player
import enemies


testVariable = True # Can't remember why this is here but I'll get back too it

messageDelay = 0.8 # Delay in seconds between messages. More comfortable and readable than everything appearing as the console calculates it.
playerHealth = 20 # Defines player base health
enemyHealth = 10 # Defines enemy health

# Defining the actions the player can take on his/her turn
def playerTurn():

    # Makes player and enemy health into global variables
    global enemyHealth
    global playerHealth

    # Prompts the player for action (i.e. 'attack', 'run')
    playerInput = input("What do you do? ")
    print(f"\nYou {playerInput} the Goblin.")
    if playerInput.lower() == "attack":
        time.sleep(messageDelay)
        playerAttack = random.randint(0,4)
        enemyHealth -= playerAttack
        print(f"Goblin takes {playerAttack} damage!")
        if enemyHealth <= 0:
            time.sleep(messageDelay)
            print("You killed the Goblin!")
            time.sleep(messageDelay)
            exit()
    elif playerInput.lower() == "run":
        print("You escaped!")
        exit()
    else:
        time.sleep(messageDelay)
        print("The Goblin just stares at you...")
        time.sleep(2)
        playerTurn()
        
# Defining enemy turn
def enemyTurn():
    global enemyHealth
    global playerHealth
    enemyAttack = random.randint(0,5)
    print(f"The goblin attacks you.")
    time.sleep(messageDelay)
    print(f"You took {enemyAttack} damage!")
    playerHealth -= enemyAttack
    

# Clears screen making for a more readable user experience; is also cross-platform, using a different command depending on the operating system
def newTurn():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    
# Central gameplay loop
def main():
    # Step 1: Prompt the player to press ENTER when they are ready to play
    input("Press ENTER to Start Combat Simulation...")

    #
    newTurn()
    print("A Goblin blocks your path!")
    while playerHealth > 0 and enemyHealth > 0:
        print(f"\nYOU: {playerHealth} | ENEMY: {enemyHealth}")
        playerTurn()
        time.sleep(messageDelay)
        enemyTurn()
        time.sleep(messageDelay)
        newTurn()

main()

'''
    TO-DO LIST

- Add different physical attack types depending on weapon a la Persona (Strike, Slash and Pierce)
- Multiple enemies
- make it into an actual dungeon where you proceed instead of it just being a single battle
- spells
- elemental weaknesses
- loot
- weapons
- character and enemy attributes

'''