import unittest

from sueca_suits_ranks import rank_points, suit_full_names

class Tests_Ranks(unittest.TestCase):
    def test_rank_points_should_return_ten_for_any_seven(self):
      # print(rank_points("7"))
      self.assertTrue(rank_points("7") == 10, "Value is wrong")

      ## These are sample tests for templates.
    # def test_strings_c(self):
    #     self.assertTrue(1 == 1, "Not true")
      
    # def test_strings_b(self):
    #     self.assertEqual( 'a'*4, 'aaaa')
      
    # # Returns True if the string contains 4 a.
    # def test_strings_a(self):
    #     self.assertEqual( 'a'*4, 'aaaa')
  

class Test_Suit_full_names(unittest.TestCase):
    def test_give_S_should_return_SPADES(self)  :
       self.assertTrue(suit_full_names("S") == "Spades", "S should be Spades") 
      
if __name__ == '__main__':
  unittest.main(exit=False)
  