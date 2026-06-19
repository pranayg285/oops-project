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
                           5. Press any other key to exit""")
        
        if user_input == "1":
            pass
        elif user_input == "2":
            pass
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else:
            exit()
        
        
obj = chatbook()  #we have created the object for the class, so now as soon as we run the code the constructor would be called immediately. The constructor gets called once we create the object for the class.