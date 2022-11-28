# Suits and Ranks

# This function checks whether if the string entered has a valid suit

rank = ['A', '2', '3', '4', '5', '6', '7', 'Q', 'J', 'K']

suit = ['H', 'C', 'S', 'D']

# This function checks whether if the string entered has a valid suit

def valid_suit(s):
  # AH
  for i in range(0, len(suit)):
    if s == suit[i]:
      return True
  return False

# Function to check if the rank is valid 
  
def valid_rank(r):
  for x in range(0, len(rank)):
    if r == rank[x]:
      return True
  return False



# Function to return the name of the suit when given the initials..

def suit_full_names(r):
  suitDict = {"S": "Spades", "D": "Diamonds", "H": "Hearts", "C": "Cubs"}

  
  if r == "S":
    return suitDict["S"]
  elif r == "D":
    return suitDict["D"]
  elif r == "H":
    return suitDict["H"]
  elif r == "C":
    return suitDict["C"]
  else:
    raise ValueError("invalid suit symbol " + r)
  return ""


# Function which returns the points of card when it is entered,


def rank_points(suitName):
  points_dict = {"A": 11, "7": 10, "K": 4, "J": 3, "Q": 2}

  if suitName[0] == "A":
    return points_dict["A"]
  elif suitName[0] == "7":
    return points_dict["7"]
  elif suitName[0] == "K":
    return points_dict["K"]
  elif suitName[0] == "J":
    return points_dict["J"]
  elif suitName[0] == "Q":
    return points_dict["Q"]
  else:
    raise ValueError("invalid suit symbol " + suitName[1])




def rank_higher_than(r1, r2):
  points_dict = {"A": 11, "7": 10, "K": 4, "J": 3, "Q": 2}
  
  if points_dict[r1] > points_dict[r2]:
    print("This card: " + r1 + " is greater than " + r2)
    return True
  elif points_dict[r2] > points_dict[r1]:
    print("This card: " + r2 + " is greater than " + r1)
    return True
  elif points_dict[r2] == points_dict[r1]:
    print("Both cards are of equal value")
    return True
  else:
    return False
