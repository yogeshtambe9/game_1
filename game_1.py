import random

comp=random.choice([0,-1,1])
yous= input("enter s,w or g: ").lower()
dic={"s":-1 ,"w":0,"g":1}
you=dic[yous]

rdic={-1:"Snake",0:"Water",1:"Gun"}

print(f"You choosed {rdic[you]}\nComputer choosed {rdic[comp]}")

if comp==you:
    print("Draw")
else :
  if comp==0 and you==-1:
    print("you win")
  elif comp==0 and you==1:
    print("you loose")
  elif comp==1 and you==-1:
    print("you loose")
  elif comp==1 and you==0:
    print("you win")
  elif comp==-1 and you==1:
    print("you win")
  elif comp==-1 and you==0:
    print("you loose")