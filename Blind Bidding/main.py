import os
import art
def bidder (id=0):
    choice="yes" 
    bidder_list={}
    while choice=="yes":
        print(art.logo)
        print("---------Welcome to the Blind Auction---------")
        name=input("\nEnter your name :")
        bid=input("Enter the bid amount :")
        bidder_list[id]=[name,bid]
        id+=1
        choice=input("""\n Are there more bidders, yes or no :""").lower()
        os.system("cls")

    max=-1
    record_id=-1
    for key in bidder_list:
        if max < int(bidder_list[key][1]):
            max = int(bidder_list[key][1])
            record_id=key
    print(f"""\nBid won by {bidder_list[record_id][0]} 
with {bidder_list[record_id][1]}$ bid.""")
        
bidder()