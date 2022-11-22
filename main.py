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


# Function to return the name of the suit when given the initials..
def suit_full_names():
  suitDict = {"S": "Spades", "D": "Diamonds", "H": "Hearts", "C": "Cubs"}

  suitName = str(input("Enter a card. "))

  if suitName[1] == "S":
    print(suitDict["S"])
  elif suitName[1] == "D":
    print(suitDict["D"])
  elif suitName[1] == "H":
    print(suitDict["H"])
  elif suitName[1] == "C":
    print(suitDict["C"])
  else:
    raise ValueError("invalid suit symbol " + suitName[1])


def rank_points():
  points_dict = {"A": 11, "7": 10, "K": 4, "J": 3, "Q": 2}

  suitName = str(input("Enter a card. "))

  if suitName[0] == "A":
    print(points_dict["A"])
  elif suitName[0] == "7":
    print(points_dict["7"])
  elif suitName[0] == "K":
    print(points_dict["K"])
  elif suitName[0] == "J":
    print(points_dict["J"])
  elif suitName[0] == "Q":
    print(points_dict["Q"])
  else:
    raise ValueError("invalid suit symbol " + suitName[1])


def rank_higher_than():
  points_dict = {"A": 11, "7": 10, "K": 4, "J": 3, "Q": 2}

  card1 = str(input("Enter a card. "))
  card2 = str(input("Enter a card. "))

  r1 = card1[0]
  r2 = card2[0]

  if points_dict[r1] > points_dict[r2]:
    print("This card: " + r1 + " is greater than " + r2)
  elif points_dict[r2] > points_dict[r1]:
    print("This card: " + r2 + " is greater than " + r1)
  elif points_dict[r2] == points_dict[r1]:
    print("Both cards are of equal value")
  else:
    return False

  # if r1 == points_dict[r1] and r2 == points_dict[r2]:



# question = str(input("Enter a card"))

# print(valid_suit(question))

print(rank_higher_than())
