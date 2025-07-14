from cards import Cards
from cardAttributes import Card, Player
from random import randint
from tkinterwidgets import mainWindow, loginScreen, alertWindow


global thePlayer, theOpponent, pickedCards
pickedCards = []

def generateCards():
    cardArray: list[Card] = []
    for i in range(5):
        newNum = randint(0,19)

        # Get unique values
        while (newNum in pickedCards) == True:
            newNum = randint(0,19)
        pickedCards.append(newNum)

        cardArray.append(Cards[newNum])
    return cardArray

def playGame() -> None:
    user = input("Enter username, leave blank if you have none: ")
    thePlayer = Player(100) # 5 card hand size
    theOpponent = Player(10)

    playerHand = generateCards()
    opponentHand = generateCards()

    for i in range(5):
        thePlayer.addCardToHand(playerHand[i])
        theOpponent.addCardToHand(opponentHand[i])

    login = loginScreen(user)
    if login.wasSuccessful():
        mainWindow(thePlayer, theOpponent, login.getFileStorageArea())
    else:
        alertWindow("Please re-run and either sign in or create an account.")
    return