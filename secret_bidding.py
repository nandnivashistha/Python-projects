from replit import clear
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
#HINT: You can call clear() to clear the output in the console
bidders={}
def add_silent_bidders(name, amount):
  bidders[name]=amount
  
next_bid=True
while next_bid:
  b_name=input("What is your name?: \n")
  b_bid=int(input("What is your bid?: \n$"))
  add_silent_bidders(b_name, b_bid)
  keep_going=input("Are there any other bidders? Type 'yes or 'no'. \n").lower()
  if keep_going=="no":
    next_bid=False
  
  clear()   
for i in bidders:
  maximum_bid=max(bidders.values())
winner= list(bidders.keys())[list(bidders.values()).index(maximum_bid)]
print(f"The winner is {winner} with a bid of ${maximum_bid}")
  
  