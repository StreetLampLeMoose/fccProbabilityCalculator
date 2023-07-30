import copy
import random


class Hat:
    def __init__(self, **kContents):
        contents = []
        for key , value in kContents.items(): 
            i = 0
            while i < value: 
                contents.append(key)
                i+=1
        self.contents = contents
        self.drawnList = []
                
    def draw(self,numberOfBalls): 
        i = 0
        currentBall = ""
        if numberOfBalls >= len(self.contents) : 
            for x in self.drawnList:
                self.contents.append(x)
            self.drawnList = []
            return self.contents
        while i < numberOfBalls :
            randIndex = random.randrange(0,len(self.contents),1)
            currentBall = self.contents[randIndex]
            self.drawnList.append(currentBall)
            del self.contents[randIndex]
            i +=1  
        return self.drawnList
        
        
    
    

def experiment(hat, expected_balls, num_balls_drawn, num_experiments): #this function performs a number of xperiemnts
    i=0
    numberOfMatches = 0
    while i < num_experiments: 
        result = []
        count = 0
        hatCopy = copy.deepcopy(hat) #have to use a deepcopy to avoid modifying the original hat object. 
        result = hatCopy.draw(num_balls_drawn)
        resultDict = resultOrganizer(result)
        for x in expected_balls :
            try : #catches an exception if there the key does not exist in one or the other objects
                if resultDict[x] >= expected_balls[x] : 
                    count +=1
            except :
                pass
        if count == len(expected_balls) : 
            numberOfMatches += 1
        i+= 1
   
    return numberOfMatches / num_experiments

def resultOrganizer(result) : #this function takes th results an contructs an object in the correct form
    organizedResults = {}
    for x in result: 
        if x not in organizedResults :
            organizedResults[x] = 1
        elif x in organizedResults : 
            organizedResults[x] +=1
    return organizedResults



    




