from card import *


def parseTrick(cs):
  if len(cs) == 11:
    splitcard = cs.split()

    # Check if any is invalid
    for x in range(0, len(splitcard)-1):
      if valid_rank(splitcard[x][0]) == False or valid_suit(splitcard[x][1]) == False:
        return False
    return True    
        
  else:
    # Return an exception
    raise ValueError("This is not a valid trick")


def parseGameFile(fname):
  f = open(fname, "r")
  for x in f:
    parseTrick(x)


class Trick:
  def __init__(self, trickStr):
    self.trickStr = trickStr

  @property
  def trick_String(self):
    return self.trickStr

  # Given a trick return the total number of points
  # "AH 2S 7D QD" = 23
  # Split to array of cards
  # initial totalPoints to 0
  # Foreach each card
    # take the first character, 
    # determine the points for that rank,
    # add the value to the totalPoints.
  def points(self):
    points_dict = {"A": 11, "7": 10, "K": 4, "J": 3, "Q": 2}

    cards = self.trickStr.split()
    totalPoints = 0
    
    for card in cards:
      key = card[0]
      # return 0 if the key is not in the dictionary
      totalPoints += points_dict.get(key, 0)
      
    return totalPoints


  # Given the trump suit determine who the winner is of a trick
  # Split the trick into array of cards.
  # Compare the suits of the cards to the trump suit
  # Whichever card has the same suit as the trump suit is the winner of the trick
  
  def trick_winner(self, t):
    cards = self.trickStr.split()

    for card in cards:
        winningPlayer = cards.index(card)
        if card[1] == t:
          return winningPlayer 
          
    


    


  


  
    
