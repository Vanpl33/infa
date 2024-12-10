from random import randint, choice

# -----------------


def select_hero():
    while True:
        print("Wybierz postać:")
        print("1 - Solaris (450 HP, 200 Mana)")
        print("2 - Maximus (400 HP, 300 Mana)")
        print("3 - Arcaneus (200 HP, 500 Mana)")

        choice = input("Wybierz 1, 2 lub 3: ")
        if choice == "1":
            print("""
                ☀☀☀
                Solaris - Wojownik słońca!
                ☀☀☀
                "Twoje imię zostanie zapisane w gwiazdach!"
            """)
            return "Solaris", 450, 200, 5, "sun_burst"
        elif choice == "2":
            print("""
                🛡️🏆🛡️
                Maximus - Potężny gladiator!
                🛡️🏆🛡️
                "Chwała to moje drugie imię!"
            """)
            return "Maximus", 400, 300, 3, "power_slam"
        elif choice == "3":
            print("""
                ✨✨✨
                Arcaneus - Mistrz magii!
                ✨✨✨
                "Moc jest moim sprzymierzeńcem!"
            """)
            return "Arcaneus", 200, 500, 4, "arcane_blast"
        else:
            print("Niepoprawny wybór. Spróbuj ponownie.")

# -----------------



def sun_burst(hp, mana):
    if hp < 50 or mana < 50:
        print("Za mało zasobów na użycie tego ataku!")
        return 0, hp, mana
    print("""
        ☀☀☀
        Eksplozja słoneczna!
        ☀☀☀
    """)
    mana -= 50
    return 120, hp, mana

def power_slam(hp, mana):
    if mana < 75:
        print("Za mało many!")
        return 0, hp, mana
    print("""
        🔨 BAM! Uderzenie mocy!
        🔨
    """)
    mana -= 75
    return 100, hp, mana

def arcane_blast(hp, mana):
    if mana < 100:
        print("Za mało many!")
        return 0, hp, mana
    print("""
        ✨✨ ARCANE BLAST! ✨✨
    """)
    mana -= 100
    return 150, hp, mana

def perform_attack(attack_name, hp, mana):
    if attack_name == "sun_burst":
        return sun_burst(hp, mana)
    elif attack_name == "power_slam":
        return power_slam(hp, mana)
    elif attack_name == "arcane_blast":
        return arcane_blast(hp, mana)
    else:
        return 0, hp, mana

# -----------------



def random_enemy(kill_count):
    bosses = [
        ("MegaBoss", 600, 80),
        ("UltraBoss", 800, 100),
    ]
    
    enemies = [
        ("Zombie", 50, 10),
        ("Wolf", 70, 15),
        ("Goblin", 30, 5),
    ]

    if kill_count % 10 == 0 and kill_count > 0:
        return choice(bosses)
    return choice(enemies)

# -----------------



def fight():
    hero_name, hp, mana, luck, special_attack = select_hero()
    kills = 0

    print(f"Rozpoczynasz przygodę jako {hero_name}!")

    while hp > 0:
        enemy_name, enemy_hp, enemy_damage = random_enemy(kills)
        print(f"Nowy przeciwnik: {enemy_name} - {enemy_hp} HP, zadaje {enemy_damage} obrażeń na turę.")

        while enemy_hp > 0 and hp > 0:
            print(f"Twoje statystyki: {hp} HP, {mana} Mana.")
            print(f"1 - Atak fizyczny (5-10 obrażeń)")
            print(f"2 - Specjalny atak: {special_attack}")
            action = input("Wybierz akcję: ")

            if action == "1":
                damage = randint(5, 10)
                enemy_hp -= damage
                print(f"Zadałeś {damage} obrażeń przeciwnikowi.")
            elif action == "2":
                damage, hp, mana = perform_attack(special_attack, hp, mana)
                enemy_hp -= damage
                print(f"Zadałeś {damage} obrażeń przeciwnikowi.")
            else:
                print("Niepoprawny wybór. Przeciwnik cię atakuje!")

            hp -= enemy_damage
            print(f"{enemy_name} zadaje ci {enemy_damage} obrażeń.")

        if hp <= 0:
            break

        print(f"Pokonałeś {enemy_name}!")
        kills += 1

        if kills % luck == 0:
            hp += 50
            mana += 30
            print("Odzyskałeś 50 HP i 30 many!")

    print(f"Koniec gry! Pokonałeś {kills} przeciwników.")

