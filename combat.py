import time
import random
import os

testVariable = True

messageDelay = 0.8
playerHealth = 20
enemyHealth = 10

def playerTurn():
    global enemyHealth
    global playerHealth
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
        
def enemyTurn():
    global enemyHealth
    global playerHealth
    enemyAttack = random.randint(0,5)
    print(f"The goblin attacks you.")
    time.sleep(messageDelay)
    print(f"You took {enemyAttack} damage!")
    playerHealth -= enemyAttack
    
def newTurn():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    
def main():
    input("Press ENTER to Start Combat Simulation...")
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
