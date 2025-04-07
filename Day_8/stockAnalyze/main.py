from stock import analyze_stock

if __name__=="__main__":
    prices=[]

    print("Enter stock prices for last 7 days:")
    for i in range(7):
        price=float(input(f"day{i+1} price: "))
        prices.append(price)

    signal=analyze_stock(prices)
    print(f"You should {signal} this stock")    