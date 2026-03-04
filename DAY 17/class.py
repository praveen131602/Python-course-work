class InstagramV1:
    def __init__(self,username):
        self.username = username

        print(f"Hey {self.username},Welcome to the instagrm!!!!!!!!!!!!!")

    def reels(self):
        print("you can upload and scroll the reels")

    def posts(self):
        print("you can post your pics")

class InstagramV2(InstagramV1):
    
    def __init__(self,username):
        super().__init__(username)

    def story(self):
        print("you can uoload the story")

class InstagramV3(InstagramV2):
    def __init__(self,username):
        super().__init__(username)

    def note(self):
        print("you can upload a note")

class Live:
    def launchlive(self):
        print("Now you can go on live")

class Verification:
    def verify(self):
        print("you can verify your account for better feautures")

class InstagramV4(InstagramV3,Live,Verification):
    def __init__(self,username):
        super().__init__(username)

class Creator(InstagramV4):
    def __init__(self,username):
        super().__init__(username)

    def insights(self):
        print("you can check you post insights")

class Business(InstagramV4):
    def __init__(self,username):
        super().__init__(username)

    def buttons(self):
        print("you can contact them mail and number")
   

sapnil = InstagramV1('sapnil')
sapnil.reels()
sapnil.posts()
print("\n")

varsha = InstagramV2('varsha')
varsha.reels()
varsha.posts()
varsha.story()
print("\n")

praveen = InstagramV3('praveen')
praveen.reels()
praveen.posts()
praveen.story()
praveen.note()
print("\n")

abhi = InstagramV4('abhi')
abhi.reels()
abhi.posts()
abhi.story()
abhi.note()
abhi.launchlive()
abhi.verify()
print("\n")




