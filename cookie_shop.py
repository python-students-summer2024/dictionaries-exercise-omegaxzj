import csv


def bake_cookies(filepath='data/cookies.csv'):
    cookies = []
    with open(filepath, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            row['sugar_free'] = row['sugar_free'].lower() in ['true', 'yes', '1']
            row['gluten_free'] = row['gluten_free'].lower() in ['true', 'yes', '1']
            row['contains_nuts'] = row['contains_nuts'].lower() in ['true', 'yes', '1']
            cookies.append(row)
    return cookies


def welcome():
    print("Welcome to the Python Cookie Shop!")
    print("We feed each according to their need.")
    dietary_prefs = {}
    dietary_prefs['nuts'] = input("Are you allergic to nuts? (yes/no) ").lower() in ['yes', 'y']
    dietary_prefs['gluten'] = input("Are you allergic to gluten? (yes/no) ").lower() in ['yes', 'y']
    dietary_prefs['sugar'] = input("Do you suffer from diabetes? (yes/no) ").lower() in ['yes', 'y']
    return dietary_prefs


def display_cookies(cookies, dietary_prefs):
    print("Here are the cookies we have in the shop for you:\n")
    for cookie in cookies:
        if (dietary_prefs['nuts'] and not cookie['contains_nuts']) or \
                (dietary_prefs['gluten'] and not cookie['gluten_free']) or \
                (dietary_prefs['sugar'] and cookie['sugar_free']):
            print(f"#{cookie['id']} - {cookie['title']}")
            print(f"{cookie['description']}")
            print(f"Price: ${cookie['price']:.2f}\n")


def solicit_order(cookies):
    orders = []
    while True:
        user_input = input(
            "Please enter the number of any cookie you would like to purchase (type 'finished' to complete): ")
        if user_input.lower() in ['finished', 'done', 'quit', 'exit']:
            break
        try:
            cookie_id = int(user_input)
            quantity = int(input(f"How many of cookie #{cookie_id} would you like? "))
            orders.append({'id': cookie_id, 'quantity': quantity})
        except ValueError:
            print("Invalid input, please enter valid numbers.")
    return orders


def display_order_total(order, cookies):
    print("\nThank you for your order. You have ordered:\n")
    total = 0.0
    for item in order:
        for cookie in cookies:
            if cookie['id'] == item['id']:
                subtotal = item['quantity'] * cookie['price']
                print(f"- {item['quantity']} {cookie['title']} at ${cookie['price']:.2f} each: ${subtotal:.2f}")
                total += subtotal
                break
    print(f"\nYour total is: ${total:.2f}")
    print("Please pay with Bitcoin before picking-up.\nThank you!\n-The Python Cookie Shop Robot.")


def run_shop():
    cookies = bake_cookies()
    dietary_prefs = welcome()
    display_cookies(cookies, dietary_prefs)
    order = solicit_order(cookies)
    display_order_total(order, cookies)
