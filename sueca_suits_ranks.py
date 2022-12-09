# Suits and Ranks

# This function checks whether if the string entered has a valid suit



# This function checks whether if the string entered has a valid suit

def valid_suit(s):
  # AH
  suit = ['H', 'C', 'S', 'D']
  
  for i in range(0, len(suit)):
    if s == suit[i]:
      return True
  return False

# Function to check if the rank is valid 
  
def valid_rank(r):

  rank = ['A', '2', '3', '4', '5', '6', '7', 'Q', 'J', 'K']
  
  for x in range(0, len(rank)):
    if r == rank[x]:
      return True
  return False


# Function to return the name of the suit when given the initials..

def suit_full_name(r):
  suitDict = {"S": "Spades", "D": "Diamonds", "H": "Hearts", "C": "Clubs"}

  
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
  points_dict = {"A": 11, "7": 10, "K": 4, "J": 3, "Q": 2, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0}

  if suitName == "A":
    return points_dict["A"]
  elif suitName == "7":
    return points_dict["7"]
  elif suitName == "K":
    return points_dict["K"]
  elif suitName == "J":
    return points_dict["J"]
  elif suitName == "Q":
    return points_dict["Q"]
  elif suitName == "2":
    return points_dict["2"]
  elif suitName == "3":
    return points_dict["3"]
  elif suitName == "4":
    return points_dict["4"]
  elif suitName == "5":
    return points_dict["5"]
  elif suitName == "6":
    return points_dict["6"]
  else:
    raise ValueError("invalid rank symbol " + suitName)




def rank_higher_than(r1, r2):
  points_dict = {"A": 11, "7": 10, "K": 4, "J": 3, "Q": 2, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0}

  valueR1 = points_dict.get(r1, -1)

  if valueR1 == -1:
      raise ValueError("invalid rank symbol " + r1)
    
  valueR2 = points_dict.get(r2, -1)

  if valueR2 == -1:
      raise ValueError("invalid rank symbol " + r2)
    
  
  if valueR1 > valueR2:  
    return True
  else:
    return False
    

  
