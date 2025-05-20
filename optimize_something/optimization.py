""""""
"""MC1-P2: Optimize a portfolio.  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
Copyright 2018, Georgia Institute of Technology (Georgia Tech)  		  	   		 	   			  		 			 	 	 		 		 	
Atlanta, Georgia 30332  		  	   		 	   			  		 			 	 	 		 		 	
All Rights Reserved  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
Template code for CS 4646/7646  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
Georgia Tech asserts copyright ownership of this template and all derivative  		  	   		 	   			  		 			 	 	 		 		 	
works, including solutions to the projects assigned in this course. Students  		  	   		 	   			  		 			 	 	 		 		 	
and other users of this template code are advised not to share it with others  		  	   		 	   			  		 			 	 	 		 		 	
or to make it available on publicly viewable websites including repositories  		  	   		 	   			  		 			 	 	 		 		 	
such as github and gitlab.  This copyright statement should not be removed  		  	   		 	   			  		 			 	 	 		 		 	
or edited.  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
We do grant permission to share solutions privately with non-students such  		  	   		 	   			  		 			 	 	 		 		 	
as potential employers. However, sharing with other current or future  		  	   		 	   			  		 			 	 	 		 		 	
students of CS 7646 is prohibited and subject to being investigated as a  		  	   		 	   			  		 			 	 	 		 		 	
GT honor code violation.  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
-----do not edit anything above this line---  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
Student Name: xxx  	   		 	   			  		 			 	 	 		 		 	
User ID: xxx		  	   		 	   			  		 			 	 	 		 		 	
ID: xxx 		  	   		 	   			  		 			 	 	 		 		 	
"""

import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from util import get_data, plot_data
import scipy.optimize as spo

def author():
    """
    :return: The username of the student
    :rtype: str
    """
    return "xxx"

def study_group():
    return "xxx"

# This is the function that will be tested by the autograder
# The student must update this code to properly implement the functionality
def optimize_portfolio(
        sd=dt.datetime(2008, 6, 1),
        ed=dt.datetime(2009, 6, 1),
        syms=["IBM", "X", "GLD", "JPM"],
        gen_plot=True,
):
    """
    This function should find the optimal allocations for a given set of stocks. You should optimize for maximum Sharpe
    Ratio. The function should accept as input a list of symbols as well as start and end dates and return a list of
    floats (as a one-dimensional numpy array) that represents the allocations to each of the equities. You can take
    advantage of routines developed in the optional assess portfolio project to compute daily portfolio value and
    statistics.

    :param sd: A datetime object that represents the start date, defaults to 1/1/2008
    :type sd: datetime
    :param ed: A datetime object that represents the end date, defaults to 1/1/2009
    :type ed: datetime
    :param syms: A list of symbols that make up the portfolio (note that your code should support any
        symbol in the data directory)
    :type syms: list
    :param gen_plot: If True, optionally create a plot named plot.png. The autograder will always call your
        code with gen_plot = False.
    :type gen_plot: bool
    :return: A tuple containing the portfolio allocations, cumulative return, average daily returns,
        standard deviation of daily returns, and Sharpe ratio
    :rtype: tuple
    """

    # Read in adjusted closing prices for given symbols, date range
    dates = pd.date_range(sd, ed)
    prices_all = get_data(syms, dates)  # automatically adds SPY
    prices = prices_all[syms]  # only portfolio symbols
    prices_SPY = prices_all["SPY"]  # only SPY, for comparison later
    # find the allocations for the optimal portfolio
    # note that the values here ARE NOT meant to be correct for a test case

    # Generate initial allocation guess using equal weights for each security in the portfolio
    securities = len(syms)
    equalAllocation = 1.0 / securities
    allocations = []
    for i in range(0, securities):
        allocations.append(equalAllocation)
    allocs = np.asarray(allocations)

    # This documentation was used to determine how to call SciPy Minimize: https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.minimize.html
    bounds = tuple((0, 1) for value in allocations)
    constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})

    # Call optimizer to minimize negative Sharpe Ratio (maximize Sharpe Ratio)
    result = spo.minimize(optimizer, x0=allocs, args=(prices), method='SLSQP', bounds=bounds, constraints=constraints)
    allocs = result.x

    # Catch for allocations that sum outside tolerance bounds
    # Maintain relative weights and adjust to a 1.0 scale
    total = np.sum(allocs)
    if total > 1.001:
        allocs = allocs/total
    if total < 0.999:
        allocs = allocs * 1/total
    cr, adr, sddr, sr = other_values(allocs, prices)

    # Get daily portfolio value by multiplying the daily prices of each
    # security by its allocation amount and summing the results
    # Normalize the starting values to 1
    port_val = (prices * allocs).sum(axis=1)
    port_val /= port_val[0]
    prices_SPY /= prices_SPY[0]
    # Compare daily portfolio value with SPY using a normalized plot
    if gen_plot:
        # add code to plot here
        df_temp = pd.concat(
            [port_val, prices_SPY], keys=["Portfolio", "SPY"], axis=1
        )
        df_temp.plot().grid(True)
        plt.title("Figure 1:\nPortfolio Performance vs. SPY\n Jun 1, 2008 - Jun 1, 2009")
        plt.xlabel("Date")
        plt.ylabel("Return")
        plt.savefig("Figure1.png")
        plt.clf()
        pass

    return allocs, cr, adr, sddr, sr


