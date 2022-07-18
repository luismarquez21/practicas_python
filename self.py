class car: 
    def __init__(self, model, color):

        self.model = model 
        self.color = color 

        self.start()
        
        self.end()
    def start(self):
        print(self.model + ", has started!")
    
    def end(self): 
        print(self.model, self.color + ", END!")

mycar = car('model XYZ', 'red')