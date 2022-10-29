# imports
import pygame
import random
from pygameRogers import Game
from pygameRogers import Room
from pygameRogers import GameObject
from pygameRogers import TextRectangle
from pygameRogers import Alarm

# create a new game
g = Game(1100, 600)

# establish colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# create resources
titleFont = g.makeFont("Arial", 38)
gameFont = g.makeFont("Arial", 22)
wFont = g.makeFont("Arial", 120)
simpleBackground = g.makeBackground(BLACK)

# create rooms
room1 = Room("Start Menu", simpleBackground)
g.addRoom(room1)
room2 = Room("Game", simpleBackground)
g.addRoom(room2)
room3 = Room("Win or Lose?", simpleBackground)
g.addRoom(room3)

# add cards into the game
redCards = []
for i in range(0, 13):
    redCards.append(g.makeSpriteImage("unoCards\Red" + str(i) + ".png"))
yellowCards = []
for i in range(0, 13):
    yellowCards.append(g.makeSpriteImage("unoCards\Yellow" + str(i) + ".png"))
greenCards = []
for i in range(0, 13):
    greenCards.append(g.makeSpriteImage("unoCards\Green" + str(i) + ".png"))
blueCards = []
for i in range(0, 13):
    blueCards.append(g.makeSpriteImage("unoCards\Blue" + str(i) + ".png"))
wildCards = []
for i in range(0, 2):
    wildCards.append(g.makeSpriteImage("unoCards\Wild" + str(i) + ".png"))
topCard = g.makeSpriteImage("unoCards\Top.png")

# add title to the game
title = TextRectangle("UNO", g.windowWidth/2 - 50, 250, titleFont, WHITE)
room1.addObject(title)

# class for room 1 start button


class start(TextRectangle):
    def __init__(self, text, xPos, yPos, font, textColour, buttonWidth, buttonHeight, buttonColour):
        TextRectangle.__init__(self, text, xPos, yPos, font, textColour, buttonWidth, buttonHeight, buttonColour)

    def update(self):
        self.checkMousePressedOnMe(event)
        if self.mouseHasPressedOnMe and event.type == pygame.MOUSEBUTTONUP:
            g.nextRoom()
            self.mouseHasPressedOnMe == False


# add start button to the game
startButton = start("Start", (g.windowWidth/2)-90,325, titleFont, BLACK, 150, 50, WHITE)
room1.addObject(startButton)

# class for win or lose text


class result(TextRectangle):
    def __init__(self, text, xPos, yPos, font, textColour):
        TextRectangle.__init__(self, text, xPos, yPos, font, textColour)


# win or lose (appended later in the code)
w = result("You Won!", g.windowWidth/2 - 200, 250, wFont, WHITE)
l = result("You Lost!", g.windowWidth/2 - 200, 250, wFont, WHITE)

# cards class


class card(GameObject):
    def __init__(self, picture, value, suit):
        GameObject.__init__(self, picture)
        self.value = value
        self.suit = suit

    # update game state based on inputs
    def update(self):
        # check mouse clikc
        self.checkMousePressedOnMe(event)
        # if mouse is clicked call click action function
        if self.mouseHasPressedOnMe and event.type == pygame.MOUSEBUTTONUP:
            self.mClickAction()

    # Mouse Click Action
    def mClickAction(self):
        # If suits are the same or wild card is played
        if self.suit == played.playedCard[-1].suit or self.suit == "W" or played.playedCard[-1].suit == "W":
            if self.suit == "W":
                if self.value == 0:
                    p.playCard(self)
                    played.addCard(self)
                if self.value == 1:
                    p.playCard(self)
                    played.addCard(self)
                    for i in range(0, 4):
                        card = d.deal()
                        c.takeACard(card)
                    c.timerP.setAlarm(1000)
            elif self.value == 10 or self.value == 11:
                p.playCard(self)
                played.addCard(self)
            elif self.value == 12:
                p.playCard(self)
                played.addCard(self)
                for i in range(0, 2):
                    Card = d.deal()
                    c.takeACard(Card)
                c.timerP.setAlarm(1000)
            else:
                p.playCard(self)
                played.addCard(self)
                c.timerP.setAlarm(1000)
        elif self.value == played.playedCard[-1].value:
            if self.value == 10 or self.value == 11:
                p.playCard(self)
                played.addCard(self)
            elif self.value == 12:
                p.playCard(self)
                played.addCard(self)
                for i in range(0, 2):
                    Card = d.deal()
                    c.takeACard(Card)
                c.timerP.setAlarm(1000)
            else:
                p.playCard(self)
                played.addCard(self)
                c.timerP.setAlarm(1000)
        self.mouseHasPressedOnMe = False

    def __str__(self):
        return str(self.value) + self.suit


