
from sueca_suits_ranks import valid_suit, valid_rank, rank_higher_than


class CardInvalidError(Exception):
  pass


# Function that takes a card then returns an object of class card
def parseCard(cs):
  # cardEntered = str(input("Enter a card?"))
  if valid_rank(cs) & valid_suit(cs) == True:
    print("The card is valid")
  else:
    raise CardInvalidError("CardInvalid: Card " + cs + " is invalid!")
  

class Card:
  
  def __init__(self, card):
    self.card = card

  # Function to return the points of the currently known card
  def points(self):
    points_dict = {"A": 11, "7": 10, "K": 4, "J": 3, "Q": 2}

    card = str(input("Enter a card. "))

    if card[0] == "A":
      print(points_dict["A"])
    elif card[0] == "7":
      print(points_dict["7"])
    elif card[0] == "K":
      print(points_dict["K"])
    elif card[0] == "J":
      print(points_dict["J"])
    elif card[0] == "Q":
      print(points_dict["Q"])
    else:
      print("This card " + card + " is invalid")

  # Function which compares 2 cards 
  def higher_than(self, other, suit, trump):
  #     suit = str(input("Enter a card with a valid suit: "))
  #     trump = str(input("Enter the trump card: "))
      print(rank_higher_than(""))
      return True

  # Function that returns the string representation of a given card
  def show(self):
     strCard = str(input("Please a enter card"))
     print(strCard)


  higher_than("AS", "KS", "S", "7D")

    
    
    
    
    