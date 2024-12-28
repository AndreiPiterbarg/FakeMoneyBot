import pandas as pd

# Module-level DataFrame, initially empty
df_prices = pd.DataFrame(columns=["Price"])

def append_price(price: float):
    """Append a new price to the shared DataFrame."""
    global df_prices
    df_prices.loc[len(df_prices)] = [price]

def get_data():
    """Return the entire DataFrame of prices."""
    return df_prices
