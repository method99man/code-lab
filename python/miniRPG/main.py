import random  # moduł do losowości (damage, crit, loot, wybór przeciwnika)


# ========================
# KLASA BAZOWA POSTACI
# ========================
class Character:
    def __init__(self, name, hp, attack):
        self.name = name            # nazwa postaci
        self.hp = hp                # aktualne HP
        self.max_hp = hp            # maksymalne HP (do leczenia)
        self.attack = attack        # bazowy atak

    # metoda ataku na inny obiekt (Player lub Enemy)
    def attack_target(self, target):
        # losowy damage w zakresie +/- 3
        damage = random.randint(self.attack - 3, self.attack + 3)

        # 20% szansy na critical hit
        crit = random.random() < 0.2

        if crit:
            target.hp -= damage * 2
            print(f"💥 CRIT! {self.name} attacks {target.name} for {damage} damage!")
        else:
            target.hp -= damage
            print(f"{self.name} attacks {target.name} for {damage} damage!")

        # zabezpieczenie żeby HP nie spadło poniżej 0
        if target.hp < 0:
            target.hp = 0

    # leczenie postaci
    def heal(self, heal_value=10):
        heal_ammount = heal_value
        self.hp += heal_ammount

        # nie przekraczamy max HP
        if self.hp > self.max_hp:
            self.hp = self.max_hp

        print(f"{self.name} heals for {heal_ammount}HP!")

    # użycie przedmiotu (np. potion)
    def use_item(self):
        # sprawdzamy czy gracz ma potion
        if "potion" in self.inventory:
            self.inventory.remove("potion")  # usuwamy potion z inventory
            print("Used potion!")
            self.heal(15)  # potion leczy więcej niż zwykły heal
        else:
            print("No potions!")

    # sprawdza czy postać żyje
    def is_alive(self):
        return self.hp > 0


# ========================
# GRACZ
# ========================
class Player(Character):
    def __init__(self, name):
        super().__init__(name, 100, 10)  # startowe staty
        self.inventory = ["potion", "potion"]  # startowy ekwipunek


# ========================
# PRZECIWNIK
# ========================
class Enemy(Character):
    pass  # na razie nic dodatkowego


# ========================
# TWORZENIE GRY
# ========================

player = Player("Hero")

# lista możliwych przeciwników
enemies = [
    Enemy("Goblin", 30, 5),
    Enemy("Orc", 50, 8),
    Enemy("Dragon", 100, 25)
]

# losowy wybór przeciwnika
enemy = random.choice(enemies)


# ========================
# GŁÓWNA PĘTLA WALKI
# ========================
while player.is_alive() and enemy.is_alive():

    print("\n--- New Turn ---")
    print(f"{player.name} HP: {player.hp}")
    print(f"{enemy.name} HP: {enemy.hp}")

    # wybór akcji przez gracza
    action = input("1. Attack\n2. Heal(10HP)\n3. Use Potion(15HP)\nChoose action: ")

    if action == "1":
        player.attack_target(enemy)
    elif action == "2":
        player.heal()
    elif action == "3":
        player.use_item()

    # tura przeciwnika (jeśli żyje)
    if enemy.is_alive():
        if enemy.hp < 10:
            enemy.heal()  # AI leczy się przy niskim HP
        else:
            enemy.attack_target(player)


# ========================
# KONIEC WALKI
# ========================
print("\n--- Battle End ---")

if player.is_alive():
    print("You won!")

    # system lootu (70% szansy na potion)
    drop = random.random()

    if drop < 0.7:
        print("You have found a potion!")
        player.inventory.append("potion")
    else:
        print("No loot this time 😢")

else:
    print("You lost!")