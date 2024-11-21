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
#Import Libraries
import random
import math
#----------------------------------------------------------
#Enemy Classes
#----------------------------------------------------------
class Monster: #Monster SUPERCLASS 
    def __init__(self, monsterName, monsterHealthPoints, monsterDialogueLine):
        self.monsterName = monsterName
        self.monsterHealthPoints = monsterHealthPoints
        self.monsterDialogueLine = monsterDialogueLine
    
    #getters and setters
    
    def setMonsterName(self, monsterName):
        self.monsterName = monsterName
    
    def getMonsterName(self):
        return self.monsterName
        
    def setMonsterHealthPoints(self, monsterHealthPoints):
        self.monsterHealthPoints = monsterHealthPoints
    
    def getMonsterHealthPoints(self):
        return self.monsterHealthPoints
    
    def setMonsterDialogueLine(self, monsterDialogueLine):
        self.monsterDialogueLine = monsterDialogueLine
    
    def getMonsterDialogueLine(self): #Speak function as well
        return self.monsterDialogueLine
    
    #Methods
    
    def take_Damage(self, damage):
        if self.monsterHealthPoints > 0:
            self.monsterHealthPoints -= damage
            return f"the monsters health points are now {self.monsterHealthPoints}"
            
        else:
            return f"{self.monsterName} has reached 0 health points"
            
            
            
class Friend(Monster): #SubClass of Monster
    def __init__(self, monsterName, monsterHealthPoints, monsterDialogueLine, highFiveDialogue, monsterGift): #constructor method
        super().__init__(monsterName, monsterHealthPoints, monsterDialogueLine) #super constructor
        self.highFiveDialogue = highFiveDialogue #initalises highFiveDialogue
        self.monsterGift = monsterGift # Same as Line 39 but monsterGift
        
    #getters and setters
        
    def getHighFive(self):
        return self.highFiveDialogue
    
    def setHighFive(self, high5):
        self.highFiveDialogue = high5
        
    def getMonsterGift(self):
        return self.monsterGift
    
    def setMonsterGift(self, gift):
        self.monsterGift = gift
    
    #highFive function
    def highFive(self):
        print(f"{self.name} says {self.highFiveDialogue}!")
        return f"You have received a Gift from {self.name}"
        
        


class Enemy(Monster): #Enemy Subclass 
    def __init__(self, monsterName, monsterHealthPoints, dialogueLine, enemyDamage, enemyWeakness):
        super().__init__(monsterName, monsterHealthPoints, dialogueLine)
        self.enemyDamage = enemyDamage
        self.enemyWeakness = enemyWeakness
    
    def getDamage(self):
        return self.enemyDamage
    
    def setDamage(self, enemyDamage):
        self.enemyDamage = enemyDamage
        
    def getWeakness(self):
        return self.weakness
    
    def setWeakness(self, enemyWeakness):
        self.enemyWeakness = enemyWeakness
        
    
    
class HostileEnemy(Enemy):
    def __init__(self, monsterName, monsterHealthPoints, enemyDamage):
        super().__init__(monsterName, monsterHealthPoints)
        
    def enemyFight(self, enemyWeakness):
        print(f"{self.dialogueLine}")
        if weapon.lower() == enemyWeakness.lower(): #Technically Weapon doesnt exist but can be fixed when imported into the game, could move to main.py 
            print("Enemy Defeated!")
            print( f"Player Wins!")
            return True
        
        else:
            print(f"Player Loses!")
            return False

