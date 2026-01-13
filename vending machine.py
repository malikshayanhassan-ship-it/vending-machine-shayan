#shayan`s vending machine
#inventory setup
# key is the code, value is [name, price, quantity]
stock = {
    "A1": ["Chips", 1.50, 5],
    "B2": ["Biscuits", 2.00, 3], 
    "C3": ["Cola", 1.25, 10],
    "D4": ["Protein Bar", 5.00, 1],
    "E5": ["Milkshake", 1.00, 20],
    "F6": ["Orange Juice", 2.50, 8],
    "G7": ["Water Bottle", 1.00, 15],
    "H8": ["Salted Peanuts", 1.75, 6],
    "I9": ["Gummy Bears", 2.20, 12],
    "J10": ["Spicy Nachos", 1.80, 5],
    "K11": ["Energy Drink", 3.00, 10],
    "L12": ["Granola Bar", 1.50, 7],
    "M13": ["Chewing Gum", 0.75, 25],
    "N14": ["Iced Coffee", 3.50, 4],
    "O15": ["Cheese Stick", 0.80, 10],
    "P16": ["Fresh Banana", 1.00, 5],
    "Q17": ["Red Apple", 1.20, 5],
    "R18": ["Trail Mix", 2.75, 8],
    "S19": ["Beef Jerky", 4.50, 6],
    "T20": ["Popcorn", 2.00, 4], 
    "U21": ["Pretzels", 1.50, 8],
    "V22": ["Root Beer", 1.50, 12],
    "W23": ["Lemonade", 2.00, 9],
    "X24": ["Choco Milk", 2.50, 6],
    "Y25": ["Yogurt", 1.75, 4],
    "Z26": ["Noodles", 3.00, 10],
    "AA27": ["Spicy Fries", 1.90, 7],
    "BB28": ["Skittles", 1.60, 15],
    "CC29": ["M&Ms", 1.60, 15],
    "DD30": ["Sour Worms", 1.80, 10],
    "EE31": ["Peach Tea", 2.25, 8],
    "FF32": ["Cold Brew", 4.00, 5],
    "GG33": ["Coco Water", 3.50, 6],
    "HH34": ["Sandwich", 5.50, 3],
    "Z99": ["Mystery Bar", 0.50, 1] 
}

balance = 0.0
is_on = True #variable to control loop.

# Function to show the list
def print_menu():
    print("\n--- Shani`s Vending Machine ---")
    print(f"Current Money: ${balance:.2f}")
    print("-" * 30)
    
    # using for loop to print keys
    #sorted makes it look nicerrr
    for key in sorted(stock.keys()):
        val = stock[key]
        if val[2] > 0:
            print(f"[{key}] {val[0]:<15} - ${val[1]:.2f}")
        else:
            print(f"[{key}] {val[0]:<15} - SOLD OUT")
    print("-" * 30)
    print("Type 'Q' to quit | 'ADD' for cash")

print("Booting up system...")

# main loop starts here
while is_on:
    print_menu()
    
    # getting user input and removing spacess
    user_input = input("Enter selection: ").strip().upper()

    # if else block for options
    if user_input == 'Q':
        if balance > 0:
            print(f"Dispensing change: ${balance:.2f}")
        print("Cya later!")
        is_on = False #stop the loop
    
    elif user_input == 'ADD':
        # trial method for number error
        try:
            amt = float(input("Enter amount to insert: "))
            if amt <= 0:
                print("Amount must be positive.")
            else:
                balance = balance + amt # add to balence
        except ValueError:
            print("Error: That is not a valid number.")

    # HIDDEN ADMIN FEATURE 
    elif user_input == 'ADMIN':
        print("\n--- ADMIN DIAGNOSTICS ---")
        for key in stock:
            # trying to calculate price per unit
            try:
                per_unit = stock[key][1] / stock[key][2]
                print(f"{key}: ${per_unit:.2f} per unit")
            except ZeroDivisionError:
                # catches error if stock is 0
\            # update variables
            balance = balance - item_price
            stock[user_input][2] = stock[user_input][2] - 1
            
            if item_name == "Mystery Bar":
                print("Good luck with that one...")
    else:
        print("Invalid code.")
