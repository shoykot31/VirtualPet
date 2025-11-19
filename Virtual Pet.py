import time
import random
import os

# --------------------------
# ASCII ART FOR PET MOODS
# --------------------------
ASCII = {
    "happy": r"""
   /\_/\ 
  ( ^.^ )  ~ Happy!
   > ^ <
""",
    "hungry": r"""
   /\_/\ 
  ( •.• )  ~ Hungry...
   > ^ <
""",
    "sleepy": r"""
   /\_/\ 
  ( -.- ) zZ
   > ^ <
""",
    "angry": r"""
   /\_/\ 
  ( >.< )  ~ Mad!
   > ^ <
""",
    "dead": r"""
   x _ x
  (  ... ) 
   > ^ <
""",
}

# --------------------------
# PET CLASS
# --------------------------
class Pet:
    def __init__(self, name):
        self.name = name
        self.stage = "Baby"     # evolution stage
        self.age = 0            # time survived
        self.hunger = 60
        self.happiness = 60
        self.energy = 60
        self.alive = True

        # Inventory & coins
        self.inventory = {"Food": 2, "Toy": 1, "Energy Drink": 1}
        self.coins = 5

    # --- EVOLUTION LOGIC ---
    def evolve_check(self):
        if self.age > 10 and self.stage == "Baby":
            self.stage = "Teen"
            print(f"\n🌱 {self.name} has evolved into a Teen!")
            time.sleep(1)
        elif self.age > 25 and self.stage == "Teen":
            self.stage = "Adult"
            print(f"\n🌳 {self.name} has evolved into an Adult!")
            time.sleep(1)
        elif self.age > 45 and self.stage == "Adult":
            self.stage = "Legendary"
            print(f"\n🔥 {self.name} has evolved into a LEGENDARY form!")
            time.sleep(1)

    # --- DISPLAY ASCII ART ---
    def show_ascii(self):
        if not self.alive:
            print(ASCII["dead"])
            return
        if self.hunger < 30:
            print(ASCII["hungry"])
        elif self.energy < 30:
            print(ASCII["sleepy"])
        elif self.happiness < 30:
            print(ASCII["angry"])
        else:
            print(ASCII["happy"])

    # --- SHOW STATS ---
    def show_stats(self):
        print(f"--- {self.name} the {self.stage} ---")
        print(f"Age: {self.age}")
        print(f"Hunger:    {self.hunger}")
        print(f"Happiness: {self.happiness}")
        print(f"Energy:    {self.energy}")
        print(f"Coins:     {self.coins}")
        print("Inventory:", self.inventory)
        print("-------------------------\n")

    # --- ACTIONS ---
    def feed(self):
        if self.inventory["Food"] > 0:
            print(f"You give food to {self.name}. 🍖")
            self.inventory["Food"] -= 1
            self.hunger = min(100, self.hunger + 25)
        else:
            print("You have no food!")

    def play(self):
        if self.inventory["Toy"] > 0:
            print(f"You play with {self.name}! 🎾")
            self.happiness = min(100, self.happiness + 20)
            self.inventory["Toy"] -= 1
            self.energy -= 5
        else:
            print("You have no toys!")

    def drink_energy(self):
        if self.inventory["Energy Drink"] > 0:
            print(f"{self.name} drinks an energy drink! ⚡")
            self.energy = min(100, self.energy + 40)
            self.inventory["Energy Drink"] -= 1
        else:
            print("You're out of energy drinks!")

    # --- SHOP ---
    def shop(self):
        print("\n--- Shop ---")
        print("1. Food (3 coins)")
        print("2. Toy (4 coins)")
        print("3. Energy Drink (5 coins)")
        print("4. Cancel")
        choice = input("> ")

        if choice == "1" and self.coins >= 3:
            self.coins -= 3
            self.inventory["Food"] += 1
            print("Bought Food!")
        elif choice == "2" and self.coins >= 4:
            self.coins -= 4
            self.inventory["Toy"] += 1
            print("Bought Toy!")
        elif choice == "3" and self.coins >= 5:
            self.coins -= 5
            self.inventory["Energy Drink"] += 1
            print("Bought Energy Drink!")
        else:
            print("Not enough coins or invalid choice!")

    # --- TIME PASSING ---
    def tick(self):
        self.age += 1

        self.hunger -= random.randint(3, 7)
        self.happiness -= random.randint(2, 6)
        self.energy -= random.randint(2, 5)

        # Earn coins for surviving
        self.coins += 1

        if min(self.hunger, self.happiness, self.energy) <= 0:
            self.alive = False
        
        self.evolve_check()


# --------------------------
# GAME LOOP
# --------------------------
def clear():
    os.system("cls" if os.name == "nt" else "clear")

def game():
    clear()
    name = input("Name your virtual pet: ")
    pet = Pet(name)

    while pet.alive:
        clear()
        pet.show_ascii()
        pet.show_stats()

        print("What would you like to do?")
        print("1. Feed")
        print("2. Play")
        print("3. Energy Drink")
        print("4. Visit Shop")
        print("5. Do nothing")

        choice = input("> ")

        if choice == "1":
            pet.feed()
        elif choice == "2":
            pet.play()
        elif choice == "3":
            pet.drink_energy()
        elif choice == "4":
            pet.shop()
        else:
            print(f"{pet.name} wanders around...")

        time.sleep(1)
        pet.tick()

    clear()
    print(ASCII["dead"])
    print(f"\n💀 {pet.name} has passed away at age {pet.age}.\n")

game()
