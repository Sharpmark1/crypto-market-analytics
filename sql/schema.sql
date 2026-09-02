-- Create market_prices table

CREATE TABLE market_prices (
    id SERIAL PRIMARY KEY,
    trade_date DATE NOT NULL,
    coin VARCHAR(10) NOT NULL,
    price NUMERIC(12,2) NOT NULL,
    daily_return NUMERIC(8,4)
);

ALTER TABLE market_prices
ADD CONSTRAINT unique_coin_date
UNIQUE (trade_date, coin);
