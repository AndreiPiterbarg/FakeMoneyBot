import pandas as pd
def run_momentum_strategy(df1):
    """Grab the latest data from data_store and run momentum logic."""
    global has_position
    has_position = False
    df = df1.copy()
    
    # Initialize DataFrame with correct dtypes
    df_trades = pd.DataFrame({
        "Decision": pd.Series(dtype='str'),
        "Price": pd.Series(dtype='float64'),
        "Amount_Dollars": pd.Series(dtype='float64'),
        "Amount": pd.Series(dtype='float64'),
    })
    # Calculate indicators once outside the loop
    df["EMA12"] = df["Price"].ewm(span=12, adjust=False).mean()
    df["EMA26"] = df["Price"].ewm(span=26, adjust=False).mean()
    df['MACD'] = df['EMA12'] - df['EMA26']
    df['Signal_Line'] = df['MACD'].ewm(span=9, adjust=False).mean()
    
    money = 100.0
    amount = 0.0

    for i in range(1, len(df)):
        current_row = df.iloc[i]
        previous_row = df.iloc[i-1]
        price = current_row["Price"]

        if (previous_row['MACD'] > previous_row['Signal_Line'] and 
            current_row['MACD'] < current_row['Signal_Line'] and 
            not has_position):
            
            amount = money / price
            new_row = pd.DataFrame({
                "Decision": ["BUY"],
                "Price": [price],
                "Amount_Dollars": [money],
                "Amount": [amount],
            })
            df_trades = pd.concat([df_trades, new_row], ignore_index=True)
            has_position = True
            
        elif (previous_row['MACD'] < previous_row['Signal_Line'] and 
              current_row['MACD'] > current_row['Signal_Line'] and 
              has_position):
              
            money = amount * price
            amount = 0.0
            new_row = pd.DataFrame({
                "Decision": ["SELL"],
                "Price": [price],
                "Amount_Dollars": [money],
                "Amount": [amount]
            })
            df_trades = pd.concat([df_trades, new_row], ignore_index=True)
            has_position = False

    
    return df_trades