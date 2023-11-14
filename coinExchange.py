"""LEARNING TASK GREEDY ALGORITHM - COIN EXCHANGE PROBLEM"""

"""Coin Exchange Problem"""

from pyfiglet import Figlet
def create_banner(text, font='small'):
    fig = Figlet(font=font)
    banner = fig.renderText(text)
    print(banner)

# Example usage
create_banner("Coin Exchange by Group 8")

# Define a function that takes two arguments the Coins and Exchange.
def coinExchange(coins, exchange):
    """
    coins - the coins available in cash register box
    exchange - the amount of change to be given to the customr
    """

    # Sort the coins in descending order. using the the sort() function and set the reverse to True.
    coins.sort(reverse=True)

    # Create an empty list to store the coins to be given to the customer.
    numCoins = []

    # Traverse the coins list using for loop.
    for coin in coins:

        # while the coin is less than or equal to the exchange.
        while coin <= exchange:

            # Subtract the coin from the exchange.
            exchange -= coin

            # Append the coin to the numCoins list. For every subtraction of coin from the exchange.
            numCoins.append(coin)
                            


    # print the coins to be given to the customer.
    print(f"{numCoins} = ₱{sum(numCoins):,}")

    # Create a variable to store the total number of coins. - initiakize it to 0
    coinsCount = 0

    # Traversing the Coins list to be given to the customer    
    while len(numCoins) > 0:

        # Get the maximum coin from the numCoins list.
        maxCoin = max(numCoins)

        # Then print the number of coins to be given to the customer. and specify the count of the coin
        print(f"\n{numCoins.count(maxCoin)} x ₱{maxCoin:,} = ₱{numCoins.count(maxCoin) * maxCoin:,}")

        # add the counted coin to the coinsCount variable.
        coinsCount += numCoins.count(maxCoin)

        # Remove the counted coin from the numCoins list. using the filter() function and lambda function.
        numCoins = list(filter(lambda x: x != maxCoin, numCoins))

    # Print the total number of coins to be given to the customer.
    print(f"\nTotal number of coins: {coinsCount}")

# MAIN FUNCTION
def main():

    # Create a list of coins available in the cash register box "THIS CAN BE IN ANY ORDER".
    coins = [0.05, 0.10, 0.25, 1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]

    # creat a loop to get the amount to be paid and the payment from the customer.
    while 1:
        try:
            # Use float to get the customer input in case of the decimal numbers
            amount = float(input("\nEnter the price to pay: "))
            payment = float(input("Enter your payment: "))

            # check if the payment is less than the amount to be paid. and return to loop to get the exact payment
            if payment < amount:
                print("\nInsufficient payment. Please try again.")
                continue
            # break the loop if the payment is valid
            break

        # Raise an exception if the input is not float or integer
        except ValueError:
            print("\nInvalid input. Please enter a valid input.")

    # Get the exchange by subtracting the payment to the total amount to pay
    exchange = payment - amount

    # print the exchange of the customer
    print(f"\nYour change is: {exchange}")

    # after getting all the input run the coinExchange function
    coinExchange(coins, exchange)

# Run the main() funtion to start the program
if __name__ == "__main__":
    main()


    