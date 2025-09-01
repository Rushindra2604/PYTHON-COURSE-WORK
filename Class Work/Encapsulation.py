class Details:
    def __init__(self,name,mail,pwd):
        self.name=name          #public attribute
        self._mail=mail         #protected attribute
        self.__pwd=pwd          #private attribute
        
    def getpassword(self):      #getter method
        return self.__pwd

    def setpassword(self,new_password):   #setter method
        self.__pwd=new_password

        


sumanth=Details("Sumanth","sumanth@gmail.com","Sumanth@123")

#Outside class

print(sumanth.name)
sumanth.name='Sanjay'
print(sumanth.name)


print(sumanth._mail)
sumanth._mail='Sanjay@gmail.com'
print(sumanth._mail)


print(sumanth.getpassword())
sumanth.setpassword("Sanjay@123")
print(sumanth.getpassword())
