# Quant-Projects
Quantitative Finance - Projects, Algorithms, Ideas etc.
## Introduction
This repository consist a few things. Firstly, the Intro to Quant module. The world of finance is quite sectretive, with the vast majority of projects online having either results that are statistically garbage or using outdated models, namely econometrics, I try to give my perspective of how to create models as well as educating in time series analysis.  Secondly, my old projects. These are quite sporadic projects that were done in the beginning of our quantitative finance journey. The backtesting is below the bar, but they show the development process during the years and highlight potential pitfalls. I will probably annotate them better in due time. 

### Table of Contents

&nbsp;

#### Old Quant Projects

* <a href=https://github.com/JonssonAlexander/Quant-Projects/blob/main/Quant%20Projects/Old%20Projects/First_project_MA_momentum_updated.ipynb>Momentum MA Strategy</a>
* <a href=https://github.com/JonssonAlexander/Quant-Projects/blob/main/Quant%20Projects/Old%20Projects/Project_2_MACD_and_portfolio_check_updated.ipynb> MACD and Portfolio Check</a>
* <a href=https://github.com/JonssonAlexander/Quant-Projects/blob/main/Quant%20Projects/Old%20Projects/Project_3_Modified_Momentum_MA_updated.ipynb>Modified Momentum MA Strategy</a>
* <a href=https://github.com/JonssonAlexander/Quant-Projects/blob/main/Quant%20Projects/Old%20Projects/Project_4_Volume_Strategy_updated.ipynb> Volume Strategy</a>
* <a href=https://github.com/JonssonAlexander/Quant-Projects/blob/main/Quant%20Projects/Old%20Projects/Review_of_Stop_loss_and_draw_down_updated.ipynb> Stop Loss and Drawdown</a>
* <a href=https://github.com/JonssonAlexander/Quant-Projects/blob/main/Quant%20Projects/Old%20Projects/Smoothing_With_Butterworth_Filter_updated.ipynb> Smoothing With Butterworth Filter</a>

#### Intro To Quant 
* <a href=https://github.com/JonssonAlexander/Quant-Projects/blob/main/IntroToQuant_Part1.ipynb/>Part 1</a>
* <a href=https://github.com/>Part 2</a>

## Strategies:

### 1. Momentum Moving Average
My friend, later to be business partner, and I had just started univeristy and had spent a couple of days researching at the univiersity library for a strategy and gotten familiar with the relevant python libraries. We saw an interesting article about how one could see different intervals for MAs (moving averages) as velocity and acceleration and that the results through a backtest showed 12000% gain over the last year. (Yes, in heinsight we should have been more sceptical.) Nontheless, using the concept, we developed a strategy based on this where if the shortest interval MA (acceleration) was higher than the middle MA (velocity) and that in turn was higher than a benchmark MA, we would buy.

Being new to the subject, the code below is extremely slow and has a couple of fundamental flaws, but the idea is still there and the code is quite intuitive to read.


### 2. MACD oscillator (taken from JSTM)

MACD oscillator is trading strategy 101. MACD refers to Moving Average Convergence/Divergence. It is a momentum trading strategy which holds the belief that upward/downward momentum has more impact on short term moving average than long term moving average. It only takes 5 minutes for any bloke with no background in finance to trade with MACD signals. Regarding the simplicity of MACD oscillator, it is the most common strategy among the non-professionals in the market. In behavioral economics, the more people believe in the strategy, the more effective the strategy becomes (not always true, e.g. 2008). Therefore, we should not underestimate the power of MACD oscillator.

For the strategy itself, we compute long term moving average and short term moving average on the close price of a given stock. To generate the trading signal, we implement a comparison between the moving averages of different time horizons. When short term moving average is above long term moving average, we long the given stock accordingly. Vice versa.

