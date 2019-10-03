'''Rock Paper and Scissors
User has to input r for rock p for paper and s for scissors
'''
import random
print("Ready for Rock Paper and Scissors!!!")
print("To quit press 100 and to check scores press 200 and to reset the score-table press 300")
print("r for rocks p for papers and s for scissors")

uscore=0
cscore=0
while True:
    x=random.randint(0,2)
    y=input("Rock Paper Scissor....: ")
    if(y=='100'):
        print("final scores are:computer "+str(cscore)+":"+str(uscore)+" user")
        if(cscore>uscore):
            print("Computer Wins :(")
        elif(cscore==uscore):
            print("Its a tie. -_-")
        else:
            print("You win!!! :)")
        break
    elif(y=='200'):
        print("scores are:computer "+str(cscore)+":"+str(uscore)+" user")
        continue
    elif(y=='300'):
        print("Scores have been reset")
        uscore=cscore=0
        continue
    elif((x==0 and y=='r')or (x==1and y=='p')or(x==2 and y=='s')):
        print("Thats a tie")
        continue
    elif((x==0 and y=='p')or (x==1 and y=='s')or (x==2 and y=='r')):
        print("You won the round")
        uscore+=1
        continue
    else:
        print("The computer won the round.")
        cscore+=1
