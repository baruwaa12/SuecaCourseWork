from card import *


def parseTrick(cs):
  if len(cs) == 11:
    splitcard = cs.split()

    # Check if any is invalid
    for x in range(0, len(splitcard)-1):
      if valid_rank(splitcard[x][0]) == False or valid_suit(splitcard[x][1]) == False:
        return False
    return True    
        
  else:
    # Return an exception
    raise ValueError("This is not a valid trick")

  
    
    

    