class Deck(GameObject):
    def __init__(self, picture, xPos, yPos):
        GameObject.__init__(self, picture)
        self.rect.x = xPos
        self.rect.y = yPos
        self.fullDeck = []

        for i in range(len(redCards)):
            c = card(redCards[i], i, "R")
            self.fullDeck.append(c)
        for i in range(len(yellowCards)):
            c = card(yellowCards[i], i, "Y")
            self.fullDeck.append(c)
        for i in range(len(greenCards)):
            c = card(greenCards[i], i, "G")
            self.fullDeck.append(c)
        for i in range(len(blueCards)):
            c = card(blueCards[i], i, "B")
            self.fullDeck.append(c)
        for i in range(len(wildCards)):
            c = card(wildCards[i], i, "W")
            self.fullDeck.append(c)

        random.shuffle(self.fullDeck)
        startCard = self.fullDeck[0]
        startCard.rect.x = 350
        startCard.rect.y = 300
        played.playedCard.append(startCard)
        del self.fullDeck[0]
        room2.addObject(startCard)

    def update(self):
        self.checkMousePressedOnMe(event)
        if self.mouseHasPressedOnMe and event.type == pygame.MOUSEBUTTONUP:
            self.mClickAction()

    def mClickAction(self):

        card = self.deal()
        p.takeACard(card)
        c.timerP.setAlarm(2000)
        self.mouseHasPressedOnMe = False

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        if len(self.fullDeck) > 0:
            c = self.fullDeck[0]
            del self.fullDeck[0]

            if len(self.fullDeck) == 0:
                self.kill()
            return c

    def __str__(self):

        s = ""
        for card in self.fullDeck:
            s = s + str(card) + " "
        s = "Deck:\n" + s + "\n"
        return s


class player(GameObject):
    def __init__(self, xPos, yPos):
        GameObject.__init__(self)
        self.startX = xPos
        self.startY = yPos
        self.hand = []
        self.cardsInHand = 0

    def takeACard(self, card):
        self.hand.append(card)
        card.rect.x = (self.cardsInHand * (card.rect.width + 4)) + self.startX
        card.rect.y = self.startY
        self.cardsInHand += 1

        room2.addObject(card)

    def playCard(self, card):

        for c in self.hand:
            c.kill()

        self.hand.remove(card)
        self.cardsInHand -= 1

        for i in range(0, self.cardsInHand):
            self.hand[i].rect.x = (i*(card.rect.width + 4)) + self.startX
            self.hand[i].rect.y = self.startY
            room2.addObject(self.hand[i])

    def __str__(self):
        s = ""
        for card in self.hand:
            s = s + str(card) + " "
        s = "Player:\n" + s + "\n"
        return s


