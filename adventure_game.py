import time
import random

inventory = []
money = 1000
clock = 1


def print_pause(string):
    print(string)
    time.sleep(2)


def intro():
    print_pause("You're trying to earn enough money to buy a sword!")
    print_pause("In order to save your hometown from a dragon, you have "
                "travelled to a mytstical city.")
    print_pause("The goal is at least $10,000 by 7:00 PM! You look "
                "inside your wallet...")


def back_to_plaza():
    print_pause("Back to the plaza it is!")
    plaza()


def plaza():
    if "enchanted sword" in inventory:
        print_pause("You have all you need to defeat the dragon!")
        hometown()
    elif clock == 8:
        print_pause("You head back to the plaza and look at the clock.")
        print_pause(f"You realize it is already {clock}:00 PM.")
        print_pause("Unfortunately, it is too late to save your "
                    "hometown now...")
    else:
        print_pause(f"Looks like you have ${money}, and it is currently "
                    f"{clock}:00 PM. Where should you go?")
        location = input("1. Back to hometown \n"
                         "2. Gamblers Hall \n"
                         "3. Look for work \n"
                         "4. Blacksmith \n")
        if location == "1":
            hometown()
        elif location == "2":
            gamblers_hall()
        elif location == "3":
            work()
        elif location == "4":
            blacksmith()
        else:
            print_pause("Please enter a valid response.")
            plaza()


def hometown():
    print_pause("Once you head back to hometown, there is no turning back.")
    choice = input("Would you like to proceed? y/n \n").lower()
    if choice == 'y':
        if "enchanted sword" in inventory:
            print_pause("With the enchanted sword in hand, you head "
                        "back home.")
            print_pause("You encounter the dragon and defeat "
                        "it with one slash!")
            print_pause("Congratulations! You have saved your hometown!")
        elif "sword" in inventory:
            print_pause("Hoping to defeat the dragon with the sword, you "
                        "head back home.")
            print_pause("With the sword in hand, you fight the dragon!")
            print_pause("Looks like this battle can go either way...")
            chances = random.randint(0, 1)
            if chances == 0:
                print_pause("Unfortunately, the dragon has bested you and "
                            "your hometown has been destroyed...")
            if chances == 1:
                print_pause("You defeated the dragon and saved your hometown!")
        elif "enchanted sword" and "sword" not in inventory:
            print_pause("You're going back home empty handed!")
            print_pause("You knew this was coming. The dragon swiped you "
                        "away and destroyed your hometown...")
    elif choice == 'n':
        back_to_plaza()
    else:
        print_pause("Please enter a valid input.")
        hometown()


def gamblers_hall():
    global money
    global clock
    if "gamblers luck" not in inventory:
        print_pause("You enter the gamblers hall in hopes to earn fast money!")
        choice = input("You can only enter once today. Would you like to "
                       "proceed? y/n \n").lower()
        if choice == 'y':
            print_pause("You sit down at the table.")
            bet = int(input("How much money would you like to bet?\n"))
            if bet > money:
                print_pause("You don't have enough money for that, "
                            "you know...")
                plaza()
            else:
                print_pause(f"You put in ${bet}.")
                gamble = random.randint(0, 3)
                outcome = bet * gamble
                if gamble == 0:
                    print_pause("Sorry, you've lost your bet...")
                    money -= bet
                elif gamble == 1:
                    print_pause("You haven't won anything, but you didn't "
                                "lose anything either! So that's good.")
                elif gamble == 2 or gamble == 3:
                    print_pause(f"You've won! You recieved ${outcome}.")
                    money += outcome
            inventory.append("gamblers luck")
            clock += 1
            plaza()

        if choice == 'n':
            back_to_plaza()

        else:
            print_pause("Please enter a valid input.")
            gamblers_hall()
    else:
        print_pause("You've already tested your luck! Sorry...")
        plaza()


def work():
    earnings = [500, 1000, 2000, 3000]
    global money
    global clock
    print_pause("You look for a steady way to increase your money.")
    print_pause("Seems like there are some people around who need help!")
    job = random.choice(earnings)
    print_pause(f"You've earned ${job}!")
    money += job
    clock += 1
    plaza()


def blacksmith():
    global money
    global clock
    print_pause("You head over to the blacksmith.")
    if money >= 10000 and "sword" not in inventory:
        decision = input("Looks like you can buy yourself a sword! Would you "
                         "like to purchase it now? y/n \n").lower()
        if decision == 'y':
            inventory.append("sword")
            money -= 10000
            print_pause("You bought yourself a sword!!")
            print_pause("Seems like you can come back next time and enchant "
                        "your sword for another $10,000.")
            plaza()
        elif decision == 'n':
            back_to_plaza()
        else:
            print_pause("Please enter a valid response.")
            blacksmith()
    elif money >= 10000 and "sword" in inventory:
        if clock == 7:
            print_pause("Unfortunately, it is too late to enchant.")
            plaza()
        else:
            enchant = input("You can enchant your sword! Would you like to "
                            "enchant? It will take about an hour. "
                            "y/n \n").lower()
            if enchant == 'y':
                inventory.append("enchanted sword")
                clock += 1
                money -= 10000
                plaza()
            elif enchant == 'n':
                back_to_plaza()
            else:
                print_pause("Please enter a valid response.")
                blacksmith()
    else:
        print_pause("You don't have enough money! You need at least "
                    "$10,000.")
        plaza()


def replay():
    global money
    global clock
    game = input("Would you like to play again? y/n \n").lower()
    if game == 'y':
        money = 1000
        clock = 1
        play_game()
    elif game == 'n':
        print_pause("Thank you for playing!!")
    else:
        print_pause("Please enter a valid response.")
        replay()


def play_game():
    intro()
    plaza()
    replay()


play_game()
