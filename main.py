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

    def test_rank_points_should_return_0_for_any_two(self):
      self.assertTrue(rank_points("2") == 0, "Value is wrong")




class Test_Suit_full_names(unittest.TestCase):
    def test_give_S_should_return_SPADES(self)  :
       self.assertTrue(suit_full_name("S") == "Spades", "S should be Spades")

    def test_give_D_should_return_Diamonds(self)  :
       self.assertTrue(suit_full_name("D") == "Diamonds", "D should be Diamonds")

    def test_give_C_should_return_Cubs(self)  :
       self.assertTrue(suit_full_name("C") == "Clubs", "C should be Clubs")

    def test_give_H_should_return_Hearts(self)  :
       self.assertTrue(suit_full_name("H") == "Hearts", "H should be Hearts")

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

  def test_is_P_Should_return_False(self):
    self.assertTrue(valid_suit("P") == False, "P is not a valid suit")

  def test_is_Hearts_Should_return_True(self):
    self.assertTrue(valid_suit("Hearts") == False, "Hearts is an invalid suit")

class Test_card_parsing(unittest.TestCase):

  def test_is_4c_Should_return_True(self):
    self.assertTrue(parseCard("4C") == True, "Four of clubs is a valid card")

  def test_is_AD_Should_return_True(self):
    self.assertTrue(parseCard("AD") == True, "Ace of Diamonds is a valid card")
  
  

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
    
  def test_2_should_be_equal_To_3(self):
    self.assertTrue(rank_higher_than("2", "3") == False, "2 is equal to 3")

  def test_3_should_be_equal_To_A(self):
    self.assertTrue(rank_higher_than("3", "A") == False, "3 is lower than ace")

  def test_6_and_5_should_return_True(self):
   self.assertTrue(rank_higher_than("6", "5") == True, "6 has an equal rank to 5 both have zero points")

  def test_B_and_B_should_return_False(self):
    with self.assertRaises(ValueError) as context:
            rank_higher_than("B", "B")


  def test_king_of_spades_shouldbe_higher_than_jack_of_diamonds(self):
    myCard = Card("KS", "S")
    self.assertTrue(myCard.higher_than("JD", "D", "D") == False, "King of spades should be low")

  def test_Queen_of_Diamonds_shouldbe_lower_than_seven_of_diamonds(self):
    myCard = Card("QD", "D")
    self.assertTrue(myCard.higher_than("7D", "D", "C") == False, "Queen of diamonds has a lower rank than seven of diamonds")

  def test_Seven_of_clubs_shouldbe_higher_than_queen_of_spades(self):
    myCard = Card("7D"), "D"
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

    def test_Points_given_QH_2D_AC_4D_should_return_13(self):
      trick = Trick("QH 2D AC 4D")
      points = trick.points()
      self.assertTrue(points == 13, "This trick should have a total of 13 points not " +  str(points))


    def test_Points_given_KH_5S_4C_4D_should_return_4(self):
      trick = Trick("KH 5S 4C 4D")
      points = trick.points()
      self.assertTrue(points == 4, "This trick should have a total of 4 points not " +  str(points))


    def test_Points_given_AS_AC_AD_AH_should_return_44(self):
      trick = Trick("AS AC AD AH")
      points = trick.points()
      self.assertTrue(points == 44, "This trick should have a total of 44 points not " +  str(points))


    def test_Points_given_AS_2D_AD_AH_should_return_33(self):
      trick = Trick("AS 2D AD AH")
      points = trick.points()
      self.assertTrue(points == 33, "This trick should have a total of 44 points not " +  str(points))

    


class Test_TrickWinner(unittest.TestCase):
  def test_Check_winner_of_trick_is_the_2nd_player(self):
      trick = Trick("AS 2D 3S AH")
      self.assertTrue(trick.trick_winner("D") == 1, "The winner of this trick is the 3rd player")

  

  


    

    
      








if __name__ == '__main__':
  unittest.main(exit=False)
