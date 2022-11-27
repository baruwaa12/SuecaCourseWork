

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
       
class Card:

  def __init__(self, cardName, cardSuit):
    self.cardName = cardName
    self.cardSuit = cardSuit      

  # Function to return the points of the currently known card  
  def points(self, card):
    points_dict = {"A": 11, "7": 10, "K": 4, "J": 3, "Q": 2}

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

  # Function which compares two suits of 2 different cards 

  
  def isThisTrue(self, TrueOrFalse):
    if(TrueOrFalse == True):
      print("True")

    return False
    
  
  def higher_than(self, other, suit, trump):
      return rank_higher_than(self.cardName, other.cardName)
  
# Instantiate a new instance of the Card
def ace_of_spade_shouldbe_higher_than_king_of_spades(self):
  myCard = Card("AS","S")
  self.assertTrue(myCard.higher_than("KS", "S", "D"))
  
def ace_of_spade_shouldNOtBe_higher_than_king_of_spades(self):
  myCard = Card("AS","S")
  self.assertFalse(myCard.higher_than("KS", "S", "D"))

def seven_of_diamonds_Shouldbe_higher_than_Jack_of_diamonds(self):
  myCard = Card("7D", "D")
  self.assertTrue(myCard.higher_than("JD", "D", "S"))

def Jack_of_Spades_Shouldbe_higher_than_Queen_of_diamonds(self):
  myCard = Card("JS", "S")
  self.assertTrue(myCard.higher_than("QD", "D", "C"))

def Queen_of_Clubs_ShouldNotBe_higher_than_Jack_of_diamonds(self):
  myCard = Card("QC", "C")
  self.assertFalse(myCard.higher_than("JD", "D", "S"))


higher_than()