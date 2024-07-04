import random

def wincon(player_hand, dealer_hand):
  print(f"Player Hand: {player_hand}")
  print(f"Dealer Hand: {dealer_hand}")
  player_sum = sum(player_hand)
  dealer_sum = sum(dealer_hand)
  if player_sum > dealer_sum:
    return "Player Wins!!"
  elif player_sum < dealer_sum:
    return "Dealer Wins!!"
  else:
    return "It's a draw!"

def game():
  player_hand = []
  dealer_hand = []

  for _ in range(2):
    player_hand.append(random.randint(1, 13))
    dealer_hand.append(random.randint(1, 13))

  print(f"Player Hand: {player_hand}")
  print(f"Dealer Hand: {dealer_hand}")

  busted = False
  player_hold = False

  while not busted and player_hold is not True:
    action = input("Hit (h) or Hold (s): ").lower()
    if action == "h":
      player_hand.append(random.randint(1, 13))
      print(f"Player Hand: {player_hand}")
      if sum(player_hand) > 21:
        busted = True
        print("Player Busted!")
    elif action == "s":
      player_hold = True
    else:
      print("Invalid Input. Please enter 'h' or 's'.")

  dealer_hold = False
  while sum(dealer_hand) < 17 and not busted:
    dealer_hand.append(random.randint(1, 13))
    if sum(dealer_hand) > 21:
      busted = True
      print(f"Dealer Hand: {dealer_hand}")
      print("Dealer Busted!")
    else:
      print(f"Dealer Hand: {dealer_hand}")

  if not busted:
    winner = wincon(player_hand, dealer_hand)
    print(winner)

game()