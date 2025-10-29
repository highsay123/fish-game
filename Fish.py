import time
import random
class Fish:
    def __init__(self,name,rarity,price,depth,chance):
        self.name=name
        self.chance=chance
        self.rarity=rarity
        self.price=price
        self.depth=depth
        self.craftable=False
        self.bait_yield=0
    
    def craft(self): #we're gonna have to make a 2nd one of these in the player class which checks inventory for the fish
        if self.craftable==True:
            print("Creating bait", end="" ,flush=True)
            time.sleep(0.5)
            print(".", end="" ,flush=True)
            time.sleep(0.5)
            print(".", end="" ,flush=True)
            time.sleep(0.5)
            print(".")
            time.sleep(0.5)
            print(f"+{self.bait_yield} {self.name} bait")
            return self.bait_yield
        else:
            print("You cant use this fish as bait!")
            return None

class Sardine(Fish):
    def __init__(self):
        super().__init__("Sardine", "Common", 5, "Shallow",35)
        self.craftable=True
        self.bait_yield=3

class Trout(Fish):
    def __init__(self):
        super().__init__("Trout", "Common", 10, "Shallow",30)

class Crab(Fish):
    def __init__(self):
        super().__init__("Crab", "Uncommon", 15, "Shallow",20)
        self.craftable=True
        self.bait_yield=1

class Sea_bass(Fish):
    def __init__(self):
        super().__init__("Sea bass","Rare", 30, "Shallow", 10)

class Mackerel(Fish):
    def __init__(self):
        super().__init__("Mackerel", "Common", 15, "Mid depth",35)
        self.craftable=True
        self.bait_yield=5

class Squid(Fish):
    def __init__(self):
        super().__init__("Squid", "Uncommon", 30, "Mid depth",30)
        self.craftable=True
        self.bait_yield=1

class Angler_fish(Fish):
    def __init__(self):
        super().__init__("Angler fish", "Rare", 60, "Mid depth",10)

class Jellyfish(Fish):
    def __init__(self):
        super().__init__("Jellyfish", "Ultra rare", 100, "Mid depth",5)

class Blobfish(Fish):
    def __init__(self):
        super().__init__("Blobfish", "Uncommon", 60, "The Depth",22)
        self.craftable=True
        self.bait_yield=3

class Goblin_shark(Fish):
    def __init__(self):
        super().__init__("Goblin shark", "Rare", 60, "The Depth",10)
        self.craftable=True
        self.bait_yield=6

class Kraken(Fish):
    def __init__(self):
        super().__init__("Kraken", "Legendary", 60, "The Depth",2)

class Siren(Fish):
    def __init__(self):
        super().__init__("Siren", "Legendary", 60, "The Depth",1)

fish_dict={"Shallow":{"Sardine":Sardine,"Trout":Trout,"Crab":Crab,"Sea bass":Sea_bass},"Mid depth":{"Mackerel":Mackerel,"Squid":Squid,"Angler_fish":Angler_fish,"Jellyfish":Jellyfish},"The Depth":{"Blobfish":Blobfish,"Goblin shark":Goblin_shark,"Kraken":Kraken,"Siren":Siren}}

class bait:
    def __init__(self,name,multiplier,cost):
        self.name=name
        self.multiplier=multiplier
        self.cost=cost

class worm(bait):
    def __init__(self):
        super().__init__("Worm", 1,0,)

class sardine_bait(bait):
    def __init__(self):
        super().__init__("Sardine bait", 1,4)

class crab_bait(bait):
    def __init__(self):
        super().__init__("Crab bait", 1,20)

class squid_bait(bait):
    def __init__(self):
        super().__init__("Squid bait", 1,45)

class mackerel_bait(bait):
    def __init__(self):
        super().__init__("Mackerel bait", 1,7)

class goblin_shark_bait(bait):
    def __init__(self):
        super().__init__("Goblin shark bait", 1,20)

class blobfish_bait(bait):
    def __init__(self):
        super().__init__("Blobfish bait", 1)

bait_dict={"Sardine":sardine_bait,"Crab":crab_bait, "Mackerel":mackerel_bait, "Squid":squid_bait,"Goblin shark":goblin_shark_bait,"Bobfish":blobfish_bait}

