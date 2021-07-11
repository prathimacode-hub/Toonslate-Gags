import random
import time
import sys
#CRICKET Teams
x=input("Team A enter your name ")
y=input("Team B enter your name ")
wicket=0
score=0
#overs
o=int(input("Enter the number of overs you want to play"))
Ov=o*6
#Toss
TOSS=random.randint(1,3)
T1=input("TOSS\n Enter your choice press (1) for HEADS/(2) for TAILS")

 
if TOSS==T1:
  print("Team",x,"choose bat(1) or ball(2)")
  t1=int(input("Enter choice:"))
  if t1==1:
         print("you choose to bat")
  elif t1==2:
         print("you choose to bowl")  
  else:
         print("INVALID CHOICE") 
         
elif TOSS==2:
  print("Team",y,"choose bat(1) or ball(2)")
  t2=int(input("Enter choice:"))
  if t2==1:
         print("you choose to bat")
  elif t2==2:
         print("you choose to bowl")
  else:
          print("INVALID CHOICE") 
          

  

    
for i in range(Ov):
  x=random.randint(-1,8)
  if x==7:
    
    wicket=wicket+1
    print("Wicket",wicket)
    if wicket==10:
       print("All Out")
       break 
 
  elif x==-1:
    print("\n WIDE BALL ")
    score=score+1

  else:
    print("run scored",x)
    score=score+x
    
print(score,"/",wicket) 
