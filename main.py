import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def blacjac():
  from replit import clear
  clear()
  from art import logo
  print(logo)
  usercards = []
  dealercards = []
  userscore = 0
  dealerscore = 0
  def calcscore(cardlist):
    return sum(cardlist)
  def dealcards(cardlist):
    index = random.randint(0,12)
    if cardlist==usercards:
      if index==0 and userscore+cards[0]>21:
        cards[0] = 1
      elif index==0 and userscore+cards[0]<=21:
        cards[0] = 11
    return cards[index]
  for x in range(0,2):
    usercard = dealcards(usercards)
    usercards.append(usercard)
  for x in range(0,2):
    dealercard = dealcards(usercards)
    dealercards.append(dealercard)
  userscore+=calcscore(usercards)
  dealerscore+=calcscore(dealercards)
  print(f"Your cards: {usercards}, current score: {userscore}. ")
  print(f"Computer's first card: {dealercards[0]}")
  wantmore = True
  while userscore<=21 and wantmore is True:
    moreinput = input("Type 'y' to get another card. ")
    if moreinput=="y":
      index = random.randint(0,12)
      usercards.append(cards[index])
      userscore+=cards[index]
      print(f"Your cards: {usercards}, current score: {userscore}. ")
      print(f"Computer's first card: {dealercards[0]}")
    else:
      wantmore = False
  def printfinal():
    print(f"Your final hand: {usercards}, final score: {userscore}")
    print(f"Dealer's final hand: {dealercards}, final score: {dealerscore}")
    if userscore>21:
      print("You went over. You lose!")
    elif dealerscore>21:
      print("Dealer went over. You win!")
    elif userscore<dealerscore:
      print("Dealer with higher score. You lose!")
    elif dealerscore<userscore:
      print("User with higher score. You win!")
    elif dealerscore==userscore:
      print("Draw!")

  if userscore>21:
    printfinal()
  else:
    while(dealerscore<17):
      index = random.randint(0,12)
      dealercards.append(cards[index])
      dealerscore+=cards[index]
    printfinal()

userchoice = True
while userchoice is True:
  want = input("Do you want to play a game of Blackjack? (y or n): ")
  if want=="y":
    blacjac()
  else:
    userchoice = False
