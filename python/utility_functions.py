import pandas as pd

def prepare_df(data, coin_initials):

    prices = data["prices"]
    df = pd.DataFrame(prices, columns=["timestamp", "price"])
    df["date"] = pd.to_datetime(df["timestamp"], unit="ms")
    df["coin"] = f"{coin_initials}"
    df["daily_return"] = df["price"].pct_change() * 100
    df = df[["date", "coin", "price", "daily_return"]]

    return df

