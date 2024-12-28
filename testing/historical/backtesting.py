import os
import sys

def backtest():

    # Add the project root (DIYBot) to the Python path
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    sys.path.append(project_root)

    import pandas as pd
    from testing.historical import data_loader
    from strategies import momentum


    dfs = data_loader.split_data()
    print(len(dfs))

    # Run strategy on each chunk
    trades_list = []
    for i in range(len(dfs)):
        print(f"\nProcessing chunk {i+1}/{len(dfs)}")
        trade_df = momentum.run_momentum_strategy(dfs[i])
        trades_list.append(trade_df)

    return trades_list


