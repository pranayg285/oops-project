class chatbook:
    def __init__(self):  #__init__ is the constructor which is used to define the attributes of the class
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.menu()   #we will call the menu method inside the constructor, because as soon as we create an object for the class, the constructor gets called. Since we have declared the menu method inside the constructor, it will also be called.
        
    def menu(self):   #this is one of the methods of the class
        user_input = input("""Welcome to Chatbook !! How would you like to proceed?
                           1. Press 1 to signup
                           2. Press 2 to signin
                           3. Press 3 to write a post
                           4. Press 4 to message a friend
                           5. Press any other key to exit 
                           
                           """)
        
        if user_input == "1":
            self.signup()  #we will call the signup method that we have created.
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            self.my_post()
        elif user_input == "4":
            self.msg_friend()
        else:
            exit()
        
    def signup(self):
        email = input("Enter your email over here : ")
        pwd = input ("Enter your desired password over here: ")
        self.username = email    #so whatever email the user provides will become the username for them, the username attribute is fetched.
        self.password = pwd
        print ("You have signed up successfully!!!")
        print("\n")
        self.menu() #we have again called the menu method at the end of this signup method because once this method is done executing, it will return back to the menu method and will run that and show the user all the options again.
        
    def signin(self): #for the signin of the user we need to first verify wether the user has signed up or not.
        if self.username == '' and self.password == '':   #if the username and password are empty then we will ask the user to sign up first and then sign in.
            print("Please Sign up first by pressing 1 in the main menu.")
        else:
            uname = input("Please enter your email/username over here: ")
            pwd = input("Please enter your password over here: ")
            if self.username == uname and self.password == pwd:
                print("You have successfully Logged in!!")
                self.loggedin = True
            else:
                print("Please input your correct credentials.")
        print("\n")
        self.menu()
            
    def my_post(self):
        if self.loggedin == True:   #we will check if the user is logged in or not, if the user is logged in (step2) then the loggedin attribute will be set to True, else False.
            txt = input("Enter your post here: ")   
            print(f"Following content has been posted: {txt}")
        else:
            print("Please sign in first by pressing 1 in the main menu.")
        print("\n")
        self.menu()
    
    def msg_friend(self):
        if self.loggedin == True:
            friend = input("Whom do you want to send this message to: ")
            msg = input ("Enter your message over here: ")
            print(f"Your message has been delivered to {friend}")
        else:
            print("You need to sign in first by pressing 1 in the main menu.")    
        print("\n")
        self.menu()
        
user1 = chatbook()  #we have created the object for the class, so now as soon as we run the code the constructor would be called immediately. The constructor gets called once we create the object for the class.