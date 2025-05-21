from sources import resources, MENU


coffer_money = {"quarter": 0, "dime": 0, "nickel": 0, "penny": 0}


def calculate_total_money(coffer):
    total = (coffer["quarter"] * .25) + (coffer["dime"] * .10) + (coffer["nickel"] * .05) + (coffer["penny"] * .01)
    return total


def reduce_resources(choice, avail_resource):
    edited_resource = avail_resource
    for resource in avail_resource:
        for ingredients in MENU[choice]["ingredients"]:
            if ingredients == resource:
                edited_resource[resource] = avail_resource[ingredients] - MENU[choice]["ingredients"][ingredients]
    return edited_resource


# TODO: 2. Check if the resources are sufficient


def check_resource(choice, avail_resource):
    lacking = discrepancy

    for resource in avail_resource:
        for ingredients in MENU[choice]["ingredients"]:
            if MENU[choice]["ingredients"][ingredients] > avail_resource[ingredients]:
                lacking.add(ingredients)

            elif lacking == set():
                lacking.add("none")
    return lacking


def check_coins(choice):
    inserted_coins = {"quarter": 0, "dime": 0, "nickel": 0, "penny": 0}
    print("Please insert coins")
    for key in inserted_coins:
        inserted_coins[key] = int(input(f"How many {key}: "))
    total_inserted = calculate_total_money(inserted_coins)
    print(f"Total: ${total_inserted}")
    if MENU[choice]["cost"] > total_inserted:
        return {"quarter": 0, "dime": 0, "nickel": 0, "penny": 0}
    else:
        return inserted_coins


def calculate_change(total_change):
    temp_change = total_change
    reduce_by = 0
    for coin_type in coffer_money:
        if coffer_money[coin_type] == 0:
            continue
        else:
            if coin_type == "quarter":
                reduce_by = .25
            elif coin_type == "dime":
                reduce_by = .10
            elif coin_type == "nickel":
                reduce_by = .05
            elif coin_type == "penny":
                reduce_by = .01
            while temp_change >= 0.0:
                temp_change -= reduce_by
                coffer_money[coin_type] -= 1

    print(f"Your change: {change}")


total_money = calculate_total_money(coffer_money)

# TODO: 1. Print choices and add an option for report to print all resources
is_off = False
discrepancy = set()
while not is_off:
    print("Welcome to the digital coffee machine!")
    user_choice = input("What would you like? (espresso/latte/cappuccino):")
    if user_choice == "report":
        print(f"resources: {resources}\nMoney: ${coffer_money}")
    elif user_choice == "off":
        is_off = True
    elif user_choice in MENU:
        discrepancy.clear()
        discrepancy = check_resource(user_choice, resources)
        print(discrepancy)
        if "none" in discrepancy:
            # TODO: 3. Process coins
            insert_again = True
            while insert_again:
                coin_result = check_coins(user_choice)
                total_coin_result = calculate_total_money(coin_result)
                # TODO: 4. Check if the transaction is successful?
                if total_coin_result == 0:
                    print("Not Enough Coins, Refunded")
                else:
                    # TODO: 5. If successful 'make' coffee and give change and repeat
                    for item in coffer_money:
                        coffer_money[item] += coin_result[item]  # Adds inserted money to the coffer if successful
                    change = round(total_coin_result - MENU[user_choice]["cost"], 2)
                    if change != 0:
                        calculate_change(change)
                    else:
                        print(f"Your paid the exact amount of ${total_coin_result}")
                        print(coffer_money)
                    # TODO: 5. If successful 'make' coffee and give change and repeat
                    resources = reduce_resources(user_choice,
                                                 resources)  # REDUCE RESOURCES AFTER SUCCESSFUL TRANSACTION
                    insert_again = False
            print(f"\n**Enjoy your {user_choice}**\n")
        else:
            for item in discrepancy:
                print(f"Not Enough {item}")


# TODO: 5. If successful 'make' coffee and give change and repeat
