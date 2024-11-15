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
    
    def getPersonProfession(self):
        return self.personProfession
    
    def setPersonProfession(self, personProfession):
        

#Character Classes

#Character SubClasses