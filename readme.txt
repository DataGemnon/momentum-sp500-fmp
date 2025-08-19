# Momentum Trading Strategy on S&P500 (FMP API)

## Objective
Backtest a simple momentum strategy (moving averages crossover) on the S&P500 using data from the Financial Modeling Prep API.

## Strategy
- Buy signal: 50-day SMA crosses above 200-day SMA
- Sell signal: 50-day SMA crosses below 200-day SMA
- Benchmark: Buy & Hold S&P500

## Tools
- Python (pandas, numpy, matplotlib, requests)
- FMP API for data

## Results
- Graph of cumulative returns (strategy vs buy & hold)
- Basic metrics: total return, Sharpe ratio, max drawdown

## Next steps
- Optimize SMA parameters
- Add transaction costs
- Test on different indices