#----------------------------------------------------------
#Friendly Classes
#----------------------------------------------------------
from EnemyClasses import * #Import Enemy Classes (due to fighting method)
#Main Classes 
class Person(): #Person Class SuperClass of all Person Classes (Paladin, Barbarian, Conjurer, Sorcerer etc)
    def __init__(self, personName, personAge, personStartLocation, personGoldCoins, 
                 personProfession, personSpeed, personHealthPoints, personLevel): #Constructor Method
        #All Attributes Initialised
        self.personName = personName
        self.personAge = personAge
        self.personStartLocation = personStartLocation
        self.personGoldCoins = personGoldCoins
        self.personProfession = personProfession
        self.personSpeed = personSpeed
        self.personHealthPoints = personHealthPoints
        self.personLevel = personLevel
    
    #Getters and Setters 
    def getPersonAge(self): 
        return self.personAge
    
    def setPersonAge(self, personAge):
        self.personAge = personAge

    def getPersonStartLocation(self):
        return self.personStartLocation
    
    def setPersonStartLocation(self, personStartLocation):
        self.personStartLocation = personStartLocation
    
    def getPersonGoldCoins(self):
        return self.personGoldCoins
    
    def setPersonGoldCoins(self, personGoldCoins):
        self.personGoldCoins = personGoldCoins
    
    def getPersonProfession(self):
        return self.personProfession
    
    def setPersonProfession(self, personProfession):
        self.personProfession = personProfession

    def getPersonSpeed(self):
        return self.personSpeed
    
    def setPersonSpeed(self, personSpeed):
        self.personSpeed = personSpeed
    
    def getPersonHealthPoints(self):
        return self.personHealthPoints
    
    def setPersonHealthPoints(self, personHealthPoints):
        self.personHealthPoints = personHealthPoints
    
    def getPersonLevel(self):
        return self.personLevel
    
    def setPersonLevel(self, personLevel):
        self.personLevel = personLevel

    #Methods 
    #These methods need to be changed
    
    def personTalk(dialogueLine):
        return f"{dialogueLine}" #Returns the dialogue line, will be generated later on 

    def personWalk(self, direction, distance):
        return f"{self.personName} walked in the {direction} for {distance} units"

    def personAttacked(self, healthPoints, Attacker):
        self.personHealthPoints -= healthPoints
        return f"{self.personName} lost {healthPoints} by {Attacker}"

#Character Classes
class Warrior(Person, Monster, Enemy):
    def __init__(self, personName, personAge, personStartLocation, personGoldCoins, 
                 personProfession, personSpeed, personLevel, 
                 WarriorHealthPoints, WarriorCombatSkill, WarriorWeapon, ):
        super().__init__(personName, personAge, personStartLocation, personGoldCoins, 
                 personProfession, personSpeed, personLevel)
        self.WarriorHealthPoints = WarriorHealthPoints
        self.WarriorCombatSkill = WarriorCombatSkill
        self.WarriorWeapon = WarriorWeapon
    
    def getWarriorHealthPoints(self):
        return self.WarriorHealthPoints
    
    def setWarriorHealthPoints(self, WarriorHealthPoints):
        self.WarriorHealthPoints = WarriorHealthPoints

    def getWarriorWeapon(self):
        return self.WarriorWeapon
    
    def setWarriorWeapon(self, WarriorWeapon):
        self.WarriorWeapon = WarriorWeapon
    
    def getWarriorCombatSkill(self):
        return self.WarriorCombatSkill

    def setWarriorCombatSkill(self, WarriorCombatSkill):
        self.WarriorCombatSkill = WarriorCombatSkill
    
    #Methods
    
    def WarriorTalk(self, dialogueLineWarrior):
        return f"{dialogueLineWarrior}"
    
    #WarriorFight definitely needs work
    
    def WarriorFight(self, WarriorCombatSkill, WarriorWeapon, currentEnemy):
        currentHP = self.WarriorHealthPoints

#----------------------------------------------------------



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
#Start of Game
def generateMonster():
    monsterNames = ["Bob", "Brian", "Dave"]
    dialogueLines = ["BRAINSSSS", "BRAINSS", "BRAINSSS"]
    weaknessList = ["Cats", "Dogs", "Cheese"]
    monsterType = ["Zombie", "Alien"]
    randName = random.randint(0, len(monsterNames)-1)
    randHealthPoints = random.randint(100, 200)
    randDialogueLines = random.randint(0, len(dialogueLines)-1)
    randDamage = random.randint(1, 6)
    randWeakness = random.randint(0, len(weaknessList)-1)
    monsterTypeName = random.randint(0, len(monsterType)-1)
    monster1 = Enemy(monsterNames[randName], randHealthPoints, dialogueLines[randDialogueLines], randDamage, weaknessList[randWeakness])

    
    