class fishing_rod:
    def __init__(self,level):
        self.level=level
        self.multiplier=1
        if level ==1:
            self.name="Stick with a hook"
        elif level==2:
            self.name="Plastic rod"
            self.cost=80
        elif level==3:
            self.name="Titanium rod"
            self.cost=150
        else:
            self.name="Mystic rod"
            self.cost=300
            self.multiplier=2


def select_item(items):
    if type(items)==dict:
        item_list=list(items.keys())
    elif type(items)==list:
        item_list=items
    for item in item_list:
        print(f"{item_list.index(item)+1}.{item}")


    choice= input("")
    while True:
        if type(choice)!=int:
            while choice.isnumeric()==False:
                choice=input("Enter a valid number")
            choice=int(choice)
        if 0<choice<=len(item_list):
            if type(items)==list:
                return items[choice-1]
            if items[item_list[choice-1]]=="Back":
                return "Back"
            try:
                return items[item_list[choice-1]]() #may cause an error i need to test this
            except:
                try:
                    return items[item_list[choice-1]]["class"]()
                except:
                    return items[item_list[choice-1]]["object"]
        else:
            choice= " "

class Fisher:
    def __init__(self,name):
        self.name=name
        self.rod=fishing_rod(1)
        self.money=10000
        self.bait={"Worm":{"class":worm,"count":"Infinite"},"Sardine bait":{"class":sardine_bait,"count":10}}#i need to test whether tihs infinite breaks any code i dont think it does tho
        self.fish={"Sardine":{"class":Sardine,"count":4}}#this is basically the fish inventory. shows u how much of each fish u have
        self.inventory={"Fishing rod":self.rod, "Fish": self.fish, "Bait":self.bait, "Money":self.money}
        self.shop_inv={"Plastic rod":{"object":fishing_rod(2)}}
    def craft(self):
        if self.fish=={}:
            print("You dont have any fish to craft bait with!")
        else:
            fish=select_item(self.fish)#fish is equal to the object of whatever fish was picked
            if self.fish[fish.name]["count"]>0:
                bait_yield=fish.craft()
                if bait_yield!=None:
                    self.fish[fish.name]["count"]-=1
                    ###
                    bait_count={}
                    bait_count["class"]=bait_dict[fish.name]
                    if (fish.name+" bait") not in self.shop_inv:
                        self.shop_inv[fish.name+" bait"]=bait_count
                    try:
                        bait_count["count"]=self.bait[fish.name]["count"]
                        bait_count["count"]+=bait_yield
                    except:
                        bait_count["count"]=bait_yield
                    self.bait[fish.name+" bait"]=bait_count #from the triple hash onwards is code to try update self.bait
            else:
                print("You dont have this fish to craft bait with")
    def fishing(self):
        if self.rod.level==1:
            depth="Shallow"
        elif self.rod.level==2:
            options=["Shallow","Mid depth"]
            depth=select_item(options)
            print (depth)
        else:
            options=["Shallow","Mid depth","The Depth"]
            depth=select_item(options)
            print (depth)
        bait=select_item(self.bait)
        if bait.name != "Worm":
            self.bait[bait.name]["count"]-=1
        for fish in fish_dict[depth]:#35,30,20,5,10 need to add something that makes the bait have influence(maybe bring in the baits multiplier attribute)
            luck=random.randint(0,100)
            catch=False
            if luck<=fish_dict[depth][fish]().chance:
                print(f"You caught a {fish}!")
                catch=True
                ###
                fish_count={}
                fish_count["class"]=fish_dict[depth][fish]
                try:
                    fish_count["count"]=self.fish[fish]["count"]
                    fish_count["count"]+=1
                except:
                    fish_count["count"]=1
                self.fish[fish]=fish_count #from the triple hash onwards is code to try update self.bait
                break
        if catch==False:
            print ("You caught nothing :(")
    def shop(self):
        print("Welcome! Would you like to buy something or sell some fish?")
        options=["Buy something","Sell fish","Back"]
        choice=select_item(options)
        if choice=="Sell fish":
            if self.fish=={}:
                print("You dont have any fish to sell!")
            else:
                confirmation="No"
                fish=None
                while fish!="Back":
                    while confirmation=="No":
                        print("Which fish are you looking to sell?")
                        choices=self.fish
                        choices["Back"]= "Back"
                        fish=select_item(choices)
                        if fish=="Back":
                            break
                        print(f"Sell {fish.name} for {fish.price}?")
                        confirmation=select_item(["Yes","No"])
                    if fish=="Back":
                        break
                    amount=int(input(f"How many? You have:{self.fish[fish.name]['count']}"))
                    if amount==0:
                        print("Do you want to sell this fish?")
                        confirmation=select_item(["Yes","No"])
                    elif amount>self.fish[fish.name]["count"]:
                        print("You dont have that many!")
                    else:
                        self.fish[fish.name]["count"]-=amount #i have to change this into the player entering a number
                        if amount==1:
                            print(f"Thank you for the {fish.name}! Heres your {fish.price*amount} coins")
                        else:
                            print(f"Thank you for the {amount} {fish.name}s! Heres your {fish.price*amount} coins")
                        self.money+=fish.price*amount
                        return None
                        #need to make it so that money goes to the player - done i think
        elif choice =="Back":
            return None
        else:
            choice="No"
            while choice=="No": #makes sure to loop till u confirm what u wanna buy
                print("What would you like to buy?")
                buy=self.shop_inv
                buy["Back"]="Back"
                choice=select_item(buy)
                if choice == "Back": #takes u back
                    return None
                if choice.cost>self.money:
                    print("You cant afford this!")
                    choice="No"
                else:
                    if choice.__class__!=fishing_rod: #checks if ur buying bait
                        while True:
                            try:
                                quantity=int(input("How many would you like?"))
                                if quantity==0:
                                    print("Do you want to buy this?")
                                    decision=select_item(["Yes","No"])
                                    if decision== "Yes":
                                        continue
                                    else:
                                        choice="No"
                                        break
                                elif self.money/choice.cost >= quantity:
                                    print(f"Would you like to buy {quantity} {choice.name} for {choice.cost*quantity}?")
                                    decision=select_item(["Yes","No"])
                                    if decision== "Yes":
                                        self.money-= choice.cost*quantity
                                        self.bait[choice.name]["count"]+=quantity
                                        print("Here you go!")
                                        choice="No"
                                        break
                                    else:
                                        choice="No"
                                        break
                                else:
                                    print("You cant afford that many!")
                            except:
                                print("Invalid input")
                    else:
                        print(f"Would you like to buy {choice.name} for {choice.cost}?")
                        decision= select_item(["Yes","No"])
                        if decision=="Yes":
                            self.money-= choice.cost
                            self.rod=fishing_rod(self.rod.level+1)
                            if self.rod.level==2:
                                del self.shop_inv["Plastic rod"]
                                b={"Titanium rod":{"object":fishing_rod(3)}}
                                self.shop_inv={**b,**self.shop_inv}
                            elif self.rod.level==3:
                                del self.shop_inv["Titanium rod"]
                                b={"Mystic rod":{"object":fishing_rod(4)}}
                                self.shop_inv={**b,**self.shop_inv}
                            elif self.rod.level==4:
                                del self.shop_inv["Mystic rod"]
                            choice="No"
                            print("Here you go!")
                        else:
                            choice="No"
    def quitting(self):
        print("Do you wanna quit?")
        decision=select_item(["Yes","No"])
        if decision=="Yes":
            return quit()
        else:
            return None
    def inv_check(self):
        for x in list(self.inventory.keys()):
            print("\n"+x+": ", end="")
            if x=="Fishing rod":
                print(self.rod.name, end="")
            elif x=="Money":
                print(self.inventory[x])
            else:
                for y in (list(self.inventory[x])):
                    if self.inventory[x][y]["count"]!=0:
                        print(y+" - ", end="")
                        print(self.inventory[x][y]["count"]," ", end="") #i wanna check if u can put the space in end

    def start(self):
        print("Menu:")
        func_dict={"Fish":self.fishing,"Craft bait":self.craft,"Enter shop":self.shop,"Leave game":self.quitting,"Check inventory":self.inv_check}
        action=select_item(func_dict)


user = input("name please ")
Player=Fisher(user)
print(f"Welcome to fish land {user}! What would you like to do today?")
while True:
    Player.start()