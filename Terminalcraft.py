#TO RUN THIS GAME, PLEASE ENTER THE FOLLOEING COMMAND:
"""python -W ignore .\Terminalcraft.py"""
#TO RUN THIS GAME, PLEASE ENTER THE FOLLOEING COMMAND:
"""python -W ignore .\Terminalcraft.py"""




import datetime
import random
import sys

# Game Data
grocery = {
    'bread': 10,
    'cheese': 15,
    'wine': 50
}

botanical_nursery = {
    'rose': 5,
    'herbs': 8,
    'magic beans': 100
}

farmers_market = {
    'apple': 2,
    'carrot': 1,
    'potato': 3
}

freelancers = {
    'brian': 700,
    'black knight': 200,
    'biccus diccus': 1000,
    'grim reaper': 5000,
    'minstrel': 000,
    'god': 1000000,
    'nordic': 2000,
    'mage': 5000,
    'ze germane': 1000,
}

antiques = {
    'french castle': 400,
    'wooden grail': 3,
    'scythe': 1500,
    'catapult': 75,
    'german joke': 5,
    'spear': 100,
    'axe': 200,
    'peace': -2000,
    'rock': 10000,
    'healing potion': 200,
    'body armor': 2000,
}

pet_shop = {
    'blue parrot': 100,
    'white rabbit': 50,
    'newt': 20,
    'wolf': 250,
    'dragon': 1000,
    'serpent': 500
}

village_quests = {
    'hunt wild boar': {'reward': 150, 'description': 'A wild boar terrorizes the fields!'},
    'deliver message to next village': {'reward': 80, 'description': 'Urgent message needs delivery!'},
    'find lost sheep': {'reward': 60, 'description': 'Farmer Johann lost his prize sheep!'},
    'escort merchant caravan': {'reward': 200, 'description': 'Dangerous roads need protection!'},
    'gather rare herbs': {'reward': 120, 'description': 'Village healer needs mystical herbs!'},
    'repair village well': {'reward': 100, 'description': 'Well broken, villagers thirsty!'},
    'catch pickpocket': {'reward': 180, 'description': 'Thief stealing from market stalls!'},
    'explore haunted ruins': {'reward': 300, 'description': 'Ancient ruins hold treasure... and danger!'},
    'tame wild horse': {'reward': 250, 'description': 'Magnificent stallion roams the plains!'},
    'brew healing elixir': {'reward': 140, 'description': 'Village plagued by mysterious illness!'}
}

blacksmith_jobs = {
    'sharpen village weapons': {'reward': 90, 'description': 'Village guard needs weapon maintenance!'},
    'forge horseshoes': {'reward': 50, 'description': 'Stable master needs quality horseshoes!'},
    'repair armor': {'reward': 70, 'description': 'Damaged armor from last skirmish!'},
    'craft ceremonial sword': {'reward': 200, 'description': 'Noble wedding needs special blade!'}
}

tavern_activities = {
    'arm wrestling contest': {'reward': 75, 'description': 'Test your strength against locals!'},
    'storytelling night': {'reward': 50, 'description': 'Entertain patrons with epic tales!'},
    'drinking contest': {'reward': 40, 'description': 'Last one standing wins the pot!'},
    'solve riddle challenge': {'reward': 85, 'description': 'Old sage poses mysterious riddles!'},
    'bard performance': {'reward': 65, 'description': 'Play music for coin and glory!'}
}

random_events = [
    {'event': 'You find a purse dropped by a merchant!', 'gold': 45},
    {'event': 'A grateful villager tips you for your heroic reputation!', 'gold': 30},
    {'event': 'You discover ancient coins while walking!', 'gold': 80},
    {'event': 'A mysterious stranger pays you for information!', 'gold': 60},
    {'event': 'You help catch a runaway pig and get rewarded!', 'gold': 25},
    {'event': 'You find treasure in an old barrel!', 'gold': 95},
    {'event': 'A noble appreciates your service to the village!', 'gold': 120}
]

