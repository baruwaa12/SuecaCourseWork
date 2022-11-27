

from sueca_suits_ranks import valid_suit, valid_rank, rank_higher_than, rank_points


class CardInvalidError(Exception):
  pass
  
  # Function that takes a card then returns an object of class card
  def parseCard(cs):
    # cardEntered = str(input("Enter a card?"))
    if valid_rank(cs) & valid_suit(cs) == True:
      print("The card is valid")
    else:
      raise CardInvalidError("CardInvalid: Card " + cs + " is invalid!")

  def higher_than(self, other, suit, trump):
    return True

    
class Card:

  def __init__(self, cardName, cardSuit):
    self.cardName = cardName
    self.cardSuit = cardSuit      

  # Function to return the points of the currently known card  
  def points(self, card):
    points_dict = {"A": 11, "7": 10, "K": 4, "J": 3, "Q": 2}

    if card[0] == "A":
      return points_dict["A"]
    elif card[0] == "7":
      return points_dict["7"]
    elif card[0] == "K":
      return points_dict["K"]
    elif card[0] == "J":
      return points_dict["J"]
    elif card[0] == "Q":
      return points_dict["Q"]
    else:
      print("This card " + card + " is invalid")
      return False

  # Function which compares two suits of 2 different cards 
  def higher_than(self, other, suit, trump):
    if rank_higher_than(self.cardName, other.cardName) != True:
      return False
    else:
      return True