import unittest

from sueca_suits_ranks import *

from card import *

from sueca_tricks import *

class Tests_Ranks(unittest.TestCase):
    def test_rank_points_should_return_ten_for_any_seven(self):
      self.assertTrue(rank_points("7") == 10, "Value is wrong")

    def test_rank_points_should_return_eleven_for_any_ace(self):
      self.assertTrue(rank_points("A") == 11, "Value is wrong")

    def test_rank_points_should_return_four_for_any_king(self):
      self.assertTrue(rank_points("K") == 4, "Value is wrong")

    def test_rank_points_should_return_three_for_any_jack(self):
      self.assertTrue(rank_points("J") == 3, "Value is wrong")

    def test_rank_points_should_return_two_for_any_queen(self):
      self.assertTrue(rank_points("Q") == 2, "Value is wrong")

class Test_Suit_full_names(unittest.TestCase):
    def test_give_S_should_return_SPADES(self)  :
       self.assertTrue(suit_full_names("S") == "Spades", "S should be Spades")

    def test_give_D_should_return_Diamonds(self)  :
       self.assertTrue(suit_full_names("D") == "Diamonds", "D should be Diamonds")

    def test_give_C_should_return_Cubs(self)  :
       self.assertTrue(suit_full_names("C") == "Cubs", "C should be Cubs")

    def test_give_H_should_return_Hearts(self)  :
       self.assertTrue(suit_full_names("H") == "Hearts", "H should be Hearts")

class Test_Valid_Ranks(unittest.TestCase):
    def test_is_three_should_return_True(self)  :
       self.assertTrue(valid_rank("3") == True, "3 is a valid rank")

    def test_does_king_return_true(self):
       self.assertTrue(valid_rank("K") == True, "K is a valid rank")

    def test_does_queen_return_true(self):
       self.assertTrue(valid_rank("Q") == True, "Q is a valid rank")

    def test_does_Jack_return_true(self):
       self.assertTrue(valid_rank("J") == True, "J is a valid rank")

class Test_Valid_Suit(unittest.TestCase):
  def test_is_Heart_should_return_True(self):
    self.assertTrue(valid_suit("H") == True, "H is a valid suit")

  def test_is_Cubs_should_return_True(self):
    self.assertTrue(valid_suit("C") == True, "C is a valid suit")

  def test_is_Spades_should_return_True(self):
    self.assertTrue(valid_suit("S") == True, "S is a valid suit")

  def test_is_Diamonds_Should_return_True(self):
    self.assertTrue(valid_suit("D") == True, "D is a valid suit")

class Test_rank_higher_than(unittest.TestCase):
  def test_King_Is_Higher_Than_Jack(self):
    self.assertTrue(rank_higher_than("K", "J") == True, "King is higher than Jack")

  def test_Ace_Is_Higher_Than_Seven(self):
    self.assertTrue(rank_higher_than("A", "7") == True, "Ace is higher than Seven")

  def test_Jack_Is_Higher_Than_Queen(self):
    self.assertTrue(rank_higher_than("J", "Q") == True, "Jack is higher than Queen")

  def test_Seven_Is_Higher_Than_King(self):
    self.assertTrue(rank_higher_than("7", "K") == True, "Seven is higher than King")

  def test_Ace_Is_Higher_Than_Queen(self):
    self.assertTrue(rank_higher_than("A", "Q") == True, "Ace is higher than Queen")

  def test_king_of_spades_shouldbe_higher_than_jack_of_diamonds(self):
    myCard = Card("KS", "S")
    self.assertFalse(myCard.higher_than("JD", "D", "D") == False, "Ace is higher than King")

  def test_Queeen_of_Diamonds_shouldbe_lower_than_seven_of_diamonds(self):
    myCard = Card("QD", "D")
    self.assertFalse(myCard.higher_than("7D", "D", "C") == False, "Ace is higher than King")

  def test_Seven_of_clubs_shouldbe_higher_than_queen_of_spades(self):
    self.assertTrue(myCard.higher_than("QS", "S", "D") == True, "Ace is higher than King")



class Test_parseTrick_Test(unittest.TestCase):
    def test_parseTrick_AH_2S_7D_QD_should_be_True(self):
      self.assertTrue(parseTrick("AH 2S 7D QD") == True, "This is a valid trick")

    def test_parseTrick_1(self):
      self.assertTrue(parseTrick("2D AS QC 4H") == True, "This is a valid trick")

    def test_parseTrick_2(self):
      self.assertTrue(parseTrick("2C 6C AS KD") == True, "This is a valid trick")

    def test_parseTrick_3(self):
      self.assertTrue(parseTrick("3S JD KH AD") == True, "This is a valid trick")

    def test_parseTrick_4(self):
      self.assertTrue(parseTrick("AA JD KH AD") == False, "This is not a valid trick")

    def test_parseTrick_5(self):
      self.assertTrue(parseTrick("AB JD KH AD") == False, "This is not a valid trick")

    def test_parseTrick_6(self):
      self.assertTrue(parseTrick("AA J7 KH AD") == False, "This is not a valid trick")

    def test_parseTrick_7(self):
      self.assertTrue(parseTrick("AB CD EH AD") == False, "This is not a valid trick")

class Test_Trick(unittest.TestCase):

    def test_Points_given_AH_2S_7D_QD_should_return_23(self):
      trick = Trick("AH 2S 7D QD")
      points = trick.points()
      self.assertTrue(points == 23, "This trick should have a total of 23 points not " +  str(points))


  


  
  

    

    
      








if __name__ == '__main__':
  unittest.main(exit=False)
