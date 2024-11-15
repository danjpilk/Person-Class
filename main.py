#Main Classes 
class Person():
    def __init__(self, personName, personAge, personStartLocation, personGoldCoins, 
                 personProfession, personSpeed, personHealthPoints):
        self.personName = personName
        self.personAge = personAge
        self.personStartLocation = personStartLocation
        self.personGoldCoins = personGoldCoins
        self.personProfession = personProfession
        self.personSpeed = personSpeed
        self.personHealthPoints = personHealthPoints
    
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

    def personTalk(dialogueLine):
        return f"{dialogueLine}"

    def personWalk(self, direction, distance):
        return f"{self.personName} walked in the {direction} for {distance} units"

    def personAttacked(self, healthPoints, Attacker):
        self.personHealthPoints -= healthPoints
        return f"{self.personName} lost {healthPoints} by {Attacker}"


#Character Classes

#Character SubClasses