class cpu(GameObject):
    def __init__(self, xPos, yPos):
        GameObject.__init__(self)
        self.startX = xPos
        self.startY = yPos
        self.timerP = Alarm()
        self.timerW = Alarm()
        self.computerHand = []
        self.computerCardsInHand = 0
        self.played = False

    def playCard(self, card):

        for c in self.computerHand:
            c.kill()
        self.computerHand.remove(card)
        self.computerCardsInHand -= 1

        for i in range(0, (self.computerCardsInHand)):
            self.computerHand[i].rect.x = (
                i*(card.rect.width + 4) + self.startX)
            self.computerHand[i].rect.y = 450
            room2.addObject(self.computerHand[i])

    def update(self):
        if self.timerP.finished():
           self.played = False
           for i in range(0, self.computerCardsInHand):
               if self.computerHand[i].suit == played.playedCard[-1].suit or self.computerHand[i].suit == "W" or played.playedCard[-1].suit == "W":
                   if self.computerHand[i].suit == "W":
                       # change color
                       if self.computerHand[i].value == 0:
                           cardCurrent = self.computerHand[i]
                           c.playCard(self.computerHand[i])
                           played.addCard(cardCurrent)
                           pygame.time.wait(1500)
                           q = random.randint(0, self.computerCardsInHand-1)
                           c.playCard(self.computerHand[q])
                           played.addCard(self.computerHand[q])
                           self.played = True
                           break
                       # plus 4
                       if self.computerHand[i].value == 1:
                           cardCurrent = self.computerHand[i]
                           c.playCard(self.computerHand[i])
                           played.addCard(cardCurrent)
                           for i in range(0, 4):
                               card = d.deal()
                               p.takeACard(card)
                           pygame.time.wait(1500)
                           c.playCard(self.computerHand[0])
                           played.addCard(self.computerHand[0])
                           self.played = True
                           break
                   # change direction or skip a turn
                   elif self.computerHand[i].value == 10 or self.computerHand[i].value == 11:
                       cardCurrent = self.computerHand[i]
                       c.playCard(self.computerHand[i])
                       played.addCard(cardCurrent)
                       pygame.time.wait(2000)
                       
                       for i in range(0, len(self.computerHand)):
                           if self.computerHand[i].suit == played.playedCard[-1].suit:
                               cardCurrent = self.computerHand[i]
                               c.playCard(self.computerHand[i])
                               played.addCard(cardCurrent)
                               self.played = True
                               break

                           elif self.computerHand[i].value == played.playedCard[-1].value:
                               cardCurrent = self.computerHand[i]
                               c.playCard(self.computerHand[i])
                               played.addCard(cardCurrent)
                               self.played = True
                               break
                       if self.played == False:
                           card = d.deal()
                           c.takeACard(card)
                           self.played = True
                       break
                           
                   elif self.computerHand[i].value == 12:
                       cardCurrent = self.computerHand[i]
                       c.playCard(self.computerHand[i])
                       played.addCard(cardCurrent)
                       for i in range(0, 2):
                           Card = d.deal()
                           p.takeACard(Card)
                       self.played = True
                       break

                       
                    # normal card/ same color
                   else:
                        cardCurrent = self.computerHand[i]
                        c.playCard(self.computerHand[i])
                        played.addCard(cardCurrent)
                        self.played = True
                        break
               # same number
               elif self.computerHand[i].value == played.playedCard[-1].value:
                   if self.computerHand[i].suit == "W":
                       # change color

                       if self.computerHand[i].value == 0:
                           cardCurrent = self.computerHand[i]
                           c.playCard(self.computerHand[i])
                           played.addCard(cardCurrent)
                           q = random.randint(0, len(self.computerCardsInHand))
                           c.playCard(self.computerHand[q])
                           played.addCard(self.computerHand[q])
                           self.played = True
                           break
                       # plus 4
                       if self.computerHand[i].value == 1:
                           cardCurrent = self.computerHand[i]
                           c.playCard(self.computerHand[i])
                           played.addCard(cardCurrent)
                           for i in range(0, 4):
                               card = d.deal()
                               p.takeACard(card)
                           c.playCard(self.computerHand[0])
                           played.addCard(self.computerHand[0])
                           self.played = True
                           break
                   # plus 2
                   elif self.computerHand[i].value == 12:
                       cardCurrent = self.computerHand[i]
                       c.playCard(self.computerHand[i])
                       played.addCard(cardCurrent)
                       for i in range(0, 2):
                           card = d.deal()
                           p.takeACard(card)
                       self.played = True
                       break
                   # change direction or skip a turn
                   elif self.computerHand[i].value == 10 or self.computerHand[i].value == 11:
                       cardCurrent = self.computerHand[i]
                       c.playCard(cardCurrent)
                       played.addCard(cardCurrent)
                       pygame.time.wait(2000)

                       for i in range(0, len(self.computerHand)):
                           if self.computerHand[i].suit == played.playedCard[-1].suit:
                               cardCurrent = self.computerHand[i]
                               c.playCard(self.computerHand[i])
                               played.addCard(cardCurrent)
                               self.played = True
                               break

                           elif self.computerHand[i].value == played.playedCard[-1].value:
                               cardCurrent = self.computerHand[i]
                               c.playCard(self.computerHand[i])
                               played.addCard(cardCurrent)
                               self.played = True
                               break
                       if self.played == False:
                           card = d.deal()
                           c.takeACard(card)
                           self.played = True
                       break
                    # normal card/ same color
                   else:
                        cardCurrent = self.computerHand[i]
                        c.playCard(self.computerHand[i])
                        played.addCard(cardCurrent)
                        self.played = True
                        break

               # pick a card
           if self.played == False:
               card = d.deal()
               c.takeACard(card)
               
        counter.setText(str(p.cardsInHand))
        counterc.setText(str(self.computerCardsInHand))
       
        if p.cardsInHand == 0:
            g.nextRoom()
            room3.addObject(w)
        elif c.computerCardsInHand == 0:
            pygame.quit()
            room3.addObappject(l)  
           
    def takeACard(self,card):
        
        self.computerHand.append(card)
        
        card.rect.x = (self.computerCardsInHand * (card.rect.width + 4)) + self.startX
        card.rect.y = 450
        
        self.computerCardsInHand += 1
        
        room2.addObject(card)
        
    def __str__(self):
        s = ""
        for card in self.computerHand:
            s = s + str(card) + " "
        s = "CPU:\n" + s + "\n"
        return s
    
