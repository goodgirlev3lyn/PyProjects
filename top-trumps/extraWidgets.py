import tkinter as tk
from cardAttributes import Card, CardValues, Player
from cards import Cards
from tkinterwidgets import mainWindow, colorThemes
import pathlib, os, time

from dataStructures import Queue, Stack

testCard1 = Cards[0]
testCard2 = Cards[1]

testCard2.getImage()

class matchScreen:
    def __init__(self, isPlayerAttacking: bool, card1 : Card, card2 : Card, attributePlayed : CardValues, hasPlayerWon: bool, matchNumber: int, theme : str, font : tuple):
        #if mainWindow == None:
        self.Theme = colorThemes[theme]
        #self.Theme = mainWin.getTheme()
        self.bg = self.Theme[0]
        self.fg = self.Theme[1]
        self.font = font

        if isPlayerAttacking:
            self.player1Name = "Your Card:"
            self.player2Name = "Opponent's Card:"
        else:
            self.player1Name = "Opponent's Card:"
            self.player2Name = "Your Card:"
        #self.font = (mainWin.getFont()[0], mainWin.getFont()[1])

        self.root = tk.Tk()
        self.root.config(background = self.bg)
        self.root.geometry("1280x720")
        #self.root = tk.Toplevel(mainWin.rootWindow, bg = self.bg)
        self.root.title("Match")
        # bg = self.bg, font = self.font, fg = self.fg

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
        self.continueButton = tk.Button(self.buttonFrame, text="<Next>", bg = self.bg, font = self.font, fg = self.fg, command=self.next)
        self.continueButton.grid(row = 0, column = 0, sticky = tk.N + tk.S + tk.E + tk.W)
        self.exitButton = tk.Button(self.buttonFrame, text="<Skip>", bg = self.bg, font = self.font, fg = self.fg, command=self.exit)
        self.exitButton.grid(row = 0, column = 1, sticky = tk.N + tk.S + tk.E + tk.W)

        # Match Frame
        self.matchFrame.rowconfigure(0, weight = 1)
        self.matchFrame.columnconfigure(0, weight = 3)
        self.matchFrame.columnconfigure(1, weight = 1)

        self.playersFrame = tk.Frame(self.matchFrame, bg = self.bg)
        self.playersFrame.grid(row = 0, column = 0, sticky = tk.N + tk.S + tk.E + tk.W)
        self.matchTimelineFrame = tk.Frame(self.matchFrame, bg = self.bg)
        self.matchTimelineFrame.grid(row = 0, column = 1, sticky = tk.N + tk.S + tk.E + tk.W)

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

        self.player1Label = tk.Label(self.player1Frame, bg = self.bg, fg = self.fg, font = self.font, text=f"{self.player1Name}")
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

        self.player2Label = tk.Label(self.player2Frame, bg = self.bg, fg = self.fg, font = self.font, text=self.player2Name)
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

    def exit(self):
        self.root.quit()
        self.root.destroy()

    def next(self):
        pass