# Game State
completed_quests = []
time_of_day = "morning"
weather = "clear"
gold = 10000
cart = ["healing potion"]
game_ended = False

# START MAIN GAME LOGIC
print("=== MEDIEVAL VILLAGE DEFENSE ===")
print("Welcome, brave hero!")

# Get start game input -        get_valid_input .
while True:
    start_input = input("Shall we begin our adventure? (y/n): ").lower()
    if start_input == 'y':
        break
    elif start_input == 'n':
        print("Game cancelled!")
        sys.exit()

# Get player name
player_name = input("Enter character name: ")


# Show intro - show_intro .
print(f"""
=== MEDIEVAL VILLAGE DEFENSE ===

Sir {player_name}!
Your village is under attack by a Germanic tribe! 
You must gather allies, weapons, and supplies to defend your home.
The fate of your village (and that special someone) depends on you!

Current Status: {time_of_day.title()}, {weather} weather
Ze germanz are approaching... time is running out!
""")

# Main game loop
while not game_ended:
    # Show atmosphere -  show_atmosphere .
    if time_of_day == "morning":
        print("\nThe morning sun casts long shadows across the cobblestones. Birds chirp in the distance.")
    elif time_of_day == "afternoon":
        print("\nThe afternoon sun beats down warmly. The village bustles with activity.")
    elif time_of_day == "evening":
        print("\nThe evening air carries the scent of cooking fires. Lanterns begin to flicker on.")
    elif time_of_day == "night":
        print("\nThe night is quiet except for distant tavern laughter. Stars twinkle overhead.")
    
    # Weather description - g get_weather_description .
    import random
    if weather == "clear":
        print("The sky is clear and bright.")
    elif weather == "cloudy":
        print("Gray clouds gather overhead.")
    elif weather == "rainy":
        print("Light rain patters on the rooftops.")
    elif weather == "foggy":
        print("A thick fog rolls through the streets.")
    
    # Show main menu -  show_main_menu .
    print(f"\n=== MAIN MENU ===")
    print("i. Check Inventory")
    print("s. Visit Shops")
    print("b. Battle Germanic Tribes")
    print("q. Quit Game")
    print()
    
    # Get main menu choice - get_menu_choice .
    while True:
        main_choice = input("Choose an option: ").strip().lower().replace(' ', '')
        if main_choice in ['i', 's', 'b', 'q', 'back', '//']:
            break
    
    if main_choice == 'q':
        print("Thanks for playing!")
        game_ended = True
    elif main_choice == 'i':
        # Show inventory - show_inventory .
        print(f"\n=== INVENTORY ===")
        print(f"Gold: {gold}")
        print(f"Items: {', '.join(cart) if cart else 'None'}")
        print(f"Completed Quests: {len(completed_quests)}")
        input("Press Enter to continue...")
    elif main_choice == 'b':
        # Check battle ready -  check_battle_ready .
        battle_items = ['brian', 'black knight', 'grim reaper', 'god', 'mage', 'nordic', 'biccus diccus']
        battle_ready = False
        for item in battle_items:
            if item in cart:
                battle_ready = True
                break
        
        if battle_ready:
            print("You enter battle with your assembled forces!")
            print("YOU WON! Thanks for playing!")
            game_ended = True
        else:
            print("You need allies or weapons before you can battle!")
            input("Press Enter to continue...")
    elif main_choice == 's':
        # Shop selection loop -  handle_shop_selection .
        shop_loop = True
        while shop_loop and not game_ended:
            print("\n=== VILLAGE SHOPS ===")
            print("1. Freelancers")
            print("2. Antiques")
            print("3. Pet Shop")
            print("4. Grocery")
            print("5. Botanical Nursery")
            print("6. Farmers Market")
            print("7. Quest Board")
            
            # Get shop choice
            while True:
                shop_choice = input("Which shop? (1-7 or 'back'): ").strip().lower().replace(' ', '')
                if shop_choice in ['1', '2', '3', '4', '5', '6', '7', 'back']:
                    break
            
            if shop_choice == 'back':
                shop_loop = False
                continue
            
            # Handle different shop choices
            if shop_choice == '1':
                # FREELANCERS SHOP - visit_freelancers .
                print("\n--- Entering Freelancers ---")
                print(f"\n=== FREELANCERS GUILD ===")
                print("The guild hall echoes with the sounds of sharpening weapons and hushed conversations.")
                
                print("\nAvailable Freelancers:")
                for name, price in freelancers.items():
                    print(f"- {name.title()}: {price} gold")
                
                # Get freelancer choice
                freelancer_options = list(freelancers.keys()) + ['exit']
                while True:
                    freelancer_choice = input("Select a freelancer or 'exit': ").strip().lower().replace(' ', '')
                    if freelancer_choice in freelancer_options:
                        break
                
                if freelancer_choice != 'exit':
                    # Process freelancer choice - process_freelancer_choice .
                    price = freelancers[freelancer_choice]
                    
                    if freelancer_choice == 'minstrel' or freelancer_choice == 'minstrel2':
                        print(f"You hired the minstrel... but he killed and looted you!")
                        print("YOU DIED! Thanks for playing.")
                        game_ended = True
                        break
                    
                    if freelancer_choice == 'ze germane':
                        print(f"You hired ze germane... but he betrayed you immediately!")
                        print("YOU DIED! Thanks for playing.")
                        game_ended = True
                        break
                    
                    if gold < price:
                        print("Not enough gold!")
                    else:
                        gold -= price
                        cart.append(freelancer_choice)
                        freelancers.pop(freelancer_choice)  # Remove from shop
                        
                        while True:
                            battle_choice = input("Ready for battle? (yes/no/inventory): ").strip().lower().replace(' ', '')
                            if battle_choice in ['yes', 'no', 'inventory']:
                                break
                        
                        if battle_choice == 'inventory':
                            print(f"\n=== INVENTORY ===")
                            print(f"Gold: {gold}")
                            print(f"Items: {', '.join(cart) if cart else 'None'}")
                            print(f"Completed Quests: {len(completed_quests)}")
                        elif battle_choice == 'yes':
                            # Handle freelancer battle - handle_freelancer_battle .
                            print(f"\n=== BATTLE BEGINS ===")
                            
                            if freelancer_choice == 'brian':
                                print("You used Brian as a meatshield... using the element of surprise!")
                                print("You defeated ze germanz! You're now the village king!")
                                print("YOU WON! Thanks for playing!")
                                game_ended = True
                                break
                                sys.exit()
                            elif freelancer_choice == 'black knight':
                                print("The Black Knight dies heroically in battle, winning it!")
                                print("You revive him with your healing potion.")
                                print("YOU WON! Thanks for playing!")
                                game_ended = True
                                break
                                sys.exit()
                            elif freelancer_choice == 'grim reaper':
                                print("The Grim Reaper uses 'GRIM EYES' ability...")
                                print("""
                             ___       ___
                            (_o_)     (_o_)
                           . |     /\      |.
                          (   )   /  \     (  )
                           \  /           /  /
                            \.............../
                             \_____________/   
                             """)
                                print("REAPING...............")
                                print("You defeated ze germanz and became village king!")
                                print("YOU WON! Thanks for playing!")
                                game_ended = True
                                break
                                sys.exit()
                            elif freelancer_choice == 'god':
                                print("GOD APPRECIATES JUSTICE!")
                                print("GOD used 'BRIGHT EYE' ability!")
                                print("""
        _,.--~=~"~=~--.._  
     _.-"  / \ !   ! / \  "-._  
   ,"     / ,` .---. `, \     ". 
/.'   `~  |   /:::::\   |  ~`   '.
\`.  `~   |   \:::::/   | ~`  ~ .'
  `.  `~  \ `, `~~~' ,` /   ~`.' 
    "-._   \ / !   ! \ /  _.-"  
       "=~~.._  _..~~=`"        """)
                                print("You received the blessing of god!")
                                print("YOU WON! Thanks for playing!")
                                game_ended = True
                                break
                                sys.exit()
                            else:
                                print(f"{freelancer_choice.title()} fights valiantly!")
                                print("You defeated ze germanz!")
                                print("YOU WON! Thanks for playing!")
                                game_ended = True
                                break
                                sys.exit()
            
            elif shop_choice == '2':
                # ANTIQUES SHOP - visit_generic_shop .
                print("\n--- Entering Antiques ---")
                print(f"\n=== ANTIQUE SHOP ===")
                print("Dust motes dance in the filtered sunlight. Ancient treasures gleam mysteriously.")
                
                if not antiques:
                    print("The shop is empty! Come back later.")
                else:
                    print(f"\nAvailable items:")
                    for item, price in antiques.items():
                        print(f"- {item.title()}: {price} gold")
                    
                    antique_options = list(antiques.keys()) + ['exit']
                    while True:
                        antique_choice = input("Select an item or 'exit': ").strip().lower().replace(' ', '')
                        if antique_choice in antique_options:
                            break
                    
                    if antique_choice != 'exit' and antique_choice in antiques:
                        # Process purchase -        process_purchase .
                        price = antiques[antique_choice]
                        
                        if price > 0 and gold >= price:
                            gold -= price
                            cart.append(antique_choice)
                            antiques.pop(antique_choice)
                            print(f"You bought {antique_choice} for {price} gold!")
                        
                        elif price==1000000:
                            cart.append(antique_choice)
                            antiques.pop(antique_choice)
                            print(f"You bought {antique_choice} for {price} gold!")
                        else:
                            print("Not enough gold!")
            
            elif shop_choice == '3':
                # PET SHOP -        visit_generic_shop .
                print("\n--- Entering Pet Shop ---")
                print(f"\n=== PET SHOP ===")
                print("The air fills with chirping, squeaking, and the rustle of small creatures.")
                
                if not pet_shop:
                    print("The shop is empty! Come back later.")
                else:
                    print(f"\nAvailable items:")
                    for item, price in pet_shop.items():
                        print(f"- {item.title()}: {price} gold")
                    
                    pet_options = list(pet_shop.keys()) + ['exit']
                    while True:
                        pet_choice = input("Select an item or 'exit': ").strip().lower().replace(' ', '')
                        if pet_choice in pet_options:
                            break
                    
                    if pet_choice != 'exit' and pet_choice in pet_shop:
                        # Process purchase - process_purchase 
                        price = pet_shop[pet_choice]
                        
                        if price > 0 and gold >= price:
                            gold -= price
                            cart.append(pet_choice)
                            pet_shop.pop(pet_choice)
                            print(f"You bought {pet_choice} for {price} gold!")
                            # Special item message
                            if pet_choice == 'newt':
                                print("The newt looks at you knowingly... something special about this one!")
                        elif price < 0:
                            gold += abs(price)
                            cart.append(pet_choice)
                            pet_shop.pop(pet_choice)
                            print(f"You took {pet_choice} and gained {abs(price)} gold!")
                        else:
                            print("Not enough gold!")
            
            elif shop_choice == '4':
                # GROCERY SHOP -        visit_generic_shop .
                print("\n--- Entering Grocery ---")
                print(f"\n=== GROCERY ===")
                print("The aroma of fresh bread and pungent cheese and aged wine fills your nostrils.")
                
                if not grocery:
                    print("The shop is empty! Come back later.")
                else:
                    print(f"\nAvailable items:")
                    for item, price in grocery.items():
                        print(f"- {item.title()}: {price} gold")
                    
                    grocery_options = list(grocery.keys()) + ['exit']
                    while True:
                        grocery_choice = input("Select an item or 'exit': ").strip().lower().replace(' ', '')
                        if grocery_choice in grocery_options:
                            break
                    
                    if grocery_choice != 'exit' and grocery_choice in grocery:
                        # Process purchase -        process_purchase .
                        price = grocery[grocery_choice]
                        
                        if price > 0 and gold >= price:
                            gold -= price
                            cart.append(grocery_choice)
                            grocery.pop(grocery_choice)
                            print(f"You bought {grocery_choice} for {price} gold!")
                        elif price < 0:
                            gold += abs(price)
                            cart.append(grocery_choice)
                            grocery.pop(grocery_choice)
                            print(f"You took {grocery_choice} and gained {abs(price)} gold!")
                        else:
                            print("Not enough gold!")
            
            elif shop_choice == '5':
                # BOTANICAL NURSERY -        visit_generic_shop .
                print("\n--- Entering Botanical Nursery ---")
                print(f"\n=== BOTANICAL NURSERY ===")
                print("Sweet floral scents and rich earth surround you.")
                
                if not botanical_nursery:
                    print("The shop is empty! Come back later.")
                else:
                    print(f"\nAvailable items:")
                    for item, price in botanical_nursery.items():
                        print(f"- {item.title()}: {price} gold")
                    
                    botanical_options = list(botanical_nursery.keys()) + ['exit']
                    while True:
                        botanical_choice = input("Select an item or 'exit': ").strip().lower().replace(' ', '')
                        if botanical_choice in botanical_options:
                            break
                    
                    if botanical_choice != 'exit' and botanical_choice in botanical_nursery:
                        # Process purchase -        process_purchase .
                        price = botanical_nursery[botanical_choice]
                        
                        if price > 0 and gold >= price:
                            gold -= price
                            cart.append(botanical_choice)
                            botanical_nursery.pop(botanical_choice)
                            print(f"You bought {botanical_choice} for {price} gold!")
                            # Special item message
                            if botanical_choice == 'magic beans':
                                print("These beans tingle with magical energy... they might grow into something amazing!")
                        elif price < 0:
                            gold += abs(price)
                            cart.append(botanical_choice)
                            botanical_nursery.pop(botanical_choice)
                            print(f"You took {botanical_choice} and gained {abs(price)} gold!")
                        else:
                            print("Not enough gold!")
            
            elif shop_choice == '6':
                # FARMERS MARKET -        visit_generic_shop .
                print("\n--- Entering Farmers Market ---")
                print(f"\n=== FARMERS MARKET ===")
                print("Fresh produce is arranged in colorful displays.")
                
                if not farmers_market:
                    print("The shop is empty! Come back later.")
                else:
                    print(f"\nAvailable items:")
                    for item, price in farmers_market.items():
                        print(f"- {item.title()}: {price} gold")
                    
                    farmers_options = list(farmers_market.keys()) + ['exit']
                    while True:
                        farmers_choice = input("Select an item or 'exit': ").strip().lower().replace(' ', '')
                        if farmers_choice in farmers_options:
                            break
                    
                    if farmers_choice != 'exit' and farmers_choice in farmers_market:
                        # Process purchase -        process_purchase .
                        price = farmers_market[farmers_choice]
                        
                        if price > 0 and gold >= price:
                            gold -= price
                            cart.append(farmers_choice)
                            farmers_market.pop(farmers_choice)
                            print(f"You bought {farmers_choice} for {price} gold!")
                        elif price < 0:
                            gold += abs(price)
                            cart.append(farmers_choice)
                            farmers_market.pop(farmers_choice)
                            print(f"You took {farmers_choice} and gained {abs(price)} gold!")
                        else:
                            print("Not enough gold!")
            
            elif shop_choice == '7':
                # QUEST BOARD -        visit_quest_board .
                print("\n--- Entering Quest Board ---")
                print("\n=== VILLAGE QUEST & BOUNTY BOARD ===")
                print("The wooden board creaks in the wind, covered with parchment notices.")
                
                print("\nAvailable Village Quests:")
                quest_choices = {}
                i = 1
                for quest, details in village_quests.items():
                    if quest not in completed_quests:
                        quest_choices[str(i)] = quest
                        print(f"{i}. {quest.title()} - {details['description']} [Reward: {details['reward']} gold]")
                        i += 1
                
                print("\nBlacksmith Jobs:")
                for j, (job, details) in enumerate(blacksmith_jobs.items(), 1):
                    if job not in completed_quests:
                        quest_choices[f"b{j}"] = job
                        print(f"b{j}. {job.title()} - {details['description']} [Reward: {details['reward']} gold]")
                
                print("\nTavern Activities:")
                for k, (activity, details) in enumerate(tavern_activities.items(), 1):
                    if activity not in completed_quests:
                        quest_choices[f"t{k}"] = activity
                        print(f"t{k}. {activity.title()} - {details['description']} [Reward: {details['reward']} gold]")
                
                valid_choices = list(quest_choices.keys()) + ['r', 'back']
                while True:
                    quest_choice = input("Choose a quest, 'r' for random adventure, or 'back': ").strip().lower().replace(' ', '')
                    if quest_choice in valid_choices:
                        break
                
                if quest_choice == 'back':
                    pass  # Continue to next iteration
                elif quest_choice == 'r':
                    # Random event -        handle_random_event .
                    event = random.choice(random_events)
                    print(f"\n=== RANDOM ADVENTURE ===")
                    print(f"{event['event']}")
                    gold += event['gold']
                    print(f"You gained {event['gold']} gold!")
                else:
                    # Handle quest completion -        handle_quest_completion .
                    quest_name = quest_choices[quest_choice]
                    
                    # Determine quest type and reward
                    if quest_name in village_quests:
                        reward = village_quests[quest_name]['reward']
                        quest_type = "village"
                    elif quest_name in blacksmith_jobs:
                        reward = blacksmith_jobs[quest_name]['reward']
                        quest_type = "blacksmith"
                    else:
                        reward = tavern_activities[quest_name]['reward']
                        quest_type = "tavern"
                    
                    print(f"\n=== {quest_name.upper()} ===")
                    
                    # Quest-specific adventures
                    if quest_name == 'hunt wild boar':
                        while True:
                            approach = input("How do you approach the boar? (stealth/direct/trap): ").strip().lower().replace(' ', '')
                            if approach in ['stealth', 'direct', 'trap']:
                                break
                        
                        if approach == 'stealth':
                            print("You sneak up and take the boar by surprise! Clean kill!")
                            reward += 25
                        elif approach == 'direct':
                            print("You charge head-on! Dangerous but heroic!")
                        else:
                            print("You set a clever trap! The boar walks right into it!")
                            reward += 15
                    
                    elif quest_name == 'explore haunted ruins':
                        while True:
                            approach = input("How do you explore the ruins? (careful/bold/mystical): ").strip().lower().replace(' ', '')
                            if approach in ['careful', 'bold', 'mystical']:
                                break
                        
                        if approach == 'careful':
                            print("You carefully avoid the traps and find extra treasure!")
                            reward += 50
                        elif approach == 'bold':
                            print("You boldly march through and face the dangers head-on!")
                        else:
                            print("You use mystical knowledge to commune with the spirits!")
                            reward += 30
                    
                    # Complete the quest
                    print(f"Quest completed! You earned {reward} gold!")
                    gold += reward
                    completed_quests.append(quest_name)
            
            if game_ended:
                break
            
            # Advance time after each shop visit -        advance_time .
            times = ["morning", "afternoon", "evening", "night"]
            current_index = times.index(time_of_day)
            time_of_day = times[(current_index + 1) % len(times)]
            
            # Randomly change weather
            if random.random() < 0.3:
                weather = random.choice(["clear", "cloudy", "rainy", "foggy"])
            
            # Show status after each shop visit
            print(f"\nGold: {gold} | Items: {len(cart)}")
            input("Press Enter to continue...")