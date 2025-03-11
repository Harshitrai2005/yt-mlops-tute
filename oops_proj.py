
class chatbook:
    def __init__(self):
        self.username=" "
        self.password=" "
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
            pass
        elif(user_input=="4"):
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

        self.menu()


obj=chatbook()                 