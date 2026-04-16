from random import choice

class MenuItem:
    def __init__(self):
        self.items = [
            {"name": "Kofe", "tur": "ichimlik", "miqdor": 20, "narx": {"kichik": 10, "o'rta": 20, "katta": 30}},
            {"name": "Choy", "tur": "ichimlik", "miqdor": 20, "narx": {"kichik": 8, "o'rta": 16, "katta": 24}},
            {"name": "Tort", "tur": "shirinlik", "miqdor": 10, "narx": {"kichik": 15, "o'rta": 25, "katta": 35}}
        ]

    def serve(self, item):
        if item["miqdor"] == 0:
            self.restock(item)

        item["miqdor"] -= 1

    def restock(self, item):
        item["miqdor"] = 20 if item["tur"] == "ichimlik" else 10

class Customer:
    def __init__(self, name, thing:MenuItem):
        self.name = name
        self.thing = thing
        self.__balance = 100
        self.count = 0
        self.revive = 1
        self.top_up_used = False

    def buy(self):
        thing = choice(self.thing.items)
        size = choice(list(thing['narx'].keys()))
        price = thing['narx'][size]

        if self.__balance < price:
            print(f"{self.name} pul yetarli emas💸")
            return False

        self.__balance -= price
        self.thing.serve(thing)
        self.count += 1

        print(f"{self.name} {size} {thing['name']} oldi, qoldi: {self.__balance}💲")
        return True

    def top_up(self):
        if self.top_up_used:
            return False
        if self.__balance > 0:
            self.__balance += 50
            print(f"{self.name} balans to'ldirdi ✔")
            return True
        else:
            print(f"{self.name} bankrot 💀")

            if self.revive > 0:
                self.__balance = 50
                self.revive -= 1
                print(f"{self.name} revive ishladi 🔄")
                return True
            
            print(f"{self.name} chiqib ketdi 🚪")
            return False
        

menu = MenuItem()
c1 = Customer("Ali", menu)
c2 = Customer("Vali", menu)
lst = [c1, c2]

while len(lst) > 0:
    player = choice(lst)
    if not player.buy():
        player.top_up()
        if not player.top_up_used:
            lst.remove(player) 

print(f"{c1.name} {c1.count} ta xarid qilgan")
print(f"{c2.name} {c2.count} ta xarid qilgan")

if c1.count > c2.count:
    print(f"G'olib {c1.name} 🏆")
elif c2.count > c1.count:
    print(f"G'olib {c2.name} 🏆")
else:
    print("Durrang 🤝")