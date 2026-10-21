# Class for vehicles car
class car:
    def __init__(self):
        self.model = None
        self.rego = None
        self.year = None
        self.color = None
    
    def setModel(self, modelName):
        self.model = modelName
        
    def getModel(self):
        return self.model
    
    def setRego(self, regoName):
        self.rego = regoName
        
    def getRego(self):
        return self.rego
    
    def setYear(self, yearName):
        self.year = yearName
        
    def getYear(self):
        return self.year
    
    def setColor(self, colorName):
        self.color = colorName
        
    def getColor(self):
        return self.color
        
        
c1 = car()
c1.setModel("Toyota")
print(c1.getModel())
        
        
    