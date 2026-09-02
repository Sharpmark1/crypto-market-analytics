-- Total records
SELECT COUNT(*) AS total_records
FROM market_prices;

-- Average price by coin
SELECT
    coin,
    ROUND(AVG(price), 2) AS average_price
FROM market_prices
GROUP BY coin
ORDER BY average_price DESC;

-- Average daily return
SELECT
    coin,
    ROUND(AVG(daily_return), 2) AS avg_daily_return
FROM market_prices
WHERE daily_return IS NOT NULL
GROUP BY coin
ORDER BY avg_daily_return DESC;

-- Volatility
SELECT
    coin,
    ROUND(STDDEV(daily_return), 2) AS volatility
FROM market_prices
WHERE daily_return IS NOT NULL
GROUP BY coin
ORDER BY volatility DESC;

-- Highest closing price
SELECT
    coin,
    ROUND(MAX(price), 2) AS highest_price
FROM market_prices
GROUP BY coin;

-- Top 5 daily gains
SELECT
    trade_date,
    coin,
    ROUND(daily_return, 2) AS gain
FROM market_prices
WHERE daily_return IS NOT NULL
ORDER BY daily_return DESC
LIMIT 5;
