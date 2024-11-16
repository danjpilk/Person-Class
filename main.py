#Roadmap
#First Code all classes and subclasses
#Allow for interaction between subclasses and randomised attributes from lists (Code exists in other folders)
#Allow for randomised enemies to be spawned in and the character/player can interact with them
#Allow for some form of attacking back which requires skill
#Levels with different levels of enemies of different difficulty
#Perhaps NPC dialogue, randomly generated from a list
#Allow for other classes to 'follow' you, perhaps party of 3/4 
#Save data in .txt file?
#IMPORT CLASSES HERE
#----------------------------------------------------------
#Game
#Give player options to move from Start Location, EXAMPLE MAP 
#Cabin -> Forest -> Haunted Hollows (MORE DIFFICULTY ENEMIES???) -> Cave (EVEN MORE DIFFICULT?) -> Clearing (Maybe choices here??) 
# -> Ambush? (maybe like 10-15 enemies could really think of strategy) -> Final Boss (dragon?? some form of mythical beast) -> Winning Screen 

#----------------------------------------------------------
def encounterEnemyMonster():
    monsterNames = ["Bob", "Brian", "Dave"]
    dialogueLines = ["BRAINSSSS", "BRAINSS", "BRAINSSS"]
    weaknessList = ["Cats", "Dogs", "Cheese"]
    import random
    randName = random.randint(0, len(monsterNames)-1)
    randHealthPoints = random.randint(100, 200)
    randDialogueLines = random.randint(0, len(dialogueLines)-1)
    randDamage = random.randint(1, 6)
    randWeakness = random.randint(0, len(weaknessList)-1)
    zombie = Enemy(monsterNames[randName], randHealthPoints, dialogueLines[randDialogueLines], randDamage, weaknessList[randWeakness])
    print(zombie.enemyFight(zombie.weakness))
    if zombie.enemyFight() == True:
        encounterFriend()
    else:
        print("Game Over")

#----------------------------------------------------------
#zombie = Monster("Zombie", 100, "BRAINS")
#friend1 = Friend("Bob", 200, "Hey!", "abc", "£20")
#print(friend1.highFive())
#enemy1 = Enemy("Bob", 200, "Hey!", 5, "£20")
#print(enemy1.enemyFight(enemy1.weakness))
#encounterEnemyMonster()
    
#----------------------------------------------------------    