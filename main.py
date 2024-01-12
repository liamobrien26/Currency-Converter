import os

exchangeRates = {"American Dollars (USD)": 1.40, "Euros (EUR)": 1.14, "Brazilian Real (BRL)": 4.77,
                 "Japanese Yen (JPY)": 151.05, "Turkish Lira (TRL)": 5.68}


def CurrencyOption():
    print("-----Welcome to Tesco Currency Converter-----")
    choice = int(input("""\nWhich 'Currency' does the customer wishes to exchange into? \n
            1. American Dollars (USD)
            2. Euros (EUR)
            3. Brazilian Real (BRL)
            4. Japanese Yen (JPY)
            5. Turkish Lira (TRL)
            
            Option:"""))
    os.system('clear')
    return choice


def CustomerDeposit():
    while True:
        deposit_amount = round(
            float(input("Please enter deposit amount you wish to convert into your choice of currency: \n£")), 2)
        if deposit_amount <= 2500:
            os.system('clear')
            return deposit_amount
        else:
            print("Transaction limit exceeded. Please enter an amount equal to or less than £2500.")
            os.system('clear')



def calculate_transaction_fee(deposit_amount):
    if deposit_amount <= 299.99:
        fee_rate = 0.035  # 3.5%
    elif 300 <= deposit_amount <= 749.99:
        fee_rate = 0.03  # 3%
    elif 750 <= deposit_amount <= 999.99:
        fee_rate = 0.025  # 2.5%
    elif 1000 <= deposit_amount <= 1999.99:
        fee_rate = 0.02  # 2%
    else:
        fee_rate = 0.015  # 1.5%

    transaction_fee = deposit_amount * fee_rate
    return transaction_fee


def Calculating(choice, deposit_amount, exchangeRates, transaction_fee):
    if choice == 1:
        usd = exchangeRates.get("American Dollars (USD)") * deposit_amount
        print("-----INVOICE-----")
        print("Deposit amount: £", deposit_amount)
        print("Currency choice: AMERICAN DOLLARS")
        print(f"Converted amount: {usd} USD")
        print("Transaction fee: £", round(transaction_fee, 2))
        print("TOTAL AMOUNT TO PAY: £", transaction_fee + deposit_amount)



    elif choice == 2:
        eur = exchangeRates.get("Euros (EUR)") * deposit_amount
        print("-----INVOICE-----")
        print("Deposit amount: £", deposit_amount)
        print("Currency choice: EUROS")
        print(f"Converted amount: {eur} EUR")
        print("Transaction fee: £", round(transaction_fee, 2))
        print("TOTAL AMOUNT TO PAY: £", transaction_fee + deposit_amount)



    elif choice == 3:
        brl = exchangeRates.get("Brazilian Real (BRL)") * deposit_amount
        print("-----INVOICE-----")
        print("Deposit amount: £", deposit_amount)
        print("Currency choice: BRAZILIAN REAL")
        print(f"Converted amount: {brl} BRL")
        print("Transaction fee: £", round(transaction_fee, 2))
        print("TOTAL AMOUNT TO PAY: £", transaction_fee + deposit_amount)


    elif choice == 4:
        jpy = exchangeRates.get("Japanese Yen (JPY)") * deposit_amount
        print("-----INVOICE-----")
        print("Deposit amount: £", deposit_amount)
        print("Currency choice: JAPANESE YEN")
        print(f"Converted amount: {jpy} JPY")
        print("Transaction fee: £", round(transaction_fee, 2))
        print("TOTAL AMOUNT TO PAY: £", transaction_fee + deposit_amount)



    elif choice == 5:
        trl = exchangeRates.get("Turkish Lira (TRL)") * deposit_amount
        print("-----INVOICE-----")
        print("Deposit amount: £", deposit_amount)
        print("Currency choice: TURKISH LIRA")
        print(f"Converted amount: {trl} TRL")
        print("Transaction fee: £", round(transaction_fee, 2))
        print("TOTAL AMOUNT TO PAY: £", transaction_fee + deposit_amount)


    else:
        print("Invalid choice")


# Main program
choice = CurrencyOption()
deposit_amount = CustomerDeposit()
transaction_fee = calculate_transaction_fee(deposit_amount)
Calculating(choice, deposit_amount, exchangeRates, transaction_fee)
