from database import connect_db
import pandas as pd
from utility_functions import prepare_df
from historical import get_coin_history



btc_data = get_coin_history("bitcoin")
sol_data = get_coin_history("solana")
eth_data = get_coin_history("ethereum")

btc_df = prepare_df(btc_data, "BTC")
eth_df = prepare_df(eth_data, "ETH")
sol_df = prepare_df(sol_data, "SOL")


market_df = pd.concat([btc_df, eth_df, sol_df], ignore_index=True)
market_df["daily_return"] = (
    market_df["daily_return"]
    .astype(object)
    .where(market_df["daily_return"].notna(), None)
)

conn = connect_db()
cursor = conn.cursor()

for _, row in market_df.iterrows():

    cursor.execute(
        """
        INSERT INTO market_prices
        (trade_date, coin, price, daily_return)
        VALUES (%s, %s, %s, %s)
        ON CONFLICT (trade_date, coin)
        DO NOTHING;
        """,
        (
            row["date"],
            row["coin"],
            row["price"],
            row["daily_return"]
        )
    )

conn.commit()

cursor.close()
conn.close()

print("Data loaded successfully!")
