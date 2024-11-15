#Roadmap
#First Code all classes and subclasses
#Allow for interaction between subclasses and randomised attributes from lists (Code exists in other folders)
#Allow for randomised enemies to be spawned in and the character/player can interact with them
#Allow for some form of attacking back which requires skill
#Levels with different levels of enemies of different difficulty



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

    def personTalk(dialogueLine):
        return f"{dialogueLine}" #Returns the dialogue line, will be generated later on 

    def personWalk(self, direction, distance):
        return f"{self.personName} walked in the {direction} for {distance} units"

    def personAttacked(self, healthPoints, Attacker):
        self.personHealthPoints -= healthPoints
        return f"{self.personName} lost {healthPoints} by {Attacker}"

#Character Classes
class Warrior(Person):
    def __init__(self, personName, personAge, personStartLocation, personGoldCoins, 
                 personProfession, personSpeed, personHealthPoints, personLevel, WarriorCombatSkill, WarriorWeapon):
        super().__init__(personName, personAge, personStartLocation, personGoldCoins, 
                 personProfession, personSpeed, personHealthPoints, personLevel)
        
#Character SubClasses