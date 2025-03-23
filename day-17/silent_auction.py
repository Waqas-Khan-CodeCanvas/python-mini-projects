import os

print("*********  -:(  WELCOME TO THE SILENT AUCTION PROGRAM  ):-   **********")
def find_winner(bidder_details):
    highest_bid=0
    winner=""
    for bidder in bidder_details:
        bidding_price=bidder_details[bidder]
        if bidding_price > highest_bid:
            highest_bid=bidding_price
            winner = bidder
    print(f"here is the list of all bidders {bidder_details}")
    print(f"the winner is {winner} with the bid price is {highest_bid} ")


end_bidder=True
bidder_data={}
while end_bidder:
    name=input("What is your name?:")
    price=int(input("What is your bid?:"))
    bidder_data[name]=price
    more_biddres=input("Are there are more bidders? type ('yes 'or no'").lower()
    if more_biddres == 'no':
        end_bidder=False
        find_winner(bidder_data)
    elif more_biddres == 'yes':
        os.system('cls')