from art import logo

print(logo)

continue_bidding = True
bids = {}

def find_highest_bidder(bids_dict):
    highest_bid = 0
    winner = ""

    for bidder in bids_dict:
        amount = bids_dict[bidder]
        if amount > highest_bid:
            highest_bid = amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}")

while continue_bidding:
    bidder = input("Who is bidding? ")
    bid_amount = int(input("How much is the bid? "))

    bids[bidder] = bid_amount

    more_bids = input("Are there more bidders? Type yes or no. ")
    if more_bids == "no":
        continue_bidding = False
        find_highest_bidder(bids)
