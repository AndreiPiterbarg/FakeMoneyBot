
import pandas as pd

def read_data():
    df = pd.read_csv("data/BTC_historical.csv")

    # Use double brackets [[ ]] to keep it as a DataFrame instead of a Series
    df_real = df[["close","date"]]


    # Now the rename will work as expected
    df_real = df_real.rename(columns={"close": "Price"})
    return df_real


def split_data():
    df = read_data()
    #720*3 is three months
    chunk_size = 720 * 3
    num_chunks = len(df) // chunk_size
    dfs = []
    
    for i in range(num_chunks):
        start_idx = i * chunk_size
        end_idx = start_idx + chunk_size
        chunk = df.iloc[start_idx:end_idx].copy()
        dfs.append(chunk)

    return dfs

def df_start_end(chunk_num):
    start_end_list =[]
    chunk_size = 720*3

    start_index = chunk_size *(chunk_num)
    end_index = chunk_size * (chunk_num+1)
    df = read_data()
    start_date = df.iloc[start_index]["date"]
    end_date = df.iloc[end_index]["date"]
    start_end_list.append(start_date)
    start_end_list.append(end_date)

    return start_end_list


