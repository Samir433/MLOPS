class Chatbook:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.menu()

    def menu(self):
        userInput = input("""Enter your input here !!
                          1. For the signup
                          2. For the sign in
                          3. For the message to a friend
                          4. For the post a picture
                          5. For the exit""")
        if userInput=='1':
            self.signup()
        elif userInput=='2':
            self.signin()
        elif userInput=='3':
            self.message()
        elif userInput=='4':
            self.post()
        else:
            exit()
    
    def signup(self):
        username = input("Enter Your email here: ")
        password = input("Setup Your password here: ")
        self.username = username
        self.password = password
        print("You are signed up successfully !!!")
        self.menu()
    
    def signin(self):
        username = self.username
        password = self.password

        if username == '' or password=='':
            print("Please signed up using 1 as input")
        else:
            name = input("Enter your Username: ")
            pwd = input("Enter Your password: ")

            if name == username and pwd == password:
                print("You have signed in succesfully !!")
                self.loggedin = True
                self.menu()
            else:
                print("Enter the correct detail and try again 😊")
                self.signin()
    def message(self):
        if self.loggedin:
            print("Select the friend you want to message")
            print("Your message sent succesfully")
            self.menu()
        else:
            print("Please first signin for that you need to press 2")
            self.menu()
    def post(self):
        if self.loggedin:
            print("select and Post the picture")
            print("Your picture posted succesfully")
            self.menu()
        else:
            print("Please first signin for that your need to press 2")   
            self.menu()

obj = Chatbook()
