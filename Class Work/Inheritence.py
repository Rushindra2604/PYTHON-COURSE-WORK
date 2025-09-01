'''
A->B

A-> B,C,D.......

A,B,C-> D

A->B->C->D......
'''
#Single Inheritance A -> B

class Status:
    def uploadImage(self,imageurl):
        self.image=imageurl
        print(f"{self.image} is uploaded to your status")

class StatusV1(Status):
    def addCaption(self,text=None):
        self.caption=text
        print(f'{self.caption} is added to your status')

rushi=Status()
rushi.uploadImage('selfie.png')

gopal=StatusV1()
gopal.uploadImage('Good Morning.png')
gopal.addCaption("Morning Friends!!!!")

#Hierachial Inheritance A ->B,C,D...

class Status:
    def uploadImage(self,imageurl):
        self.image=imageurl
        print(f"{self.image} is uploaded to your status")

class StatusV1(Status):
    def addCaption(self,text=None):
        self.caption=text
        print(f'{self.caption} is added to your status')

class StatusV2(Status):
    def like(self):
        print(f'You can like Status')
    

rushi=Status()
rushi.uploadImage('selfie.png')

gopal=StatusV1()
gopal.uploadImage('Good Morning.png')
gopal.addCaption("Morning Friends!!!!")

tarak=StatusV2()
tarak.uploadImage("Tea.png")
tarak.like()

#Multiple Inheritance A,B,C ->D

class Status:
    def uploadImage(self,imageurl):
        self.image=imageurl
        print(f"{self.image} is uploaded to your status")

class StatusV1(Status):
    def addCaption(self,text=None):
        self.caption=text
        print(f'{self.caption} is added to your status')

class StatusV2(Status):
    def like(self):
        print(f'You can like Status')
        
class StatusV3(StatusV1,StatusV2):
    def addMusic(self,music):
        self.music=music
        print(f'{self.music}... is added to your status')
        
rushi=Status()
rushi.uploadImage('selfie.png')

gopal=StatusV1()
gopal.uploadImage('Good Morning.png')
gopal.addCaption("Morning Friends!!!!")

tarak=StatusV2()
tarak.uploadImage("Tea.png")
tarak.like()

mohit = StatusV3()
mohit.uploadImage("Mountains and Trees.png")
mohit.addCaption("No WiFi")
mohit.like()
mohit.addMusic("PowerHouse.mp3")

#Multi-Level Inheritance A -> B -> C -> D
class Status:
    def uploadImage(self,image):
        self.image = image
        print(f"{self.image} is uploaded to your status")
class StatusV1(Status):
    def addCaption(self,text=None):
        self.caption = text
        print(f"{self.caption} is added to yout status")
class StatusV2(StatusV1):
    def like(self):
        print(f"You can like status")
class StatusV3(StatusV2):
    def addMusic(self,music):
        self.music = music
        print(f"{self.music}...is add to your status")
class StatusV4(StatusV3):
    def videolength(self,video):
        self.video = video
        print(f"{self.video} is uploaded to your status")
ramya = Status()
print('Ramya upload')
ramya.uploadImage('Good Morning.png')

hema = StatusV1()
print("Hema able to access")
hema.uploadImage('God.png')
hema.addCaption('Om Sai ram..!')

print("Vaishnavi able to access")
vaishnavi = StatusV2()
print("Vaishnavi able to access")
vaishnavi.uploadImage('Selfie.png')
vaishnavi.like()

print("Deepika able to access")
deepika = StatusV3()
deepika.uploadImage("Mountanains.png")
deepika.addCaption('Hey..! Guys good morning')
deepika.like()
deepika.addMusic('PowerHouse.mp3')

print("Tarak able to access")
tarak = StatusV4()
tarak.uploadImage("Swag.png")
tarak.addCaption('Chill!')
tarak.like()
tarak.addMusic("Salam Anali.mp3")
tarak.videolength("SelfsssLove.mp4")