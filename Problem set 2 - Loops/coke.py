def main():
    buy_coke()


def equal(inserted):
    coins = [25, 10, 5]
    for coin in coins:
        if coin == inserted: 
            return True 


def buy_coke():
    amount_due = 50
    while 1 <= amount_due:
        print("\n"f"Amount due: {amount_due}")
        insert_coin = int(input("Insert coin: "))
        if equal(insert_coin):
            amount_due -= insert_coin
            if amount_due < 0:
                print("\n"f"Change owed: {-amount_due}")
    if amount_due == 0: print("\n"f"Amount due: {amount_due}")


if __name__ == "__main__":
    main()