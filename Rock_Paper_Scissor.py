import random
lisname = ["Rock","Paper","Scissor"]
print(f"Enter Rock, Paper, Scissors")
inp = input("You Chose : ")
k = random.choice(lisname)
print("Opponent Chose :",k)
if(k==inp):
    print("TIED")
elif(k == 0 and inp != 2):
    print("You Lose")
elif(k == 1 and inp != 0):
    print("You Lose")
elif(k == 2 and inp != 1):
    print("You Lose")
else:
    print("You Win")