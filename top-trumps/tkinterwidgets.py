from cardAttributes import CardValues, Card, Player
import tkinter as tk
from tkinter import ttk
from random import randint
from enum import Enum

def chooseRandom(*args):
    randNum = randint(0,len(args)-1)
    return args[randNum]

def chooseLargestAttribute(card: Card) -> CardValues:
    a = card.getFirepower()
    b = card.getTonnage()
    c = card.getSpeed()
    d = card.getArmour()

    # Some attributes may duplicate for cards
    if a == b:
        if chooseRandom(a,b) == a:
            return CardValues.FIREPOWER
        else:
            return CardValues.TONNAGE
    if a == c:
        if chooseRandom(a,c) == a:
            return CardValues.FIREPOWER
        else:
            return CardValues.SPEED
    if a == d:
        if chooseRandom(a,d) == a:
            return CardValues.FIREPOWER
        else:
            return CardValues.ARMOUR
    if b == c:
        if chooseRandom(b,c) == b:
            return CardValues.TONNAGE
        else:
            return CardValues.SPEED
    if b == d:
        if chooseRandom(b,d) == b:
            return CardValues.TONNAGE
        else:
            return CardValues.ARMOUR
    if c == d:
        if chooseRandom(c,d) == d:
            return CardValues.SPEED
        else:
            return CardValues.ARMOUR
        
    if a > b and a > c and a > d:
        return CardValues.FIREPOWER
    if b > a and b > c and b > d:
        return CardValues.TONNAGE
    if c > a and c > b and c > d:
        return CardValues.SPEED
    if d > a and d > b and d > c:
        return CardValues.ARMOUR
    try:
        raise Exception("No attribute selected!")
    except Exception:
        print("No attribute selected for opponent, how odd.")
        return CardValues.FIREPOWER

        


    # if here, there is one value that is greatest
    if a > b and a > c and a > d:
        return CardValues.FIREPOWER
    elif b > c and b > d:
        return CardValues.TONNAGE
    elif c > d:
        return CardValues.SPEED
    return CardValues.ARMOUR


# Theme name : [bg, fg]
global colorThemes

colorThemes = {
    'Default' : ['#ffffff', '#000000'],
    'Ice Cold' : ['#d3d3d3', '#739BD0']
}


# For the "Help" option in the menu
helpText = "Help Text"


# return [SCREEN_WIDTH, SCREEN_HEIGHT]
def getScreenDimensions() -> list[int]:
    # return [tk.Tk().winfo_screenwidth(), tk.Tk().winfo_screenheight()]
    return [1280, 720]
#name, country, firepower, tonnage, speed, armour


