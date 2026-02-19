import os
print("Welcome to secret Auction program.")
bids = {}
def highestBidder(bids):
    maxValue = max(bids.values())
    print(maxValue)

def findHighestBidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount> highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")
    
while True:
    name = input("What is your name? ")
    bid  = int(input("What's your bid? $"))
    bids [name]= bid
    anyOther = input("Are there any other bidders? (y/n)").lower()
    if anyOther!="y":
        break
    else:
        os.system("cls")
# for items in bids:
#     print(bids[items])

highestBidder(bids=bids)