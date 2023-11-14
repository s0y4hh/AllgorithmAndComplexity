def coinExchange(coins, amount):
    coins.sort(reverse=True)
    numCoins = []
    for coin in coins:
        while coin <= amount:
            amount -= coin
            numCoins.append(coin)
    coinsCount = 0
    print(f"{numCoins} = {sum(numCoins):,}")
    while len(numCoins) > 0:
        maxCoin = max(numCoins)

        print(f"\n{numCoins.count(maxCoin)} x ₱{maxCoin:,} = ₱{numCoins.count(maxCoin) * maxCoin:,}")
        coinsCount += numCoins.count(maxCoin)

        numCoins = list(filter(lambda x: x != maxCoin, numCoins))

    print(f"\nTotal number of coins: {coinsCount}")

def main():
    coins = [0.05, 0.10, 0.25, 1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]
    while 1:
        try:
            amount = float(input("\nEnter the price to pay: "))
            payment = float(input("Enter your payment: "))
            if payment < amount:
                print("\nInsufficient payment. Please try again.")
                continue
            break
        except ValueError:
            print("\nInvalid input. Please enter an integer.")
    exchange = payment - amount
    print(f"\nYour change is: {exchange}")
    coinExchange(coins, exchange)

if __name__ == "__main__":
    main()


    