# Define objective function to minimize (negative Sharpe Ratio)
def optimizer(allocs, prices):
    # Normalize the prices
    normalized = pd.DataFrame()
    for symbol in prices:
        normalized[symbol] = prices[symbol] / prices[symbol][0]
    # Find value of each position and the whole portfolio; Calculate daily return
    positionValues = normalized * allocs
    portfolioValue = positionValues.sum(axis=1)
    dailyReturn = portfolioValue.pct_change().dropna()

    # Average Daily Returns, Daily Standard Deviation, Daily Sharpe, Yearly Sharpe, Cumulative Return
    adr = dailyReturn.mean()
    sddr = dailyReturn.std()
    dailySharpe = (adr - 0) / sddr
    yearlySharpe = dailySharpe * np.sqrt(252)
    cr = portfolioValue[-1] / portfolioValue[0] - 1

    return -dailySharpe

def other_values(allocs, prices):
    # Normalize the prices
    normalized = pd.DataFrame()
    for symbol in prices:
        normalized[symbol] = prices[symbol] / prices[symbol][0]
    # Find value of each position and the whole portfolio; Calculate daily return
    positionValues = normalized * allocs
    portfolioValue = positionValues.sum(axis=1)
    dailyReturn = portfolioValue.pct_change().dropna()
    # Average Daily Returns, Daily Standard Deviation, Cumulative Return, Daily Sharpe
    adr = dailyReturn.mean()
    sddr = dailyReturn.std()
    cr = portfolioValue[-1] / portfolioValue[0] - 1
    sr = ((adr - 0) / sddr) * np.sqrt(252)

    return cr, adr, sddr, sr

def test_code():
    """  		  	   		 	   			  		 			 	 	 		 		 	
    This function WILL NOT be called by the auto grader.  		  	   		 	   			  		 			 	 	 		 		 	
    """

    start_date = dt.datetime(2009, 1, 1)
    end_date = dt.datetime(2010, 1, 1)
    symbols = ["GOOG", "AAPL", "GLD", "XOM", "IBM"]

    # Assess the portfolio
    allocations, cr, adr, sddr, sr = optimize_portfolio(
        sd=start_date, ed=end_date, syms=symbols, gen_plot=False
    )

    # Print statistics
    print(f"Start Date: {start_date}")
    print(f"End Date: {end_date}")
    print(f"Symbols: {symbols}")
    print(f"Allocations:{allocations}")
    print(f"Sharpe Ratio: {sr}")
    print(f"Volatility (stdev of daily returns): {sddr}")
    print(f"Average Daily Return: {adr}")
    print(f"Cumulative Return: {cr}")

if __name__ == "__main__":
    # This code WILL NOT be called by the auto grader
    # Do not assume that it will be called
    optimize_portfolio()
