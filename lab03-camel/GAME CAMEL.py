import random
def main():
    done=False
    miles=0
    thirst=0
    camel_tiredness=0
    nativos=-20
    canteen=3
    while done==False:
        nativosaleatorios=random.randint(7,14)
        millasaleatorios=random.randint(10,20)
        millasaleatorios2=random.randint(5,12)
        camelloaleatorio=random.randint(1,3)
        print("A. Drink from your canteen\n"
              "B. Ahead moderate speed.\n"
              "C. Ahead full speed.\n"
              "D  Stop and rest.\n"
              "E. Status check.\n"
              "Q. Quit.")
        letra=input("Your choice? ")
        if letra.upper()=="Q":
            print("Game end")
            break
        elif letra.upper()=="E":
            print("Miles travelled: " ,miles)
            print("Drinks on canteen: " ,canteen)
            print("The natives are " ,miles-nativos, "miles behind you.")
        elif  letra.upper()=="D":
            camel_tiredness=0
            print("The camel is happy")
            nativos+=nativosaleatorios
        elif letra.upper()=="C":
            miles+=millasaleatorios
            print("Miles : " ,miles)
            thirst+=1
            camel_tiredness+=camelloaleatorio
            nativos+=nativosaleatorios
        elif letra.upper()=="B":
            miles+=millasaleatorios2
            print("Miles : " ,miles)
            thirst+=1
            camel_tiredness+=1
            nativos+=nativosaleatorios
        elif letra.upper()=="A":
            if canteen>=1:
                canteen-=1
                thirst=0
            else:
                print("No water on canteen")
        if thirst>6:
            print("YOU DIE")
            break
        elif thirst>4:
            print("YOU ARE THIRST")
        if camel_tiredness>8:
            print("YOUR CAMEL DIES")
            break
        elif camel_tiredness>5:
            print("YOUR CAMEL IS GETTING TIRED")
        if nativos>=miles:
            print("Natives caugth you")
        elif miles-nativos<=15:
            print("NATIVES ARE CLOSE")
        if miles>=200:
            print("YOU WON ")
            break
        print()
        print()



main()
