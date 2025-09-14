# Function to ask the user for number of tickets
def get_ticket_request():
    while True:
        try:
            num = int(input("What is the amount of tickets being purchased? "))
            if 1 <= num <= 4:
                return num
            else:
                print("Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Function to handle the ticket sale
def sell_tickets():
    tickets_left = 10
    buyers = 0

    while tickets_left > 0:
        print(f"\nTickets remaining: {tickets_left}")
        requested = get_ticket_request()

        if requested <= tickets_left:
            tickets_left -= requested
            buyers += 1
            print(f"You bought {requested} ticket(s). {tickets_left} remaining.")
        else:
            print(f"Only {tickets_left} tickets left. You can't buy {requested}.")

    print(f"\nAll tickets sold. Total buyers: {buyers}")

# Run the ticket selling process
sell_tickets()



