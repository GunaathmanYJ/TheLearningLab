print("welcome to the blind auction")
bids = {}
continue_bidding = True
while continue_bidding:
    name = input("enter the name ")
    bid_amount = int(input("enter the bid amount "))
    bids[name] = bid_amount
    more_bids = input("is there any other bidding? type yes or no ").lower()
    if more_bids == "no":
        continue_bidding = False
    elif more_bids == "yes":
        print("\n" * 100)
def highest_bid_finder(bidding_dictionary):
    highest_bid = 0
    winner = ''
    for bidder in bidding_dictionary:
        if bidding_dictionary[bidder] > highest_bid:
            highest_bid = bidding_dictionary[bidder]
            winner = bidder
    print(f"the winner is {winner} with a bid of {highest_bid}")
highest_bid_finder(bids)
