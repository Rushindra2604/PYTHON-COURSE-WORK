class normalUser:
    def playvideo(self,name):
        print(f"\n{name} is playing video with :\n1.Normal Quality\n2.Ads run\n3.No background play\n4.limited downloads\n5.Music with Ads")
    def likes(self):
        pass
    def comments(self):
        pass
    def share(self):
        pass
    def title(self):
        pass
    def description(self):
        pass
    def subscribe(self):
        pass

class premiumUser(normalUser):
    def playvideo(self,name):
        print(f"\n{name} is playing video with :\n1.High Quality\n2.Ads Free\n3.Background play\n4.unlimited downloads\n5.Exclusive Music")

def play_video(user,username):
    user.playvideo(username)

dinesh=normalUser()
sanjay=premiumUser()
mohit=normalUser()
tarak=premiumUser()
gopal=normalUser()
rushi=premiumUser()

play_video(dinesh,"dinesh")
play_video(sanjay,"sanjay")
play_video(mohit,"mohit")
play_video(tarak,"tarak")
play_video(gopal,"gopal")
play_video(rushi,"rushi")