# -----------------



if __name__ == "__main__":
    fight()

# -----------------



def heal(hero_hp, hero_mana):
    healing_potion = randint(20, 50)
    mana_restore = randint(10, 30)
    hero_hp += healing_potion
    hero_mana += mana_restore
    print(f"Znalazłeś eliksir, odzyskujesz {healing_potion} HP i {mana_restore} Many.")
    return hero_hp, hero_mana

def find_loot(kills):
    if kills % 5 == 0:
        loot_type = choice(["weapon_upgrade", "armor_upgrade", "extra_health"])
        if loot_type == "weapon_upgrade":
            print("Znalazłeś ulepszenie broni! Ataki zadają więcej obrażeń.")
        elif loot_type == "armor_upgrade":
            print("Znalazłeś lepszą zbroję! Otrzymujesz mniej obrażeń.")
        elif loot_type == "extra_health":
            print("Znalazłeś kryształ życia! Twoje HP zostało zwiększone o 30 punktów.")

# -----------------




def evade_chance():
    chance = randint(1, 100)
    if chance <= 15:
        print("Udało Ci się uniknąć ataku przeciwnika!")
        return True
    return False

# ---------------




def enhanced_enemy(enemy_name, enemy_hp, enemy_damage):
    mutation_chance = randint(1, 100)
    if mutation_chance <= 20:
        enemy_name += " (Zmutowany)"
        enemy_hp = int(enemy_hp * 1.5)
        enemy_damage = int(enemy_damage * 1.5)
        print(f"Przeciwnik mutuje! {enemy_name} ma teraz {enemy_hp} HP i zadaje {enemy_damage} obrażeń.")
    return enemy_name, enemy_hp, enemy_damage

# -----------------




def fight_with_enhancements():
    hero_name, hp, mana, luck, special_attack = select_hero()
    kills = 0

    print(f"Przygotuj się na epicką podróż, {hero_name}!")

    while hp > 0:
        enemy_name, enemy_hp, enemy_damage = random_enemy(kills)
        enemy_name, enemy_hp, enemy_damage = enhanced_enemy(enemy_name, enemy_hp, enemy_damage)

        print(f"Napotykasz przeciwnika: {enemy_name} ({enemy_hp} HP, {enemy_damage} obrażeń na turę).")

        while enemy_hp > 0 and hp > 0:
            print(f"Twoje statystyki: {hp} HP, {mana} Mana.")
            if evade_chance():
                print(f"Dzięki refleksowi unikasz ataku {enemy_name}!")
                continue

            print(f"1 - Atak fizyczny (5-10 obrażeń)")
            print(f"2 - Specjalny atak: {special_attack}")
            action = input("Wybierz akcję: ")

            if action == "1":
                damage = randint(5, 10)
                enemy_hp -= damage
                print(f"Zadałeś {damage} obrażeń przeciwnikowi.")
            elif action == "2":
                damage, hp, mana = perform_attack(special_attack, hp, mana)
                enemy_hp -= damage
                print(f"Zadałeś {damage} obrażeń przeciwnikowi.")
            else:
                print("Niepoprawny wybór. Przeciwnik cię atakuje!")

            hp -= enemy_damage
            print(f"{enemy_name} zadaje ci {enemy_damage} obrażeń.")

        if hp <= 0:
            break

        print(f"Pokonałeś {enemy_name}!")
        kills += 1
        hp, mana = heal(hp, mana)
        find_loot(kills)

    print(f"Koniec gry! Pokonałeś {kills} przeciwników.")


