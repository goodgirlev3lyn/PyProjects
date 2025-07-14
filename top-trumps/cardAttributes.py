from dataStructures import Queue
from enum import Enum


class Card:
    def __init__(self, name: str, country: str, firepower: int, tonnage: int, speed: int, armour: int, imageSource: str = "img/yamato.jpg"):
        self.Name = name
        self.Country = country
        self.Firepower = firepower
        self.Tonnage = tonnage
        self.Speed = speed
        self.Armour = armour
        self.Image = imageSource

    def getFirepower(self) -> int:
        """
        Returns the firepower attribute of the card
        """
        return self.Firepower

    def getTonnage(self) -> int:
        """
        Returns the tonnage attribute of the card
        """
        return self.Tonnage

    def getSpeed(self) -> int:
        """
        Returns the speed attribute of the card
        """
        return self.Speed

    def getArmour(self) -> int:
        """
        Returns the armour attribute of the card
        """
        return self.Armour

    def getName(self) -> str:
        """
        Returns the name attribute of the card
        """
        return self.Name

    def getCountry(self) -> str:
        """
        Returns the country attribute of the card
        """
        return self.Country

    def getImage(self) -> str:
        """
        Returns the image filename for the card
        """
        return self.Image

    def __str__(self) -> str:
        return f"Name: {self.Name}\n Country: {self.Country}\n Firepower: {self.Firepower}\n Tonnage: {self.Tonnage}\n Speed: {self.Speed}\n Armour: {self.Armour}\n Image Source: {self.Image}\n"

class Player:
    def __init__(self, handSize: int):
        self.Hand = Queue(handSize)

    def addCardToHand(self, card: Card):
        """
        Adds a card to the player's hand
        """
        self.Hand.enQueue(card)

    def getTopCard(self) -> Card:
        """
        Return the top card of the stack
        USE Hand.isEmptyHand() TO AVOID CALLING IF THE HAND IS EMPTY
        """
        return self.Hand.peek()

    def removeCard(self) -> Card:
        """
        Returns the top card
        USE Hand.isEmptyHand() TO AVOID CALLING IF THE HAND IS EMPTY
        """
        return self.Hand.deQueue()

    def __str__(self):
        return self.Hand.__str__()

    def getCardCount(self) -> int:
        """
        Returns the amount of cards in the hand
        """
        return self.Hand.getSize()

    def moveOntoNextCard(self) -> None:
        """
        Puts the first card at the back of the deck and moves onto the next card
        """
        self.addCardToHand(self.removeCard())
        return

    def isEmptyHand(self) -> bool:
        """
        Returns True if the hand has no cards, else returns False
        """
        return self.Hand.isEmpty()


class CardValues(Enum):
    """
    Enum for CardValues, has attributes FIREPOWER, TONNAGE, SPEED, ARMOUR
    """
    NULL = 0
    FIREPOWER = 1
    TONNAGE = 2
    SPEED = 3
    ARMOUR = 4


