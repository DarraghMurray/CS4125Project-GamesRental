from View.LogInUI import LogInUI
from View.RegisterUI import RegisterUI
from View.ItemPageUI import ItemPageUI

class NavigationController():

    def __init__(self, mainScreen):
        self.mainScreen = mainScreen
        
    def navigateToRegistration(self):
        self.mainScreen.setCurrentFrame(RegisterUI)
        self.mainScreen.loadScreen()

    def navigateToLogIn(self):
        self.mainScreen.setCurrentFrame(LogInUI)
        self.mainScreen.loadScreen()

    def navigateToStore(self):
        self.mainScreen.setCurrentFrame(ItemPageUI)
        self.mainScreen.loadScreen()

    def navigateToLibrary(self):
        pass

    def navigateToCart(self):
        pass