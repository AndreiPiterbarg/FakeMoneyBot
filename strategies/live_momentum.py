
from testing.live.data_store import get_data
import trade_storage.trade_logger
import pandas as pd
from config import GlobalVars
import testing.live.data_collector

has_position = False

def run_momentum_strategy():
    """Grab the latest data from data_store and run momentum logic."""
    # Make a copy to avoid adding columns to the global df_prices
    global has_position
    df = get_data().copy()

    if len(df) < 26:
        print("Not enough data yet.")
        return

    df["EMA12"] = df["Price"].ewm(span=12, adjust=False).mean()
    df["EMA26"] = df["Price"].ewm(span=26, adjust=False).mean()
    df['MACD'] = df['EMA12'] - df['EMA26']
    df['Signal_Line'] = df['MACD'].ewm(span=9, adjust=False).mean()

    last_row = df.iloc[-1]
    second_last_row = df.iloc[-2]

    if second_last_row['MACD'] > second_last_row['Signal_Line'] and last_row['MACD'] < last_row['Signal_Line'] and not has_position:
        curr_price = float(testing.data_collector.get_BTC_price_amount())
        curr_money=GlobalVars.balance
        GlobalVars.curr_amt =  curr_money/curr_price
        trade_storage.trade_logger.buy(curr_price,curr_money, GlobalVars.curr_amt )
        has_position = True
        print('BUY BUY BUY')
    elif second_last_row['MACD'] < second_last_row['Signal_Line'] and last_row['MACD'] > last_row['Signal_Line'] and has_position:
        curr_price = float(testing.data_collector.get_BTC_price_amount())
        GlobalVars.balance = curr_price * GlobalVars.curr_amt
        curr_money=GlobalVars.balance

        GlobalVars.curr_amt =0

        trade_storage.trade_logger.sell(curr_price, curr_money, GlobalVars.curr_amt)
        has_position = False
        print('SELL SELL SELL')
    else:
        trade_storage.trade_logger.nothing()
        print("DO NADA")
