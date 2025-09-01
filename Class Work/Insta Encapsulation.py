class Instagram:
    def __init__(self,username,bio,account_status=False):
        self.username=username
        self.bio=bio
        self.__account_status=account_status

    def get_acc_status(self):
        return self.__account_status

    def set_acc_status(self,status):
        self.__account_status=status

    @property
    def bio(self):
        return self._bio

    @bio.setter
    def bio(self,new_bio):
        self._bio=new_bio
            

        
mohit=Instagram("Mohith","My Life My Rules",False)

print(mohit.username)
mohit.username="Tarak"
print(mohit.username)

print(mohit.get_acc_status())
mohit.set_acc_status(True)
print(mohit.get_acc_status())

print(mohit.bio)
mohit.bio="Coder"
print(mohit.bio)
