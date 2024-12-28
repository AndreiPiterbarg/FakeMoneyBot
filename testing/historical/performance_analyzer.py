import backtesting
import data_loader
import pandas as pd

trades_list = backtesting.backtest()

for i in range(len(trades_list)):

    start_end_list = data_loader.df_start_end(i)
    start_date = pd.to_datetime(start_end_list[0]) 
    end_date = pd.to_datetime(start_end_list [1])
    num_days = (start_date - end_date).days







    print(f"""
    Period {i+1} Analysis
    --------------------------------------------------
    Date Range: {start_date} to {end_date} ({num_days} days)
    --------------------------------------------------
    Equity:
    Start: ${100.00}

    
    """)
    """
    #print(

    Final: ${final_equity:.2f}
    Peak:  ${peak_equity:.2f}
    Return: {return_pct:.2f}%

    Trading Activity:
    Total Trades: {num_trades}
    Best Trade:  ${best_trade:.2f}
    Worst Trade: ${worst_trade:.2f}
    Avg Trade:   ${avg_trade:.2f}

    Risk Metrics:
    
    
    Volatility:   ${volatility:.2f}
    Max Drawdown: ${max_drawdown:.2f}
    --------------------------------------------------
    )"""
    
def final_money(df):
    size = len(df)    
    if(size==0):
        return 100

    last_row = df.
    return 