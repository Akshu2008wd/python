class cat:
    def __init__(self , name , age):
        self.name=name
        self.age=age
        
    def info(self):
        print("My name is {self.name} and My age is {self.age}")
        
    def info(self):
        print("I am a cat i can meow.... ")
        
class dog:
    def __init__(self , name , age):
        self.name=name
        self.age=age
        
    def info(self):
        print("My name is {self.name} and My age is {self.age}")
        
    def info(self):
        print("I am a cat i can Bark.... ")
        
class cow:
    def __init__(self , name , age):
        self.name=name
        self.age=age
        
    def info(self):
        print("My name is {self.name} and My age is {self.age}")
        
    def info(self):
        print("I am a cat i can mooo.... ")

c=cat("kitty",3)
d=dog("chtti" , 5)
co=cow("belly" , 6)

for animal in (c,d,co):
    info(c)

