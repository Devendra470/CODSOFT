import random
def gamewin(player,comp):
    if(player=='r'):
        if(comp=='p'):
            return False
        elif (comp=='s'):
            return True
    if (player=='p'):
        if(comp=='r'):
            return True
        elif (comp=='s'):
            return False
    if(player=='s'):
        if(comp=='r'):
            return False
        elif(comp=='p'):
            return True
    if(player==comp):
        return None
randomno=random.randint(1,3)
if(randomno==1):
    comp='r'
if(randomno==2):
    comp='p'
if(randomno==3):
    comp='s'
choice='y'
while(choice=='y'):
    player=str(input("Your Move: Rock(r),Paper(p) or Scissor(s): ")).lower()
    win=gamewin(player,comp)
    if(win==True):
        print("You Won!")
    elif(win==None):
        print("Its a Tie!")
    elif(win==False):
        print("You Loose!")
    print(f"Computer Choose: {comp}")
    print(f"You Choose: {player}")
    choice=str(input("Do you want to play again?(Y/N): ")).lower()