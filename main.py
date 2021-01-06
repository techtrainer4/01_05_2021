import numpy as np
pot = 100
while pot > 5:
  hand = np.random.randint(1,10,5)
  hand = list(hand)
  for h in hand:
    if hand.count(h) == 2:
      print("You win")
      pot = pot + 5
      print("You have {} left".format(pot))
      break
    else:
      print("You lost")
      pot = pot - 5 
      print("You have {} left.".format(pot)) 




