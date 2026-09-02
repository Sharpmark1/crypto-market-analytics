-- KPI View

CREATE OR REPLACE VIEW coin_kpis AS
SELECT
    coin,
    ROUND(AVG(price), 2) AS average_price,
    ROUND(MAX(price), 2) AS highest_price,
    ROUND(MIN(price), 2) AS lowest_price,
    ROUND(AVG(daily_return), 2) AS avg_return,
    ROUND(STDDEV(daily_return), 2) AS volatility
FROM market_prices
WHERE daily_return IS NOT NULL
GROUP BY coin;
