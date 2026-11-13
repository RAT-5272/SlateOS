from TerminalUserInterface import Window, windowManager, WIDTH, HEIGHT

class LoginScreen:
    def __init__(self, password: str = "1234"):
        loginScreenWindow = Window()
        #loginScreenWindow.AddLine(WIDTH/2, 0, HEIGHT/2+1, True)
        #loginScreenWindow.AddLine(0, HEIGHT/2, WIDTH/2, False)

        loginScreenWindow.CreateBox(-1, -1, WIDTH/3, HEIGHT)
        loginScreenWindow.CreateBox(WIDTH/3, 2*(HEIGHT/3)-1, 2*WIDTH/3, HEIGHT/3)

        welcomeString = "Welcome to SlateOS 2.0"
        loginScreenWindow.AddTextBox(WIDTH/2 - len(welcomeString)/2, HEIGHT/3, len(welcomeString), 2, welcomeString)
        windowManager.RenderWindow(loginScreenWindow)

    