# Suits and Ranks

# This function checks whether if the string entered has a valid suit

rank = ['A', '2', '3', '4', '5', '6', '7', 'Q', 'J', 'K']

suit = ['H', 'C', 'S', 'D']


def valid_suit(value):
  # AH
  for i in range(0, len(suit)):
    if value[1] != suit[i]:
      print(value[1] + " not equal " + suit[i])  #logging
    else:
      return True
  return False


def valid_rank(value):
  # r = str(input("Enter a card with a valid rank. " ))
  for x in range(0, len(rank)):
    if value[0] != rank[x]:
      print(value[0] + " not equal " + rank[x])
    else:
      return True
  return False


def suit_full_names():
  suitDict = {"S": "Spades", "D": "Diamonds", "H": "Hearts", "C": "Cubs"}

  # suitName = suitDict["H"]
  # suitName = str(input("Enter a card. "))
  # suit = suitDict[1]
  print(suitDict["S"])
  # if suit == suitDict["S"]:
  #   print(suit)

  # print(suitName)
  


# You need to complete the else condition otherwise you will get red squiges on the next line. Ok?
# question = str(input("Enter a card"))

# print(valid_suit(question))

suit_full_names()