class mainWindow:
    def __init__(self, playerHand: Player, opponentHand: Player, playerDataSaveLocation: str) -> None:
        # Attributes
        self.selectedAttribute: CardValues = CardValues.NULL
        self.fileStorageLocation = playerDataSaveLocation
        self.rootWindow = tk.Tk()
        self.root = tk.Frame(self.rootWindow)
        self.root.pack(fill="both", expand=True)
        self.SCREEN_WIDTH = (getScreenDimensions())[0]
        self.SCREEN_HEIGHT = (getScreenDimensions())[1]
        self.isOpponentHuman: bool = False
        self.playAgainstComputer = tk.IntVar()
        self.currentCard: Card = Card("", "", 0,0,0,0, "")
        self.photo = None
        self.font_selectedOption = tk.StringVar(value = "Arial")
        self.theme_selectedOption = tk.StringVar(value = "Default")
        self.fontsize_selectedOption = tk.StringVar(value = "10")
        self.matchNumber: int = 0

        self.playerHand: Player = playerHand
        self.opponentHand: Player = opponentHand

        # I feel stupid now because the constructor is like 500 lines long when i could just abstract most of this into a private method


        # Root Configurations
        self.rootWindow.title("Top Trumps")
        self.rootWindow.geometry(f"{self.SCREEN_WIDTH}x{self.SCREEN_HEIGHT}")
        self.root.grid_rowconfigure(0, weight=0)
        self.root.grid_rowconfigure(1, weight=15) # 75%
        self.root.grid_rowconfigure(2, weight=2)  # 10%
        self.root.grid_rowconfigure(3, weight=3)  # 15%
        self.root.grid_columnconfigure(0, weight = 1)



        # <---Menu---> #
        self.menuBar = tk.Menu(self.root)

        # File Menu
        self.fileMenu = tk.Menu(self.menuBar, tearoff=0)
        self.fileMenu.add_command(label="New", command=self.noFunctionality)
        self.fileMenu.add_command(label="Open", command=self.noFunctionality)
        self.fileMenu.add_command(label="Save", command=self.noFunctionality)
        self.fileMenu.add_command(label="Save As", command=self.noFunctionality)
        self.fileMenu.add_command(label="Close", command=self.noFunctionality)
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label="Quit", command=self.closeWindow)
        self.menuBar.add_cascade(label="File", menu=self.fileMenu)

        # Edit Menu
        self.editMenu = tk.Menu(self.menuBar, tearoff=0)
        self.editMenu.add_command(label="undo", command = self.noFunctionality)
        self.editMenu.add_separator()
        self.editMenu.add_command(label="Cut", command = self.noFunctionality)
        self.editMenu.add_command(label="Copy", command = self.noFunctionality)
        self.editMenu.add_command(label="Paste", command = self.noFunctionality)
        self.editMenu.add_command(label="Delete", command = self.noFunctionality)
        self.editMenu.add_command(label="Select All", command = self.noFunctionality)
        self.menuBar.add_cascade(label="Edit", menu=self.editMenu)

        # Help Menu
        self.helpMenu = tk.Menu(self.menuBar, tearoff=0)
        self.helpMenu.add_command(label="How To Play", command=self.showHelpPage)
        self.helpMenu.add_command(label="About...", command=self.noFunctionality)
        self.menuBar.add_cascade(label="Help", menu=self.helpMenu)

        self.rootWindow.config(menu = self.menuBar)
        # <---End of menu---> #



        # <----Image and Stats Frame---->
        self.displayFrame = tk.Frame(self.root)
        self.displayFrame.rowconfigure(0, weight=1)
        self.displayFrame.columnconfigure(0, weight = 3)
        self.displayFrame.columnconfigure(1, weight = 1)

        # Image Widget
        self.ImageLabel = tk.Label(self.displayFrame)
        self.ImageLabel.grid(row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W)


        # Configure stats frame
        self.StatsFrame = tk.Frame(self.displayFrame)
        self.StatsFrame.grid(row=0, column=1, sticky=tk.N + tk.S + tk.E + tk.W)
        for i in range(7):
            self.StatsFrame.rowconfigure(i, weight = 1)

        # Stats Frame:
        self.cardLabel = tk.Label(self.StatsFrame, text="Your card:")
        self.nameLabel = tk.Label(self.StatsFrame, text="Name: ")
        self.countryLabel = tk.Label(self.StatsFrame, text="Country: ")
        self.firepowerLabel = tk.Label(self.StatsFrame, text="Firepower: ")
        self.tonnageLabel = tk.Label(self.StatsFrame, text="Tonnage: ")
        self.speedLabel = tk.Label(self.StatsFrame, text="Speed: ")
        self.armourLabel = tk.Label(self.StatsFrame, text="Armour: ")

        self.cardLabel.grid(row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
        self.nameLabel.grid(row=1, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
        self.countryLabel.grid(row=2, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
        self.firepowerLabel.grid(row=3, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
        self.tonnageLabel.grid(row=4, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
        self.speedLabel.grid(row=5, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
        self.armourLabel.grid(row=6, column=0, sticky=tk.N + tk.S + tk.E + tk.W)


        # <!---Image and Stats Frame---->



        # <----Buttons Frame---->
        self.selectAttributeFrame = tk.Frame(self.root)
        self.selectAttributeFrame.rowconfigure(0, weight=1)
        for i in range(4):
            self.selectAttributeFrame.columnconfigure(i, weight = 1)

        # Button widgets
        self.firepowerButton = tk.Button(self.selectAttributeFrame, command=lambda: self.changeSelectedAttribute(CardValues.FIREPOWER), text="Select Firepower")
        self.tonnageButton = tk.Button(self.selectAttributeFrame, command=lambda: self.changeSelectedAttribute(CardValues.TONNAGE), text="Select Tonnage")
        self.speedButton = tk.Button(self.selectAttributeFrame, command=lambda: self.changeSelectedAttribute(CardValues.SPEED), text="Select Speed")
        self.armourButton = tk.Button(self.selectAttributeFrame, command=lambda: self.changeSelectedAttribute(CardValues.ARMOUR), text="Select Armour")

        # Place Buttons into grid
        self.firepowerButton.grid(row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
        self.tonnageButton.grid(row=0, column=1, sticky=tk.N + tk.S + tk.E + tk.W)
        self.speedButton.grid(row=0, column=2, sticky=tk.N + tk.S + tk.E + tk.W)
        self.armourButton.grid(row=0, column=3, sticky=tk.N + tk.S + tk.E + tk.W)

        # <!---Buttons Frame---->



        # <---Options, Play and Info Frame---->
        self.interactiveFrame = tk.Frame(self.root)
        self.interactiveFrame.columnconfigure(0, weight = 1)
        self.interactiveFrame.columnconfigure(1, weight = 1)
        self.interactiveFrame.columnconfigure(2, weight = 2)
        self.interactiveFrame.rowconfigure(0, weight = 1)

        # Options Frame
        self.optionsFrame = tk.Frame(self.interactiveFrame)
        self.optionsFrame.grid(row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
        self.optionsFrame.columnconfigure(0, weight = 1)
        self.optionsFrame.rowconfigure(0, weight = 1)
        self.optionsFrame.rowconfigure(1, weight = 1)

        # optionsFrame widgets
        self.openOptionsButton = tk.Button(self.optionsFrame, text="Open Options Page", command=self.displayOptionsPage)
        self.infoLabel = tk.Label(self.optionsFrame, text="Development started 06/07/2025")
        self.infoLabel.grid(row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
        self.openOptionsButton.grid(row=1, column=0, sticky=tk.N + tk.S + tk.E + tk.W)

        # Play Button
        self.PlayButton = tk.Button(self.interactiveFrame, text="Play Game", command=self.playgame)                # <------------------------------------------------- PLAY
        self.PlayButton.grid(row=0, column=1, sticky=tk.N + tk.S + tk.E + tk.W)

        # Bottom Corner Match Stats Page
        self.MatchStatsFrame = tk.Frame(self.interactiveFrame)
        self.MatchStatsFrame.grid(row=0, column=2, sticky=tk.N + tk.S + tk.E + tk.W)
        self.MatchStatsFrame.columnconfigure(0, weight = 1)
        self.MatchStatsFrame.rowconfigure(0, weight = 1)
        self.MatchStatsFrame.rowconfigure(1, weight = 1)
        self.MatchStatsFrame.rowconfigure(2, weight = 1)

        # Inside MatchStatsFrame

        self.cardSelectedLabel = tk.Label(self.MatchStatsFrame, text="Selected Attribute: None")
        self.cardSelectedLabel.grid(row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W)

        # Player Stats Frame
        self.playerStatsFrame = tk.Frame(self.MatchStatsFrame)
        self.playerStatsFrame.grid(row=1, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
        self.playerStatsFrame.rowconfigure(0, weight = 1)
        self.playerStatsFrame.columnconfigure(0, weight = 1)
        self.playerStatsFrame.columnconfigure(1, weight = 1)

        # PlayerStatsFrame widgets
        self.playerCardCountLabel = tk.Label(self.playerStatsFrame)
        self.playerWinCountLabel = tk.Label(self.playerStatsFrame)
        self.playerCardCountLabel.grid(row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
        self.playerWinCountLabel.grid(row=0, column=1, sticky=tk.N + tk.S + tk.E + tk.W)

        # Opponent Stats Frame
        self.opponentStatsFrame = tk.Frame(self.MatchStatsFrame)
        self.opponentStatsFrame.grid(row=2, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
        self.opponentStatsFrame.rowconfigure(0, weight = 1)
        self.opponentStatsFrame.columnconfigure(0, weight = 1)
        self.opponentStatsFrame.columnconfigure(1, weight = 1)

        # OpponentStatsFrame widgets
        self.opponentCardCountLabel = tk.Label(self.opponentStatsFrame)
        self.opponentWinCountLabel = tk.Label(self.opponentStatsFrame)
        self.opponentCardCountLabel.grid(row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
        self.opponentWinCountLabel.grid(row=0, column=1, sticky=tk.N + tk.S + tk.E + tk.W)

        # <!---Options, Play and Info Frame---->



        # Display 3 frames, mainloop

        self.greetingLabel = tk.Label(self.root, text="Top Trumps Game")
        self.greetingLabel.grid(row = 0, column = 0, sticky=tk.N + tk.S + tk.E + tk.W)

        self.displayFrame.grid(row=1, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
        self.selectAttributeFrame.grid(row=2, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
        self.interactiveFrame.grid(row = 3, column = 0, sticky=tk.N + tk.S + tk.W + tk.E)

        self.updateCardShown(self.playerHand.getTopCard())
        self.updateBottomCornerInformation()
        self.rootWindow.mainloop()

    def getWinLossCount(self) -> list[int]:
        """
        Gets the win/loss count of the player from their data file
        """
        file = open(self.fileStorageLocation, "r")
        information = file.readlines()
        file.close()

        # Line 02: 'Wins: {winCount}'
        wins = information[2][0:(len(information[2])-1)]
        wins = wins[5:]

        # Line 03: 'Losses: {lossCount}'
        losses = information[3][0:(len(information[3])-1)]
        losses = losses[7:]
        return [int(wins), int(losses)]
    
    def updateWinLossCount(self, hasWon: bool) -> None:
        file = open(self.fileStorageLocation, "r")
        information = file.readlines()
        file.close()

        if hasWon == True:
            wins = information[2][0:(len(information[2])-1)]
            wins = int(wins[5:])
            wins += 1
            information[2] = "Wins: " + str(wins) + "\n"
            file = open(self.fileStorageLocation, "w")
            file.writelines(information)
            file.close()
            return
        else:
            losses = information[3][0:(len(information[3])-1)]
            losses = int(losses[7:])
            losses += 1
            information[3] = "Losses:" + str(losses) + "\n"
            file = open(self.fileStorageLocation, "w")
            file.writelines(information)
            file.close()
            return

    def updateInformation(self, hasWon: bool) -> None:
        """
        Updates the information in the player's file
        @param bool hasWon: True for if the player won, False if the opponent won
        """
        self.updateWinLossCount(hasWon)
        winLossInfo = self.getWinLossCount()
        file = open(self.fileStorageLocation, 'r')
        information = file.readlines()
        file.close()

        file = open(self.fileStorageLocation, "w")
        information[4] = f"Win/Loss Ratio: {winLossInfo[0] / winLossInfo[1]}"
        file.writelines(information)
        file.close()
        return

    def updateBottomCornerInformation(self) -> None:
        """
        Updates the bottom corner information of the root window
        """
        self.playerCardCountLabel.config(text=f"Your card count: {str(self.playerHand.getCardCount())}")
        self.opponentCardCountLabel.config(text=f"Opponent card count: {str(self.opponentHand.getCardCount())}")
        pass

    def getFont(self) -> tuple[str, int]:
        """
        Returns the font size in a tuple (font, fontSize)
        """
        return (self.font_selectedOption.get(), int(self.fontsize_selectedOption.get()))

    def getTheme(self) -> str:
        """
        Returns the theme of the screen, use in colorThemes[] to get [bg, fg]
        """
        return self.theme_selectedOption.get()

    def __str__(self) -> str:
        return f"Dimension of the window: {self.SCREEN_WIDTH}x{self.SCREEN_HEIGHT}"

    # Updates the 'selected attribute: ...' label in bottom right
    def updateCardSelectedLabel(self, cardValue: CardValues) -> None:
        """
        Updates the 'selected attribute: ...' label in the bottom right
        """
        if cardValue == CardValues.NULL:
            self.cardSelectedLabel.config(text="Selected Attribute: None")
        elif cardValue == CardValues.FIREPOWER:
            self.cardSelectedLabel.config(text="Selected Attribute: Firepower")
        elif cardValue == CardValues.TONNAGE:
            self.cardSelectedLabel.config(text="Selected Attribute: Tonnage")
        elif cardValue == CardValues.SPEED:
            self.cardSelectedLabel.config(text="Selected Attribute: Speed")
        else:
            self.cardSelectedLabel.config(text="Selected Attribute: Armour")

    def changeSelectedAttribute(self, newCardValue : CardValues) -> None:
        """
        Defines the behaviour for what attribute is selected to play
        """
        if self.selectedAttribute != newCardValue:
            self.selectedAttribute = newCardValue
        else:
            self.selectedAttribute = CardValues.NULL
        self.updateCardSelectedLabel(self.selectedAttribute)
        return

    def getSelectedAttribute(self) -> CardValues:
        """
        Returns the attribute selected by the player to play
        """
        return self.selectedAttribute

    def destructor(self) -> None:
        """
        For debugging
        """
        print("Session Quit!")
        return

    def closeWindow(self) -> None:
        """
        Closes the window and calls the destructor method
        """
        self.rootWindow.quit()
        self.rootWindow.destroy()
        self.destructor()

    def showHelpPage(self) -> None:
        """
        Creates the help page in the menu
        """
        helpWindow = tk.Toplevel(self.root)
        helpLabel = tk.Label(helpWindow, text=helpText)
        helpLabel.pack()

    def noFunctionality(self) -> None:
        """
        Creates a window for non-functional menu options
        """
        popupWindow = tk.Toplevel(self.root)
        alertLabel = tk.Label(popupWindow, text="No functionality added yet.", font=('Arial', 20))
        alertLabel.pack()

    def changeFont(self, fontName: str, fontSize: int) -> None:
        """
        Updates the font of the main window
        :param fontName: Name of the font, i.e Courier New
        :param fontSize: Font size to update to
        """
        self.cardLabel.config(font=(f"{fontName}", fontSize))
        self.nameLabel.config(font=(f"{fontName}", fontSize))
        self.countryLabel.config(font=(f"{fontName}", fontSize))
        self.firepowerLabel.config(font=(f"{fontName}", fontSize))
        self.tonnageLabel.config(font=(f"{fontName}", fontSize))
        self.speedLabel.config(font=(f"{fontName}", fontSize))
        self.armourLabel.config(font=(f"{fontName}", fontSize))

        self.firepowerButton.config(font=(f"{fontName}", fontSize))
        self.tonnageButton.config(font=(f"{fontName}", fontSize))
        self.speedButton.config(font=(f"{fontName}", fontSize))
        self.armourButton.config(font=(f"{fontName}", fontSize))

        self.PlayButton.config(font=(f"{fontName}", fontSize))

        self.openOptionsButton.config(font=(f"{fontName}", fontSize))
        self.infoLabel.config(font=(f"{fontName}", fontSize))

        self.cardSelectedLabel.config(font=(f"{fontName}", fontSize))

        self.playerCardCountLabel.config(font=(f"{fontName}", fontSize))
        self.playerWinCountLabel.config(font=(f"{fontName}", fontSize))

        self.opponentCardCountLabel.config(font=(f"{fontName}", fontSize))
        self.opponentWinCountLabel.config(font=(f"{fontName}", fontSize))

    def changeBackgroundColour(self, newColour: str):
        """
        Updates the theme of the main window
        :param newColour: Hexadecimal string to update the colour of the background to, i.e '#ffffff'
        """
        self.cardLabel.config(bg=newColour)
        self.nameLabel.config(bg=newColour)
        self.countryLabel.config(bg=newColour)
        self.firepowerLabel.config(bg=newColour)
        self.tonnageLabel.config(bg=newColour)
        self.speedLabel.config(bg=newColour)
        self.armourLabel.config(bg=newColour)

        self.firepowerButton.config(bg=newColour)
        self. tonnageButton.config(bg=newColour)
        self.speedButton.config(bg=newColour)
        self.armourButton.config(bg=newColour)

        self.PlayButton.config(bg=newColour)

        self.openOptionsButton.config(bg=newColour)
        self.infoLabel.config(bg=newColour)

        self.cardSelectedLabel.config(bg=newColour)
        self.playerCardCountLabel.config(bg=newColour)
        self.playerWinCountLabel.config(bg=newColour)
        self.opponentCardCountLabel.config(bg=newColour)
        self.opponentWinCountLabel.config(bg=newColour)

        self.rootWindow.config(bg = newColour)
        self.root.config(bg = newColour)
        self.displayFrame.config(bg = newColour)
        self.StatsFrame.config(bg = newColour)
        self.selectAttributeFrame.config(bg = newColour)
        self.interactiveFrame.config(bg = newColour)
        self.optionsFrame.config(bg = newColour)
        self.MatchStatsFrame.config(bg = newColour)
        self.playerStatsFrame.config(bg = newColour)
        self.opponentStatsFrame.config(bg = newColour)
        self.ImageLabel.config(bg = newColour)
        self.greetingLabel.config(bg = newColour)

    def changeTextColour(self, newColour: str):
        """
        Change the text colour of the window
        :param newColour: Hexadecimal string to update the text colour to, i.e '#ffffff'
        """
        self.cardLabel.config(fg=newColour)
        self.nameLabel.config(fg=newColour)
        self.countryLabel.config(fg=newColour)
        self.firepowerLabel.config(fg=newColour)
        self.tonnageLabel.config(fg=newColour)
        self.speedLabel.config(fg=newColour)
        self.armourLabel.config(fg=newColour)

        self.firepowerButton.config(fg=newColour)
        self.tonnageButton.config(fg=newColour)
        self.speedButton.config(fg=newColour)
        self.armourButton.config(fg=newColour)

        self.PlayButton.config(fg=newColour)

        self.openOptionsButton.config(fg=newColour)
        self.infoLabel.config(fg=newColour)

        self.cardSelectedLabel.config(fg=newColour)
        self.playerCardCountLabel.config(fg=newColour)
        self.playerWinCountLabel.config(fg=newColour)
        self.opponentCardCountLabel.config(fg=newColour)
        self.opponentWinCountLabel.config(fg=newColour)

    def updateCardShown(self, newCard: Card) -> None:
        """
        Updates the screen based on the card given
        :param newCard: Updates the screen to the information of this card
        """
        self.currentCard = newCard
        winWidth = self.SCREEN_WIDTH
        winHeight = self.SCREEN_HEIGHT
        winWidth = int(winWidth * 0.75)
        winHeight = int(winHeight * 0.75)

        self.nameLabel.config(text=f"Name: {newCard.getName()}")
        self.countryLabel.config(text=f"Country: {newCard.getCountry()}")
        self.firepowerLabel.config(text=f"Firepower: {newCard.getFirepower()}")
        self.tonnageLabel.config(text=f"Tonnage: {newCard.getTonnage()}")
        self.speedLabel.config(text=f"Speed: {newCard.getSpeed()}")
        self.armourLabel.config(text=f"Armour: {newCard.getArmour()}")

    def applyTheme(self, theme: str) -> None:
        """
        Updates the look of the screen based on the theme given
        :param theme: String used in colorThemes[] to access theme information
        """
        colours = colorThemes[theme] # Contains [bg_colour, fg_colour]
        self.changeBackgroundColour(colours[0])
        self.changeTextColour(colours[1])
        self.optionsRoot.destroy()
        return

    def closeOptionsRoot(self) -> None:
        """
        Closes the option window
        """
        self.optionsRoot.destroy()
        self.rootWindow.deiconify()

    def applyChanges(self) -> None:
        """
        Applies changes from the options screen
        """
        self.applyTheme(self.theme_selectedOption.get())
        newFont = self.font_selectedOption.get()
        newFontSize = int(self.fontsize_selectedOption.get())
        self.changeFont(newFont, newFontSize)
        self.rootWindow.deiconify()
        return

    def displayOptionsPage(self) -> None:
        """
        Creates an options page
        """
        self.rootWindow.withdraw()
        self.optionsRoot = tk.Toplevel(self.root)
        self.optionsPage = tk.Frame(self.optionsRoot)
        self.optionsPage.pack(fill="both", expand=True)

        self.optionsRoot.geometry(f"{int(self.SCREEN_WIDTH / 2)}x{int(self.SCREEN_HEIGHT / 2)}")
        separator = ttk.Separator(self.optionsPage, orient="horizontal") # for decoration
        self.optionsPage.columnconfigure(0, weight = 1)

        self.optionsPage.rowconfigure(0, weight = 2)
        self.optionsPage.rowconfigure(1, weight = 0)
        self.optionsPage.rowconfigure(2, weight = 2)
        self.optionsPage.rowconfigure(3, weight = 0)
        self.optionsPage.rowconfigure(4, weight = 2)
        self.optionsPage.rowconfigure(5, weight = 0)
        self.optionsPage.rowconfigure(6, weight = 1)
        separator.grid(row = 1, column = 0)
        separator.grid(row = 3, column = 0)
        separator.grid(row = 5, column = 0)

        self.font_choices = ['Arial', 'Times New Roman', 'Comic Sans MS', 'Courier New', 'Impact', 'Georgia', 'Comfortaa']
        self.Themes = ["Ice Cold", "Default"]
        self.fontSizeChoices = [8,9,10,12,14,16,18,20,24]

        self.themeFrame = tk.Frame(self.optionsPage)
        self.fontFrame = tk.Frame(self.optionsPage)
        self.fontSizeFrame = tk.Frame(self.optionsPage)

        # Theme Frame
        self.themeFrame.rowconfigure(0, weight = 1)
        self.themeFrame.columnconfigure(0, weight = 4) # Change this to reposition the dropdown menu
        self.themeFrame.columnconfigure(1, weight = 1)
        self.theme_DropDownMenu = tk.OptionMenu(self.themeFrame, self.theme_selectedOption, *self.Themes)
        self.themeLabel = tk.Label(self.themeFrame, text="Choose a theme: ")
        self.themeLabel.grid(row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
        self.theme_DropDownMenu.grid(row=0, column=1, sticky=tk.N + tk.S + tk.E + tk.W)


        # Font Frame
        self.fontFrame.rowconfigure(0, weight = 1)
        self.fontFrame.columnconfigure(0, weight = 4) # Change this to reposition the dropdown menu
        self.fontFrame.columnconfigure(1, weight = 1)
        self.font_DropDownMenu = tk.OptionMenu(self.fontFrame, self.font_selectedOption, *self.font_choices)
        self.fontLabel = tk.Label(self.fontFrame, text = "Font: ")
        self.fontLabel.grid(row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
        self.font_DropDownMenu.grid(row=0, column=1, sticky=tk.N + tk.S + tk.E + tk.W)

        # Font size frame
        self.fontSizeFrame.rowconfigure(0, weight = 1)
        self.fontSizeFrame.columnconfigure(0, weight = 4) # Change this to reposition the dropdown menu
        self.fontSizeFrame.columnconfigure(1, weight = 1)
        self.fontSize_DropDownMenu = tk.OptionMenu(self.fontSizeFrame, self.fontsize_selectedOption, *str(self.fontSizeChoices))
        self.fontSizeLabel = tk.Label(self.fontSizeFrame, text="Font size:")
        self.fontSizeLabel.grid(row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
        self.fontSize_DropDownMenu.grid(row=0, column=1, sticky=tk.N + tk.S + tk.E + tk.W)


        self.action_bar = tk.Frame(self.optionsRoot, bg='#ffffff', bd=1, relief="raised")
        self.action_bar.pack(side = "bottom", fill="x")

        self.apply_button = tk.Button(self.action_bar, text="Apply", width=10, command=self.applyChanges)
        self.ok_button = tk.Button(self.action_bar, text="Ok", width = 10, command=self.closeOptionsRoot)

        self.apply_button.pack(side="right", padx=10, pady=5)
        self.ok_button.pack(side="right", padx=10, pady=5)

        self.themeFrame.grid(row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
        self.fontFrame.grid(row=2, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
        self.fontSizeFrame.grid(row=1, column=0, sticky=tk.N + tk.S + tk.E + tk.W)

    def playgame(self) -> None:
        """
        Logic for controlling how the game is played
        """
        if self.selectedAttribute == CardValues.NULL:
            alertWindow("Choose a valid attribute!")
            return

        if self.opponentHand.isEmptyHand() == True:
            self.updateInformation(True)
            self.closeWindow()
            return

        if self.playerHand.isEmptyHand() == True:
            self.updateInformation(False)
            self.closeWindow()
            return

        # Valid card
        self.matchNumber += 1

        self.rootWindow.withdraw()
        playerCard = self.playerHand.getTopCard()
        opponentCard = self.opponentHand.getTopCard()
        self.updateCardShown(playerCard)
        self.updateBottomCornerInformation()

        if self.selectedAttribute == CardValues.FIREPOWER:
            if playerCard.getFirepower() > opponentCard.getFirepower():
                matchScreen(self, True, playerCard, opponentCard, CardValues.FIREPOWER, matchResult.WIN, self.matchNumber)
                opponentCard = self.opponentHand.removeCard()
                self.playerHand.addCardToHand(opponentCard)
            elif playerCard.getFirepower() == opponentCard.getFirepower():
                matchScreen(self, True, playerCard, opponentCard, CardValues.FIREPOWER, matchResult.TIE, self.matchNumber)
            else:
                matchScreen(self, True, playerCard, opponentCard, CardValues.FIREPOWER, matchResult.LOSE, self.matchNumber)
                playerCard = self.playerHand.removeCard()
                self.opponentHand.addCardToHand(playerCard)

        if self.selectedAttribute == CardValues.TONNAGE:
            if playerCard.getTonnage() > opponentCard.getTonnage():
                matchScreen(self, True, playerCard, opponentCard, CardValues.TONNAGE, matchResult.WIN, self.matchNumber)
                opponentCard = self.opponentHand.removeCard()
                self.playerHand.addCardToHand(opponentCard)
            elif playerCard.getTonnage() == opponentCard.getTonnage():
                matchScreen(self, True, playerCard, opponentCard, CardValues.TONNAGE, matchResult.TIE, self.matchNumber)
            else:
                matchScreen(self, True, playerCard, opponentCard, CardValues.TONNAGE, matchResult.LOSE, self.matchNumber)
                playerCard = self.playerHand.removeCard()
                self.opponentHand.addCardToHand(playerCard)

        elif self.selectedAttribute == CardValues.SPEED:
            if playerCard.getSpeed() > opponentCard.getSpeed():
                matchScreen(self, True, playerCard, opponentCard, CardValues.SPEED, matchResult.WIN, self.matchNumber)
                opponentCard = self.opponentHand.removeCard()
                self.playerHand.addCardToHand(opponentCard)
            elif playerCard.getSpeed() == opponentCard.getSpeed():
                matchScreen(self, True, playerCard, opponentCard, CardValues.SPEED, matchResult.TIE, self.matchNumber)
            else:
                matchScreen(self, True, playerCard, opponentCard, CardValues.SPEED, matchResult.LOSE, self.matchNumber)
                playerCard = self.playerHand.removeCard()
                self.opponentHand.addCardToHand(playerCard)

        elif self.selectedAttribute == CardValues.ARMOUR:
            if playerCard.getArmour() > opponentCard.getArmour():
                matchScreen(self, True, playerCard, opponentCard, CardValues.ARMOUR, matchResult.WIN, self.matchNumber)
                opponentCard = self.opponentHand.removeCard()
                self.playerHand.addCardToHand(opponentCard)
            elif playerCard.getArmour() == opponentCard.getArmour():
                matchScreen(self, True, playerCard, opponentCard, CardValues.ARMOUR, matchResult.TIE, self.matchNumber)
            else:
                matchScreen(self, True, playerCard, opponentCard, CardValues.ARMOUR, matchResult.LOSE, self.matchNumber)
                playerCard = self.playerHand.removeCard()
                self.opponentHand.addCardToHand(playerCard)

        # Player has completed their turn, onto the next round.
        if self.opponentHand.isEmptyHand() == True:
            self.updateInformation(True)
            self.closeWindow()
            return

        if self.playerHand.isEmptyHand() == True:
            self.updateInformation(False)
            self.closeWindow()
            return
        
        self.matchNumber += 1

        self.playerHand.moveOntoNextCard()
        self.opponentHand.moveOntoNextCard()
        playerCard = self.playerHand.getTopCard()
        opponentCard = self.opponentHand.getTopCard()
        opponentChoice = chooseLargestAttribute(opponentCard)

        self.updateCardShown(playerCard)
        self.updateBottomCornerInformation()

        if opponentChoice == CardValues.FIREPOWER:
            if playerCard.getFirepower() > opponentCard.getFirepower():
                matchScreen(self, False, playerCard, opponentCard, CardValues.FIREPOWER, matchResult.WIN, self.matchNumber)
                opponentCard = self.opponentHand.removeCard()
                self.playerHand.addCardToHand(opponentCard)
            elif playerCard.getFirepower() == opponentCard.getFirepower():
                matchScreen(self, False, playerCard, opponentCard, CardValues.FIREPOWER, matchResult.TIE, self.matchNumber)
            else:
                matchScreen(self, False, playerCard, opponentCard, CardValues.FIREPOWER, matchResult.LOSE, self.matchNumber)
                playerCard = self.playerHand.removeCard()
                self.opponentHand.addCardToHand(playerCard)

        elif opponentChoice == CardValues.TONNAGE:
            if playerCard.getTonnage() > opponentCard.getTonnage():
                matchScreen(self, False, playerCard, opponentCard, CardValues.TONNAGE, matchResult.WIN, self.matchNumber)
                opponentCard = self.opponentHand.removeCard()
                self.playerHand.addCardToHand(opponentCard)
            elif playerCard.getTonnage() == opponentCard.getTonnage():
                matchScreen(self, False, playerCard, opponentCard, CardValues.TONNAGE, matchResult.TIE, self.matchNumber)
            else:
                matchScreen(self, False, playerCard, opponentCard, CardValues.TONNAGE, matchResult.LOSE, self.matchNumber)
                playerCard = self.playerHand.removeCard()
                self.opponentHand.addCardToHand(playerCard)

        elif opponentChoice == CardValues.SPEED:
            if playerCard.getSpeed() > opponentCard.getSpeed():
                matchScreen(self, False, playerCard, opponentCard, CardValues.SPEED, matchResult.WIN, self.matchNumber)
                opponentCard = self.opponentHand.removeCard()
                self.playerHand.addCardToHand(opponentCard)
            elif playerCard.getSpeed() == opponentCard.getSpeed():
                matchScreen(self, False, playerCard, opponentCard, CardValues.SPEED, matchResult.TIE, self.matchNumber)
            else:
                matchScreen(self, False, playerCard, opponentCard, CardValues.SPEED, matchResult.LOSE, self.matchNumber)
                playerCard = self.playerHand.removeCard()
                self.opponentHand.addCardToHand(playerCard)

        elif opponentChoice == CardValues.ARMOUR:
            if playerCard.getArmour() > opponentCard.getArmour():
                matchScreen(self, False, playerCard, opponentCard, CardValues.ARMOUR, matchResult.WIN, self.matchNumber)
                opponentCard = self.opponentHand.removeCard()
                self.playerHand.addCardToHand(opponentCard)
            elif playerCard.getArmour() == opponentCard.getArmour():
                matchScreen(self, False, playerCard, opponentCard, CardValues.ARMOUR, matchResult.TIE, self.matchNumber)
            else:
                matchScreen(self, False, playerCard, opponentCard, CardValues.ARMOUR, matchResult.LOSE, self.matchNumber)
                playerCard = self.playerHand.removeCard()
                self.opponentHand.addCardToHand(playerCard)

        self.updateBottomCornerInformation()
        self.playerHand.moveOntoNextCard()
        self.opponentHand.moveOntoNextCard()
        self.updateCardShown(self.playerHand.getTopCard())
        self.updateBottomCornerInformation()
        self.rootWindow.deiconify()

class opponentPlayInformation:
    def __init__(self, opponentCard: Card, mainWin: mainWindow, opponentChoice: CardValues):
        # oStr = attribute selected by opponent
        self.oStr = ""
        if opponentChoice == CardValues.FIREPOWER:
            self.oStr = "Firepower"
        elif opponentChoice == CardValues.TONNAGE:
            self.oStr = "Tonnage"
        elif opponentChoice == CardValues.SPEED:
            self.oStr = "Speed"
        else:
            self.oStr = "Armour"

        mainWin.rootWindow.withdraw()
        self.root = tk.Toplevel(mainWin.rootWindow)
        self.root.title("Oppoent's Card")
        self.windowWidth = 800
        self.windowHeight = 600
        self.screenWidth = mainWin.rootWindow.winfo_screenwidth()
        self.screenHeight = mainWin.rootWindow.winfo_screenheight()
        self.x = (self.screenWidth - self.windowWidth) // 2
        self.y = (self.screenHeight - self.windowHeight) // 2
        self.root.geometry(f"{self.windowWidth}x{self.windowHeight}+{self.x}+{self.y}")
        self.fontInfo = mainWin.getFont()
        self.font: tuple = (self.fontInfo[0], self.fontInfo[1])
        self.theme = colorThemes[mainWin.getTheme()]
        self.bg = self.theme[0]
        self.fg = self.theme[1]

        self.root.rowconfigure(0, weight = 4)
        self.root.rowconfigure(1, weight = 1)

        self.InformationFrame = tk.Frame(self.root, bg=self.bg)
        self.InformationFrame.rowconfigure(0, weight = 1)
        self.InformationFrame.columnconfigure(0, weight = 3)
        self.InformationFrame.columnconfigure(1, weight=1)
        self.InformationFrame.grid(row = 0, column = 0, sticky=tk.N + tk.S + tk.E + tk.W)

        self.card = opponentCard
        self.StatsFrame = tk.Frame(self.InformationFrame, bg = self.bg)
        self.StatsFrame.columnconfigure(0, weight = 1)
        for i in range(8):
            self.StatsFrame.rowconfigure(i, weight = 1)
        self.StatsFrame.grid(row = 0, column = 1, sticky=tk.N + tk.S + tk.E + tk.W)

        self.cardLabel = tk.Label(self.StatsFrame, text="The opponent's card: ", font = self.font, bg = self.bg, fg = self.fg)
        self.nameLabel = tk.Label(self.StatsFrame, text=f"Name: {self.card.getName()}", font = self.font, bg = self.bg, fg = self.fg)
        self.countryLabel = tk.Label(self.StatsFrame, text=f"Country: {self.card.getCountry()}", font = self.font, bg = self.bg, fg = self.fg)
        self.firepowerLabel = tk.Label(self.StatsFrame, text=f"Firepower: {self.card.getFirepower()}", font = self.font, bg = self.bg, fg = self.fg)
        self.tonnageLabel = tk.Label(self.StatsFrame, text=f"Tonnage: {self.card.getTonnage()}", font = self.font, bg = self.bg, fg = self.fg)
        self.speedLabel = tk.Label(self.StatsFrame, text=f"Speed: {self.card.getSpeed()}", font = self.font, bg = self.bg, fg = self.fg)
        self.armourLabel = tk.Label(self.StatsFrame, text=f"Armour: {self.card.getArmour()}", font = self.font, bg = self.bg, fg = self.fg)
        self.opponentPlay = tk.Label(self.StatsFrame, text=f"The opponent is playing the attribute: {self.oStr}", font = self.font, bg = self.bg, fg = self.fg)

        self.cardLabel.grid(row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
        self.nameLabel.grid(row=1, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
        self.countryLabel.grid(row=2, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
        self.firepowerLabel.grid(row=3, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
        self.tonnageLabel.grid(row=4, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
        self.speedLabel.grid(row=5, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
        self.armourLabel.grid(row=6, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
        self.opponentPlay.grid(row=7, column=0, sticky=tk.N + tk.S + tk.E + tk.W)

        self.Image = tk.Label(self.InformationFrame, bg = self.bg)
        winWidth = self.windowWidth
        winHeight = self.windowHeight
        winWidth = int(winWidth * 0.75)
        winHeight = int(winHeight * 0.8)
        self.Image.grid(row = 0, column = 0, sticky=tk.N + tk.S + tk.E + tk.W)

        self.ok_button = tk.Button(self.root, text="Ok", command=lambda: self.continue_on(mainWin), font = self.font, bg = self.bg, fg = self.fg)
        self.ok_button.grid(row = 1, column = 0)

        self.root.mainloop()

    def continue_on(self, mainWin):
        self.root.quit()
        self.root.destroy()
        mainWin.rootWindow.deiconify()


class alertWindow:
    def __init__(self, labelText):
        self.root = tk.Tk()

        #self.windowWidth = 300
        #self.windowHeight = 200

        #self.screenWidth = self.root.winfo_screenwidth()
        #self.screenHeight = self.root.winfo_screenheight()

        #self.x = (self.screenWidth - self.windowWidth) // 2
        #self.y = (self.screenHeight - self.windowHeight) // 2

        #self.root.geometry(f"{self.windowWidth}x{self.windowHeight}+{self.x}+{self.y}")

        self.root.title("Alert")
        self.root.rowconfigure(0, weight=4)
        self.root.rowconfigure(1, weight=1)
        self.root.columnconfigure(0, weight = 1)
        self.label = tk.Label(self.root, text=labelText)
        self.label.grid(row = 0, column = 0, sticky=tk.N + tk.S + tk.W + tk.E)
        self.ok_button = tk.Button(self.root, text="Ok", command=self.continue_on)
        self.ok_button.grid(row = 1, column = 0, sticky=tk.N + tk.S + tk.W + tk.E)
        self.root.mainloop()

    def continue_on(self):
        self.root.quit()
        self.root.destroy()


class loginScreen:
    def __init__(self, informationFilePath: str):
        self.isLoggedIn = False
        self.storageArea = ""
        if informationFilePath != "":
            self.storageArea = informationFilePath + ".txt"
        self.root = tk.Tk()
        self.root.title("Sign in to access game")
        self.windowWidth = 400
        self.windowHeight = 300
        self.screenWidth = self.root.winfo_screenwidth()
        self.screenHeight = self.root.winfo_screenheight()
        self.x = (self.screenWidth - self.windowWidth) // 2
        self.y = (self.screenHeight - self.windowHeight) // 2
        self.root.geometry(f"{self.windowWidth}x{self.windowHeight}+{self.x}+{self.y}")

        self.loginButton = tk.Button(self.root, command=lambda: self.createLoginScreen(self.storageArea), text="Log In")
        self.createAccountButton = tk.Button(self.root, command=self.createAccountScreen, text="Create Account")

        if self.storageArea != "":
            self.loginButton.pack(fill="both", expand=True)
        else:
            self.createAccountButton.pack(fill="both", expand=True)

        self.root.mainloop()

    def createLoginScreen(self, informationFilePath: str):
        try:
            open(informationFilePath, "r")
        except FileNotFoundError:
            alertWindow("Error - user file can not be found. Please create another account.")
            return
        self.file = open(informationFilePath, "r")
        self.info = self.file.readlines()
        self.file.close()

        self.loginWindow = tk.Toplevel(self.root)
        self.loginWindow.title("Log in to continue")
        self.root.withdraw()
        self.windowWidth = 400
        self.windowHeight = 300
        self.screenWidth = self.root.winfo_screenwidth()
        self.screenHeight = self.root.winfo_screenheight()
        self.x = (self.screenWidth - self.windowWidth) // 2
        self.y = (self.screenHeight - self.windowHeight) // 2
        self.loginWindow.geometry(f"{self.windowWidth}x{self.windowHeight}+{self.x}+{self.y}")

        self.loginWindow.rowconfigure(0, weight = 4)
        self.loginWindow.rowconfigure(1, weight = 1)
        self.loginWindow.columnconfigure(0, weight = 1)

        self.loginFrame = tk.Frame(self.loginWindow)

        self.loginFrame.rowconfigure(0, weight = 1)
        self.loginFrame.rowconfigure(1, weight=1)

        self.loginFrame.columnconfigure(0, weight=4)
        self.loginFrame.columnconfigure(0, weight=1)

        self.usernameLabel = tk.Label(self.loginFrame, text = "Enter Username: ")
        self.passwordLabel = tk.Label(self.loginFrame, text = "Enter Password: ")

        self.usernameEntry = tk.Entry(self.loginFrame)
        self.passwordEntry = tk.Entry(self.loginFrame)
        self.loginButton = tk.Button(self.loginWindow, text="Log In!", command=self.verifyDetails)

        self.usernameLabel.grid(row = 0, column = 0, sticky=tk.N + tk.S + tk.E + tk.W)
        self.usernameEntry.grid(row = 0, column = 1, sticky=tk.N + tk.S + tk.E + tk.W)
        self.passwordLabel.grid(row = 1, column = 0, sticky=tk.N + tk.S + tk.E + tk.W)
        self.passwordEntry.grid(row = 1, column = 1, sticky=tk.N + tk.S + tk.E + tk.W)

        self.loginFrame.grid(row = 0, column = 0, sticky=tk.N + tk.S + tk.E + tk.W)
        self.loginButton.grid(row = 1, column = 0, sticky=tk.N + tk.S + tk.E + tk.W)

    def verifyDetails(self):
        # "Username: {...}"
        # "Password: {...}"
        userinfo = self.info[0][0:(len(self.info[0])-1)]
        userinfo = userinfo[10:]

        passwordinfo = self.info[1][0:(len(self.info[1])-1)]
        passwordinfo = passwordinfo[10:]

        if userinfo == self.usernameEntry.get() and passwordinfo == self.passwordEntry.get():
            self.loginWindow.withdraw()
            self.root.withdraw()
            alertWindow(f"Welcome, {userinfo}")
            self.root.quit()
            self.root.destroy()
            self.isLoggedIn = True
        else:
            alertWindow("Error - details do not match")
            self.loginWindow.quit()
            self.loginWindow.destroy()
            self.root.deiconify()


    def createAccountScreen(self):
        self.root.withdraw()
        self.AccountCreationScreen = tk.Toplevel(self.root)
        self.AccountCreationScreen.title("Create Account")

        self.windowWidth = 400
        self.windowHeight = 300
        self.screenWidth = self.root.winfo_screenwidth()
        self.screenHeight = self.root.winfo_screenheight()
        self.x = (self.screenWidth - self.windowWidth) // 2
        self.y = (self.screenHeight - self.windowHeight) // 2
        self.AccountCreationScreen.geometry(f"{self.windowWidth}x{self.windowHeight}+{self.x}+{self.y}")

        self.AccountCreationScreen.columnconfigure(0, weight = 1)
        self.AccountCreationScreen.rowconfigure(0, weight = 4)
        self.AccountCreationScreen.rowconfigure(1, weight = 1)

        self.acctFrame = tk.Frame(self.AccountCreationScreen)
        for i in range(3):
            self.acctFrame.rowconfigure(i, weight = 1)
        self.acctFrame.columnconfigure(0, weight = 1)
        self.acctFrame.columnconfigure(1, weight=1)

        self.usernameLabel = tk.Label(self.acctFrame, text="Enter username: ")
        self.passwordLabel = tk.Label(self.acctFrame, text="Enter password: ")
        self.repasswordLabel = tk.Label(self.acctFrame, text="Re-Enter password: ")
        self.usernameEntry = tk.Entry(self.acctFrame)
        self.passwordEntry = tk.Entry(self.acctFrame)
        self.repasswordEntry = tk.Entry(self.acctFrame)

        self.createAccountButtonConfirm = tk.Button(self.AccountCreationScreen, text = "Create Account!", command=self.verifyIfValid)

        self.usernameLabel.grid(row = 0, column = 0, sticky=tk.N + tk.S + tk.E + tk.W)
        self.passwordLabel.grid(row = 1, column = 0, sticky=tk.N + tk.S + tk.E + tk.W)
        self.repasswordLabel.grid(row = 2, column = 0, sticky=tk.N + tk.S + tk.E + tk.W)
        self.usernameEntry.grid(row = 0, column = 1, sticky=tk.N + tk.S + tk.E + tk.W)
        self.passwordEntry.grid(row = 1, column = 1, sticky=tk.N + tk.S + tk.E + tk.W)
        self.repasswordEntry.grid(row = 2, column = 1, sticky=tk.N + tk.S + tk.E + tk.W)

        self.acctFrame.grid(row = 0, column = 0, sticky=tk.N + tk.S + tk.E + tk.W)
        self.createAccountButtonConfirm.grid(row = 1, column = 0, sticky=tk.N + tk.S + tk.E + tk.W)

    def verifyIfValid(self):
        if len(self.usernameEntry.get()) < 6:
            alertWindow("Username too short!")
            return
        elif len(self.usernameEntry.get()) > 20:
            alertWindow("Username too long!")
            return

        if len(self.passwordEntry.get()) < 8:
            alertWindow("Password too short!")
            return
        elif len(self.passwordEntry.get()) > 40:
            alertWindow("Very secure password, but it is too long!")
            return

        if self.passwordEntry.get() == self.repasswordEntry.get():
            self.storageArea = f"{self.usernameEntry.get()}.txt"
            data = [f"Username: {self.usernameEntry.get()}\n"
                    f"Password: {self.passwordEntry.get()}\n"
                    "Wins: 0\n"
                    "Losses: 0\n"
                    "Win/Loss Ratio: 0\n"
            ]
            file = open(self.storageArea, "w")
            file.writelines(data)
            file.close()

            self.root.withdraw()
            self.AccountCreationScreen.withdraw()

            alertWindow("Account creation was successful!")
            self.isLoggedIn = True
            self.AccountCreationScreen.quit()
            self.AccountCreationScreen.destroy()
            self.root.quit()
            self.root.destroy()
            return
        else:
            alertWindow("Passwords do not match!")
            return


    def getFileStorageArea(self):
        return self.storageArea

    def wasSuccessful(self):
        return self.isLoggedIn
    
class gameState(Enum):
    STATE_ATTACK = 0
    STATE_ATTRIBUTES = 1
    STATE_WINNER = 2
    CONTINUE_ON = 3

class matchResult(Enum):
    WIN = 0
    LOSE = 1
    TIE = 2

class matchScreen:
    def __init__(self, mainWin : mainWindow, isPlayerAttacking: bool, card1 : Card, card2 : Card, attributePlayed : CardValues, hasPlayerWon: matchResult, matchNumber: int):
        self.Theme = mainWin.getTheme()
        self.Theme = colorThemes[self.Theme]
        self.bg = self.Theme[0]
        self.fg = self.Theme[1]
        self.isPlayerAttacking = isPlayerAttacking
        
        self.font: tuple = (mainWin.getFont()[0], int(mainWin.getFont()[1]))
        self.gameState : gameState = gameState.STATE_ATTACK
        self.attributePlayed = attributePlayed
        self.hasPlayerWon = hasPlayerWon

        self.playerCard = card1
        self.opponentCard = card2

        self.root = tk.Toplevel(mainWin.rootWindow, bg = self.bg)
        self.root.config(background = self.bg)
        self.root.geometry(f"{mainWin.rootWindow.winfo_geometry()}")
        self.root.title(f"Match {matchNumber}")
        mainWin.rootWindow.withdraw()
        self.root.bind("<Escape>", lambda x: self.exit(mainWin))
        self.root.bind("<Return>", lambda x: self.next(mainWin))

        # ROWCONFIG, COLUMNCONFIG
        self.root.columnconfigure(0, weight = 1)
        self.root.rowconfigure(0, weight = 1)
        self.root.rowconfigure(1, weight = 10)
        self.root.rowconfigure(2, weight = 1)

        # Root widgets
        self.matchInfoLabel = tk.Label(self.root, text=f"Match {matchNumber}", bg = self.bg, font = self.font, fg = self.fg)
        self.matchInfoLabel.grid(row = 0, column = 0, sticky = tk.N + tk.S + tk.E + tk.W)
        self.matchFrame = tk.Frame(self.root, bg = self.bg)
        self.matchFrame.grid(row = 1, column = 0, sticky = tk.N + tk.S + tk.E + tk.W)
        self.buttonFrame = tk.Frame(self.root, bg = self.bg)
        self.buttonFrame.grid(row = 2, column = 0, sticky = tk.N + tk.S + tk.E + tk.W)

        # buttonFrame config and widgets
        self.buttonFrame.rowconfigure(0, weight = 1)
        self.buttonFrame.columnconfigure(0, weight = 4)
        self.buttonFrame.columnconfigure(1, weight = 1)
        self.continueButton = tk.Button(self.buttonFrame, text="<Next>", bg = self.bg, font = self.font, fg = self.fg, command=lambda: self.next(mainWin))
        self.continueButton.grid(row = 0, column = 0, sticky = tk.N + tk.S + tk.E + tk.W)
        self.exitButton = tk.Button(self.buttonFrame, text="<Skip>", bg = self.bg, font = self.font, fg = self.fg, command=lambda: self.exit(mainWin))
        self.exitButton.grid(row = 0, column = 1, sticky = tk.N + tk.S + tk.E + tk.W)

        # Match Frame
        self.matchFrame.rowconfigure(0, weight = 1)
        self.matchFrame.columnconfigure(0, weight = 3)
        self.matchFrame.columnconfigure(1, weight = 1)

        self.playersFrame = tk.Frame(self.matchFrame, bg = self.bg)
        self.playersFrame.grid(row = 0, column = 0, sticky = tk.N + tk.S + tk.E + tk.W)
        self.matchTimelineFrame = tk.Frame(self.matchFrame, bg = self.bg)
        self.matchTimelineFrame.grid(row = 0, column = 1, sticky = tk.N + tk.S + tk.E + tk.W)
        self.matchTimelineFrame.columnconfigure(0, weight = 1)
        for i in range(5):
            self.matchTimelineFrame.rowconfigure(i, weight=1)

        # playersFrame
        self.playersFrame.rowconfigure(0, weight = 1)
        self.playersFrame.rowconfigure(1, weight = 1)
        self.playersFrame.columnconfigure(0, weight = 1)

        self.player1Frame = tk.Frame(self.playersFrame, bg = self.bg)
        self.player1Frame.grid(row = 0, column = 0, sticky = tk.N + tk.S + tk.E + tk.W)
        self.player2Frame = tk.Frame(self.playersFrame, bg = self.bg)
        self.player2Frame.grid(row = 1, column = 0, sticky = tk.N + tk.S + tk.E + tk.W)

        # player1Frame
        self.player1Frame.rowconfigure(0, weight = 1)
        self.player1Frame.rowconfigure(1, weight = 4)
        self.player1Frame.columnconfigure(0, weight = 1)

        self.player1Label = tk.Label(self.player1Frame, bg = self.bg, fg = self.fg, font = self.font, text="Your card")
        self.player1Label.grid(row = 0, column = 0, sticky = tk.N + tk.S + tk.E + tk.W)
        self.player1CardFrame = tk.Frame(self.player1Frame, bg = self.bg)
        self.player1CardFrame.grid(row = 1, column = 0, sticky = tk.N + tk.S + tk.E + tk.W)

        # player1CardFrame
        self.player1CardFrame.rowconfigure(0, weight = 1)
        self.player1CardFrame.columnconfigure(0, weight = 3)
        self.player1CardFrame.columnconfigure(1, weight = 1)

        self.player1Image = tk.Label(self.player1CardFrame, bg = self.bg)
        self.player1Image.grid(row = 0, column = 0, sticky = tk.N + tk.S + tk.E + tk.W)

        self.player1StatsFrame = tk.Frame(self.player1CardFrame, bg = self.bg)
        self.player1StatsFrame.grid(row = 0, column = 1, sticky = tk.N + tk.S + tk.E + tk.W)

        # player1StatsFrame
        for i in range(6):
            self.player1StatsFrame.rowconfigure(i, weight = 1)

        # Name, country, firepower, tonnage, speed, armour
        self.player1CardName = tk.Label(self.player1StatsFrame, bg = self.bg, fg = self.fg, font = self.font, text=f"Name: {card1.getName()}")
        self.player1CardName.grid(row = 0, column = 0, sticky = tk.N + tk.S + tk.E + tk.W)

        self.player1CardCountry = tk.Label(self.player1StatsFrame, bg = self.bg, fg = self.fg, font = self.font, text=f"Country: {card1.getCountry()}")
        self.player1CardCountry.grid(row = 1, column = 0, sticky = tk.N + tk.S + tk.E + tk.W)

        self.player1CardFirepower = tk.Label(self.player1StatsFrame, bg = self.bg, fg = self.fg, font = self.font, text=f"Firepower: {card1.getFirepower()}")
        self.player1CardFirepower.grid(row = 2, column = 0, sticky = tk.N + tk.S + tk.E + tk.W)

        self.player1CardTonnage = tk.Label(self.player1StatsFrame, bg = self.bg, fg = self.fg, font = self.font, text=f"Tonnage: {card1.getTonnage()}")
        self.player1CardTonnage.grid(row = 3, column = 0, sticky = tk.N + tk.S + tk.E + tk.W)

        self.player1CardSpeed = tk.Label(self.player1StatsFrame, bg = self.bg, fg = self.fg, font = self.font, text=f"Speed: {card1.getSpeed()}")
        self.player1CardSpeed.grid(row = 4, column = 0, sticky = tk.N + tk.S + tk.E + tk.W)

        self.player1CardArmour = tk.Label(self.player1StatsFrame, bg = self.bg, fg = self.fg, font = self.font, text=f"Armour: {card1.getArmour()}")
        self.player1CardArmour.grid(row = 5, column = 0, sticky = tk.N + tk.S + tk.E + tk.W)


        # player2Frame
        self.player2Frame.rowconfigure(0, weight = 1)
        self.player2Frame.rowconfigure(1, weight = 4)
        self.player2Frame.columnconfigure(0, weight = 1)

        self.player2Label = tk.Label(self.player2Frame, bg = self.bg, fg = self.fg, font = self.font, text="Opponent's card")
        self.player2Label.grid(row = 0, column = 0, sticky = tk.N + tk.S + tk.E + tk.W)
        self.player2CardFrame = tk.Frame(self.player2Frame, bg = self.bg)
        self.player2CardFrame.grid(row = 1, column = 0, sticky = tk.N + tk.S + tk.E + tk.W)

        # player1CardFrame
        self.player2CardFrame.rowconfigure(0, weight = 1)
        self.player2CardFrame.columnconfigure(0, weight = 3)
        self.player2CardFrame.columnconfigure(1, weight = 1)

        self.player2Image = tk.Label(self.player2CardFrame, bg = self.bg)
        self.player2Image.grid(row = 0, column = 0, sticky = tk.N + tk.S + tk.E + tk.W)

        self.player2StatsFrame = tk.Frame(self.player2CardFrame, bg = self.bg)
        self.player2StatsFrame.grid(row = 0, column = 1, sticky = tk.N + tk.S + tk.E + tk.W)

        # player2StatsFrame
        for i in range(6):
            self.player2StatsFrame.rowconfigure(i, weight = 1)

        # Name, country, firepower, tonnage, speed, armour
        self.player2CardName = tk.Label(self.player2StatsFrame, bg = self.bg, fg = self.fg, font = self.font, text=f"Name: {card2.getName()}")
        self.player2CardName.grid(row = 0, column = 0, sticky = tk.N + tk.S + tk.E + tk.W)

        self.player2CardCountry = tk.Label(self.player2StatsFrame, bg = self.bg, fg = self.fg, font = self.font, text=f"Country: {card2.getCountry()}")
        self.player2CardCountry.grid(row = 1, column = 0, sticky = tk.N + tk.S + tk.E + tk.W)

        self.player2CardFirepower = tk.Label(self.player2StatsFrame, bg = self.bg, fg = self.fg, font = self.font, text=f"Firepower: {card2.getFirepower()}")
        self.player2CardFirepower.grid(row = 2, column = 0, sticky = tk.N + tk.S + tk.E + tk.W)

        self.player2CardTonnage = tk.Label(self.player2StatsFrame, bg = self.bg, fg = self.fg, font = self.font, text=f"Tonnage: {card2.getTonnage()}")
        self.player2CardTonnage.grid(row = 3, column = 0, sticky = tk.N + tk.S + tk.E + tk.W)

        self.player2CardSpeed = tk.Label(self.player2StatsFrame, bg = self.bg, fg = self.fg, font = self.font, text=f"Speed: {card2.getSpeed()}")
        self.player2CardSpeed.grid(row = 4, column = 0, sticky = tk.N + tk.S + tk.E + tk.W)

        self.player2CardArmour = tk.Label(self.player2StatsFrame, bg = self.bg, fg = self.fg, font = self.font, text=f"Armour: {card2.getArmour()}")
        self.player2CardArmour.grid(row = 5, column = 0, sticky = tk.N + tk.S + tk.E + tk.W)


        self.root.mainloop()

    def getStrFromAttrPlayed(self) -> str:
        if self.attributePlayed == CardValues.ARMOUR:
            return "Armour"
        elif self.attributePlayed == CardValues.FIREPOWER:
            return "Firepower"
        elif self.attributePlayed == CardValues.SPEED:
            return "Speed"
        else:
            return "Tonnage"

    def exit(self, mainWin: mainWindow):
        self.root.quit()
        self.root.destroy()
        mainWin.rootWindow.deiconify()

    def next(self, mainWin: mainWindow):
        if self.gameState == gameState.STATE_ATTACK:
            self.gameState = gameState.STATE_ATTRIBUTES
            if self.isPlayerAttacking:
                label = tk.Label(self.matchTimelineFrame, text = f"You played: {self.getStrFromAttrPlayed()}", bg = self.bg, fg = self.fg, font = self.font)
            else:
                label = tk.Label(self.matchTimelineFrame, text = f"The opponent played: {self.getStrFromAttrPlayed()}", bg = self.bg, fg = self.fg, font = self.font)
            label.grid(row = 0, column = 0, sticky = tk.N + tk.S + tk.E + tk.W)
            return
        
        if self.gameState == gameState.STATE_ATTRIBUTES:
            self.gameState = gameState.STATE_WINNER
            if self.attributePlayed == CardValues.FIREPOWER:
                label1 = tk.Label(self.matchTimelineFrame, text = f"Your firepower: {self.playerCard.getFirepower()}", bg = self.bg, fg = self.fg, font = self.font)
                label1.grid(row = 1, column = 0, sticky = tk.N + tk.S + tk.E + tk.W)

                label2 = tk.Label(self.matchTimelineFrame, text = f"Opponent's firepower: {self.opponentCard.getFirepower()}", bg = self.bg, fg = self.fg, font = self.font)
                label2.grid(row = 2, column = 0, sticky = tk.N + tk.S + tk.E + tk.W)

            elif self.attributePlayed == CardValues.TONNAGE:
                label1 = tk.Label(self.matchTimelineFrame, text = f"Your tonnage: {self.playerCard.getTonnage()}", bg = self.bg, fg = self.fg, font = self.font)
                label1.grid(row = 1, column = 0, sticky = tk.N + tk.S + tk.E + tk.W)

                label2 = tk.Label(self.matchTimelineFrame, text = f"Opponent's tonnage: {self.opponentCard.getTonnage()}", bg = self.bg, fg = self.fg, font = self.font)
                label2.grid(row = 2, column = 0, sticky = tk.N + tk.S + tk.E + tk.W)

            elif self.attributePlayed == CardValues.SPEED:
                label1 = tk.Label(self.matchTimelineFrame, text = f"Your speed: {self.playerCard.getSpeed()}", bg = self.bg, fg = self.fg, font = self.font)
                label1.grid(row = 1, column = 0, sticky = tk.N + tk.S + tk.E + tk.W)

                label2 = tk.Label(self.matchTimelineFrame, text = f"Opponent's speed: {self.opponentCard.getSpeed()}", bg = self.bg, fg = self.fg, font = self.font)
                label2.grid(row = 2, column = 0, sticky = tk.N + tk.S + tk.E + tk.W)
                
            else:
                label1 = tk.Label(self.matchTimelineFrame, text = f"Your armour: {self.playerCard.getArmour()}", bg = self.bg, fg = self.fg, font = self.font)
                label1.grid(row = 1, column = 0, sticky = tk.N + tk.S + tk.E + tk.W)

                label2 = tk.Label(self.matchTimelineFrame, text = f"Opponent's armour: {self.opponentCard.getArmour()}", bg = self.bg, fg = self.fg, font = self.font)
                label2.grid(row = 2, column = 0, sticky = tk.N + tk.S + tk.E + tk.W)
            return

        if self.gameState == gameState.STATE_WINNER:
            self.gameState = gameState.CONTINUE_ON
            if self.hasPlayerWon == matchResult.WIN:
                label = tk.Label(self.matchTimelineFrame, text = f"You won! You gain your opponent's card, {self.opponentCard.getName()}\n You both move onto the next card.", bg = self.bg, fg = self.fg, font = self.font)
            elif self.hasPlayerWon == matchResult.LOSE:
                label = tk.Label(self.matchTimelineFrame, text = f"Your opponent won, and was given your card, {self.playerCard.getName()}\n You both move onto the next card.", bg = self.bg, fg = self.fg, font = self.font)
            else:
                label = tk.Label(self.matchTimelineFrame, text = f"Neither of you won, and you both move onto your next card.", bg = self.bg, fg = self.fg, font = self.font)
            label.grid(row = 3, column = 0, sticky = tk.N + tk.S + tk.E + tk.W)
            return
        
        if self.gameState == gameState.CONTINUE_ON:
            self.root.quit()
            self.root.destroy()
            mainWin.rootWindow.deiconify()



