from replit import clear
#HINT: You can call clear() to clear the output in the console.

from art import logo
print(logo)

bids = []
bidding_finished = False

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  for bid in bidding_record:
    if bid["bidder_amt"] > highest_bid:
      highest_bid = bid["bidder_amt"]
      winner = bid["bidder_name"]
  print(f"The winner is {winner} with a bid of ${highest_bid}.")
  
while not bidding_finished:
  name = input("What is your name?: ")
  bidding_amt = int(input("What's your bid?: $"))
  bidder = {"bidder_name": name,
  "bidder_amt": bidding_amt}
  bids.append(bidder)
  
  more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  clear()
  if more_bidders == "no":
    bidding_finished = True
    find_highest_bidder(bids)