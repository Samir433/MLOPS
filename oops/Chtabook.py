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
            print("Sam")
        elif userInput=='2':
            pass
        elif userInput=='3':
            pass
        elif userInput=='4':
            pass
        else:
            exit()
    
    def user_inputs(self):
        username = input("Enter Your email here: ")
        password = input("Setup Your password here: ")
        self.username = username
        self.password = password
    
