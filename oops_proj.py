
class chatbook:
    def __init__(self):
        self.username=""
        self.password=""
        self.loggedin=False
        self.menu()

    def menu(self):
        user_input=input("""WELCOME""")

        if(user_input=="1"):
            self.signup()
            pass
        elif(user_input=="2"):
            self.signin()
            pass
        elif(user_input=="3"):
            self.my_post()
            pass
        elif(user_input=="4"):
            self.sendmsg()
            pass
        else:
            exit()

    def signup(self):
        email=input("enter your email")
        pwd=input("setup your password here")
        self.username=email
        self.password=pwd
        print("successfully signedup ")
        print("\n")
        self.menu()
    

    def signin(self):
        if(self.username=="" and self.password==""):
            print("please signup by pressing one in main")
        else:
            uname=input("enter your email/username here ->")
            pwd=input("enter your password here")
            if self.username==uname and self.password==pwd:
                print("you are successfully signed in")    
                self.loggedin=True
            else:
                print("please input correct credantials")
                print("\n")

        self.menu()

    def my_post(self):
        if self.loggedin==True:
            txt=input("pls enter your post")
            print(f"following content has been posted {txt}")
        else:
            print("You nee dto sign in successfully")

        print("\n")    
        self.menu()

    def sendmsg(self):
        if self.loggedin==True:
            txt=input("enter your message here")
            frnd=input("enter to whom the message will be sent")

            print(f"the message has been sent to {frnd}")

        print("\n")
        self.menu()


obj=chatbook()                 