class pilePlayed(GameObject):
    def __init__(self,xPos,yPos):
        GameObject.__init__(self)
        self.rect.x = xPos
        self.rect.y = yPos
        self.playedCard = []
        
    def removeCard(self,card):
        self.playedCard.remove(card)
        
    def addCard(self,card):
        self.playedCard.append(card)
        self.image = card.image
        
    def __str__(self):
        s = ""
        for card in self.playedCard:
            s = s + str(card) + " "
        s = "Played:\n" + s + "\n"
        return s
    
class addToDeckButton(TextRectangle):
    def __init__(self, text, xPos, yPos, font, textColor, buttonWidth, buttonHeight, buttonColor):
        TextRectangle.__init__(self,text, xPos, yPos, font, textColor, buttonWidth, buttonHeight, buttonColor)
    
    def update(self):
        self.checkMousePressedOnMe(event)
        if self.mouseHasPressedOnMe and event.type == pygame.MOUSEBUTTONUP:
            self.mClickAction()
            
    def mClickAction(self):
        for i in range(0, len(played.playedCard) - 1):
            d.addcard(played.playedCard[0])
            played.removeCard(played.playedCard[0])
            
        d.shuffle()
        room1.addObject(d)
        self.kill()
        self.mouseHasPressedOnMe = False
        
played = pilePlayed(350,300)
d = Deck(topCard, g.windowWidth/2 -55, g.windowHeight/2 - 100)
room2.addObject(d)

p = player(8,10)
for i in range(0,7):
    Card = d.deal()
    p.takeACard(Card)
room2.addObject(p)

c = cpu(8, 450)
for i in range (0,7):
    Card = d.deal()
    c.takeACard(Card)
room2.addObject(played)
room2.addObject(c)


room2.addObject(TextRectangle('Your Cards: ',10,150, gameFont, WHITE))
counter = TextRectangle(str(p.cardsInHand),125,152, gameFont, WHITE)
room2.addObject(counter)

room2.addObject(TextRectangle('CPU Cards: ',10,400, gameFont, WHITE))
counterc = TextRectangle(str(c.computerCardsInHand),125,402, gameFont, WHITE)
room2.addObject(counterc)




#Start Game
g.start()
while g.running :

	#How often the game loop executes each second
	dt = g.clock.tick(60)
	#Check Events
	for event in pygame.event.get():
		#Check for [x]
		if event.type == pygame.QUIT:
			g.stop()
	#Update All objects in Room
	g.currentRoom().updateObjects()
	#Render Background to the game surface
	g.currentRoom().renderBackground(g)
	#Render Objects to the game surface
	g.currentRoom().renderObjects(g)
	#Draw everything on the screen
	pygame.display.flip()


pygame.quit()
    
