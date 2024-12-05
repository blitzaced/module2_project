# Defeat the Evil Wizard! |
# -------------------------

import random

# Base Character class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health                                            # Store the original health for maximum limit
        self.defensive_ability_active = False                               # Defensive ability toggle, defaulted off

    def attack(self, opponent):
        min_damage = int(self.attack_power * 0.8)                           # Damage min level
        max_damage = int(self.attack_power * 1.2)                           # Damage max level
        damage = random.randint(min_damage, max_damage)                     # Damage output randomizer
        
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

    # Add your heal method here
    def heal(self, heal_amount = 20):
        self.health += heal_amount
        self.health = min(self.health, self.max_health)                     # Healing condition so healing does not exceed max health
        print(f"{self.name} heals themself for {heal_amount} health!")
       

# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)                 # Boost health and attack power
        
    # Add your special ability methods here
    def use_shield(self):
        print(f"{self.name} raises their shield to block the next attack!")
        self.defensive_ability_active = True                                # Defensive ability toggled on
        
    def use_smash(self, opponent):
        smash_damage = self.attack_power * 1.2                              # Offensive ability bonus damage modifier
        opponent.health -= smash_damage
        print(f"{self.name} smashes {opponent.name} with their mace for {smash_damage:.1f} damage!")

# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)                 # Boost attack power
       
    # Add your special ability methods here
    def cast_vanish(self):
        print(f"{self.name} disappears from sight!")
        self.defensive_ability_active = True                                # Defensive ability toggled on
    
    def cast_thunderbolt(self, opponent):
        thunderbolt_damage = self.attack_power * 1.3                        # Offensive ability bonus damage modifier
        opponent.health -= thunderbolt_damage
        print(f"{self.name} shocks {opponent.name} with an electrifying thunderbolt for {thunderbolt_damage:.1f} damage!")

# Sage class (inherits from Character)
class Sage(Character):
    def __init__(self, name):
        super().__init__(name, health=110, attack_power=15)                 # Boost health and attack power
                
    # Add your special ability methods here
    def cast_mist(self):
        print(f"{self.name} fades into an inpenetrable mist!")
        self.defensive_ability_active = True                                # Defensive ability toggled on
        
    def cast_smite(self, opponent):
        smite_damage = self.attack_power * 1.1                              # Offensive ability bonus damage modifier
        opponent.health -= smite_damage
        print(f"{self.name} smites {opponent.name} with holy light for {smite_damage:.1f} damage!")
            
class Dragoon(Character):
    def __init__(self, name):
        super().__init__(name, health = 125, attack_power=30)               # Boost health and attack power
        self.defensive_ability_active = False
        
    # Add your special ability methods here        
    def use_parry(self):
        print(f"{self.name} will parry the next attack!")
        self.defensive_ability_active = True                                # Defensive ability toggled on
        
    def use_jump(self, opponent):
        jump_damage = self.attack_power * 1.25                              # Offensive ability bonus damage modifier
        opponent.health -= jump_damage
        print(f"{self.name} jumps down on {opponent.name} with their lance for {jump_damage:.1f} damage!")

# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)                 # Lower attack power
    
    # Evil Wizard's special ability: it can regenerate health
    def regenerate(self):
        if self.health > 0:
            self.health += 5                                                # Lower regeneration amount
            self.health = min(self.health, self.max_health)                 # Conditional so wizard does not exceed max health
            print(f"{self.name} regenerates 5 health! Current health: {self.health}")

# Function to create player character based on user input
def create_character():
    while True:
        print("Choose your character class:")
        print("1. Warrior")
        print("2. Mage")
        print("3. Sage")                                                    # Add Healer Class      
        print("4. Dragoon")                                                 # Add Melee Class       
    
        class_choice = input("Enter the number of your class choice: ")
        
        if class_choice in ['1', '2', '3', '4']:
            break
        else:
            print("Invalid choice. Please select a valid class.")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        heal_amount = 20
        return Sage(name)                                                   # Add Healer class here
    elif class_choice == '4':
        return Dragoon(name)                                                # Add Melee class here              
    
# Battle function with user menu for actions
def battle(player, wizard):
    heal_amount = 20
    
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Offensive Ability")                                   # Split Special Ability option from starter code
        print("3. Use Defensive Ability")                                   # Split Special Ability option from starter code
        print("4. Heal")
        print("5. View Stats")
        
        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':                                                 # New action option: Offensive ability                 
            # Call the special ability here                                 # Perform a powerful class-based attack
            if isinstance(player, Warrior):
                player.use_smash(wizard)
            elif isinstance(player, Mage):
                player.cast_thunderbolt(wizard)
            elif isinstance(player, Sage):
                player.cast_smite(wizard)
            elif isinstance(player, Dragoon):
                player.use_jump(wizard)
        elif choice == '3':                                                # New action option: Defensive ability
            # Call the special ability here                                # Nullfies the wizard's next attack
            if isinstance(player, Warrior):
                player.use_shield()
            elif isinstance(player, Mage):
                player.cast_vanish()
            elif isinstance(player, Sage):
                player.cast_mist()
            elif isinstance(player, Dragoon):
                player.use_parry()
        elif choice == '4':                                                # Call the heal method here                            
            player.heal(heal_amount)
        elif choice == '5':                                 
            player.display_stats()
        else:
            print("Invalid choice, try again.")
            continue

# Evil Wizard's turn to attack and regenerate
        if wizard.health > 0:
            if player.defensive_ability_active:
                print(f"{player.name} is protected by their defensive ability! The wizard's attack is nullified!")
                player.defensive_ability_active = False
            else:
                wizard.attack(player)
        
            if player.health > 0:                                               # Wizard won't regen health after player defeat
                wizard.regenerate()

        if player.health <= 0:
                print(f"{player.name} has been defeated!")
                break
 
    if wizard.health <= 0:
        print(f"{wizard.name} has been defeated by {player.name}!")

# Main function to handle the flow of the game
def main():
    # Character creation phase
    player = create_character()

    # Evil Wizard is created
    wizard = EvilWizard("The Dark Wizard")

    # Start the battle
    battle(player, wizard)

if __name__ == "__main__":
    main()