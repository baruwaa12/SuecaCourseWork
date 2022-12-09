

from sueca_suits_ranks import valid_suit, valid_rank, rank_higher_than, rank_points

class CardInvalidError(Exception):
  pass
  
  # Function that takes a card then returns an object of class card
def parseCard(cs):
    # cardEntered = str(input("Enter a card?"))
    if valid_rank(cs[0]) & valid_suit(cs[1]) == True:
      return True
    else:
      raise CardInvalidError("CardInvalid: Card " + cs + " is invalid!")


class Card:

  def __init__(self):
    self.cardName = cardName
    self.cardSuit = cardSuit      

  @property
  def card_Name(self):
    return self.cardName

  @property
  def card_Suit(self):
    return self.cardSuit

    
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
  
  def higher_than(self, other, s, t):
    comparing_card = self.cardName
    compared_card = other
    lead_suit = s
    trump_suit = t

    if comparing_card[1] == lead_suit and compared_card[1] != trump_suit:
      return True
    else:
      return False

  def show(self):
    newCard = self.cardName
    return newCard

