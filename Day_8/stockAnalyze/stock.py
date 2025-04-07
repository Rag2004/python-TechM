def analyze_stock(prices):
    if len(prices)<3:
        return "Not enough data to analyze"
    
    last_3=prices[-3:]

    if last_3[0]<last_3[1]<last_3[2]:
       return "Buy"
    elif last_3[0]>last_3[1]>last_3[2]:
        return "Sell"
    else:
        return "Hold"

