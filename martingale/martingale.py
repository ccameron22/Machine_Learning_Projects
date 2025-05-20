""""""  		  	   		 	   			  		 			 	 	 		 		 	
"""Assess a betting strategy.  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
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
  		  	   		 	   			  		 			 	 	 		 		 	
import numpy as np
import matplotlib.pyplot as plt
  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
def author():  		  	   		 	   			  		 			 	 	 		 		 	
    """  		  	   		 	   			  		 			 	 	 		 		 	
    :return: The username of the student  		  	   		 	   			  		 			 	 	 		 		 	
    :rtype: str  		  	   		 	   			  		 			 	 	 		 		 	
    """  		  	   		 	   			  		 			 	 	 		 		 	
    return "xxx"


def study_group():

    return "xxx"
  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
def gtid():  		  	   		 	   			  		 			 	 	 		 		 	
    """  		  	   		 	   			  		 			 	 	 		 		 	
    :return: The ID of the student  		  	   		 	   			  		 			 	 	 		 		 	
    :rtype: int  		  	   		 	   			  		 			 	 	 		 		 	
    """  		  	   		 	   			  		 			 	 	 		 		 	
    return xxx  
  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
def get_spin_result(win_prob):  		  	   		 	   			  		 			 	 	 		 		 	
    """  		  	   		 	   			  		 			 	 	 		 		 	
    Given a win probability between 0 and 1, the function returns whether the probability will result in a win.  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
    :param win_prob: The probability of winning  		  	   		 	   			  		 			 	 	 		 		 	
    :type win_prob: float  		  	   		 	   			  		 			 	 	 		 		 	
    :return: The result of the spin.  		  	   		 	   			  		 			 	 	 		 		 	
    :rtype: bool  		  	   		 	   			  		 			 	 	 		 		 	
    """  		  	   		 	   			  		 			 	 	 		 		 	
    result = False  		  	   		 	   			  		 			 	 	 		 		 	
    if np.random.random() <= win_prob:  		  	   		 	   			  		 			 	 	 		 		 	
        result = True  		  	   		 	   			  		 			 	 	 		 		 	
    return result  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
def test_code():  		  	   		 	   			  		 			 	 	 		 		 	
    """  		  	   		 	   			  		 			 	 	 		 		 	
    Method to test your code  		  	   		 	   			  		 			 	 	 		 		 	
    """
    win_prob = 0.4737  # set appropriately to the probability of a win
    np.random.seed(gtid())  # do this only once
    # add your code here to implement the experiments`

    basic_10(win_prob)
    basic_1000(win_prob)
    realistic_1000(win_prob)


def basic_10(win_prob):

    # Create array and set episode count to 0
    winLoss = np.zeros((10, 1001))
    episodeTracker = 0

    while episodeTracker < 10:
        # initialize variables for the loop
        episode_winnings = 0
        spinTracker = 0
        bet_amount = 1

        while spinTracker < 1000:
            # Get the result of the current spin
            result = (get_spin_result(win_prob))
            # If the bet won add the current winnings to the total winnings, then add the total winnings to
            # the next cell in the array1000
            # If the total winnings have exceeded 80, fill the rest of the array with the total winnings and
            # set the tracker to trigger an end to the loop
            if result:
                episode_winnings = episode_winnings + bet_amount
                winLoss[episodeTracker, spinTracker + 1] = episode_winnings
                if episode_winnings >= 80:
                    for i in range(spinTracker, 1001):
                        winLoss[episodeTracker, i] = episode_winnings
                    spinTracker = 1000
            # If the bet lost, subtr1000act it from the total winnings and double the amount of the next bet
            else:
                episode_winnings = episode_winnings - bet_amount
                winLoss[episodeTracker, spinTracker + 1] = episode_winnings
                bet_amount = bet_amount * 2
            spinTracker += 1
        episodeTracker += 1

    # Plot all rows on the same graph, save as a png, and clear the plot
    for i in range(10):
        plt.plot(np.arange(1, 1001), winLoss[i, 1:], label=f'Episode {i + 1}')
    # Add a title
    plt.title('Figure 1: 10 Episode Winnings')
    # Set x and y limits
    plt.xlim(0, 300)
    plt.ylim(-256, +100)
    # Add labels and legend
    plt.xlabel('Spins')
    plt.ylabel('Winnings')
    plt.legend()
    plt.savefig('tenEpisodePlot.png')
    plt.clf()


def basic_1000(win_prob):

    # Create array and set episode count to 0
    winLoss = np.zeros((1000, 1001))
    episodeTracker = 0

    while episodeTracker < 1000:
        # initialize variables for the loop
        episode_winnings = 0
        spinTracker = 0
        bet_amount = 1

        while spinTracker < 1000:
            # Get the result of the current spin
            result = (get_spin_result(win_prob))
            # If the bet won add the current winnings to the total winnings, then add the total winnings to
            # the next cell in the array
            # If the total winnings have exceeded 80, fill the rest of the array with the total winnings and
            # set the tracker to trigger an end to the loop
            if result:
                episode_winnings = episode_winnings + bet_amount
                winLoss[episodeTracker, spinTracker + 1] = episode_winnings
                if episode_winnings >= 80:
                    for i in range(spinTracker, 1001):
                        winLoss[episodeTracker, i] = episode_winnings
                    spinTracker = 1000
            # If the bet lost, subtract it from the total winnings and double the amount of the next bet
            else:
                episode_winnings = episode_winnings - bet_amount
                winLoss[episodeTracker, spinTracker + 1] = episode_winnings
                bet_amount = bet_amount * 2
            spinTracker += 1
        episodeTracker += 1

    # Find the mean, median, and standard deviation
    medians = np.median(winLoss, axis = 0)
    means = np.mean(winLoss, axis = 0)
    # Calculate standard deviation
    stdDev = np.std(winLoss, axis = 0)

    # Find number of episodes that won at least $80 as well as the average value of a win and a loss
    winningEpisodes = 0
    winningValue = 0
    losingValue = 0
    for i in range(0, 1000):
        if winLoss[i, 1000] >= 80:
            winningEpisodes += 1
            winningValue += winLoss[i, 1000]
        else:
            losingValue += winLoss[i, 1000]
    if winningEpisodes < 1000:
        losingValue /= 1000 - winningEpisodes
        winningValue /= winningEpisodes
    else:
        winningValue /= 1000

    # Find the odds of winning a random episode, and the mean and median winnings to be expected of a random episode
    oddsOfWinning = winningEpisodes/1000
    totalWinnings = 0
    for i in range(0, 1000):
        totalWinnings += winLoss[i, 1000]
    meanWinnings = totalWinnings/1000
    medianWinnings = np.median(medians)

    #print(oddsOfWinning)
    #print(meanWinnings)
    #print(medianWinnings)
    #print(winningValue)

    # Plot the mean
    plt.plot(np.arange(len(means)), means, label='Mean Winnings')
    # Plot the mean + standard deviation
    plt.plot(np.arange(len(means)), means + stdDev, label='Mean + Std. Dev.')
    # Plot the mean - standard deviation
    plt.plot(np.arange(len(means)), means - stdDev, label='Mean - Std. Dev.')
    # Add a title
    plt.title('Figure 2: Basic Function Mean and Deviation')
    # Set x and y limits
    plt.xlim(0, 300)
    plt.ylim(-256, +100)
    # Add labels and legend
    plt.xlabel('Spins')
    plt.ylabel('Winnings')
    plt.legend()
    # Save plot as PNG file and then clear plot
    plt.savefig('basicMeanPlot.png')
    plt.clf()

    # Plot the median
    plt.plot(np.arange(len(medians)), medians, label='Median Winnings')
    # Plot the median + standard deviation
    plt.plot(np.arange(len(medians)), medians + stdDev, label='Median + Std. Dev.')
    # Plot the median - standard deviation
    plt.plot(np.arange(len(medians)), medians - stdDev, label='Median - Std. Dev.')
    # Add a title
    plt.title('Figure 3: Basic Function Median and Deviation')
    # Set x and y limits
    plt.xlim(0, 300)
    plt.ylim(-256, +100)
    # Add labels and legend
    plt.xlabel('Spins')
    plt.ylabel('Winnings')
    plt.legend()
    # Save plot as PNG file
    plt.savefig('basicMedianPlot.png')
    plt.clf()

def realistic_1000(win_prob):

    # Create array and set episode count to 0
    winLoss = np.zeros((1000, 1001))
    episodeTracker = 0

    while episodeTracker < 1000:
        # initialize variables for the loop
        bankroll = 256
        episode_winnings = 0
        spinTracker = 0
        bet_amount = 1

        while spinTracker < 1000:
            # Get the result of the current spin
            result = (get_spin_result(win_prob))
            # Check if the bankroll is large enough to cover the proposed bet; If not, set the
            # proposed bet to the size of the bankroll
            if bankroll < bet_amount:
                bet_amount = bankroll
            # If the bet won add the current winnings to the total winnings, then add the total winnings to
            # the next cell in the array
            # If the total winnings have exceeded 80, fill the rest of the array with the total winnings and
            # set the tracker to trigger an end to the loop
            if result:
                episode_winnings = episode_winnings + bet_amount
                winLoss[episodeTracker, spinTracker + 1] = episode_winnings
                bankroll += bet_amount
                if episode_winnings >= 80:
                    for i in range(spinTracker, 1001):
                        winLoss[episodeTracker, i] = episode_winnings
                    spinTracker = 1000
            # If the bet lost, subtract it from the total winnings and double the amount of the next bet
            else:
                episode_winnings = episode_winnings - bet_amount
                winLoss[episodeTracker, spinTracker + 1] = episode_winnings
                bankroll -= bet_amount
                bet_amount = bet_amount * 2
                if episode_winnings < -255:
                    for i in range(spinTracker, 1001):
                        winLoss[episodeTracker, i] = episode_winnings
                    spinTracker = 1000
            spinTracker += 1
        episodeTracker += 1

    # Find the mean, median and standard deviation
    medians = np.median(winLoss, axis = 0)
    means = np.mean(winLoss, axis = 0)
    # Calculate standard deviation
    stdDev = np.std(winLoss, axis = 0)

    # Find number of episodes that won at least $80 as well as the average value of a win and a loss
    winningEpisodes = 0
    winningValue = 0
    losingValue = 0
    for i in range(0, 1000):
        if winLoss[i, 1000] >= 80:
            winningEpisodes += 1
            winningValue += winLoss[i, 1000]
        else:
            losingValue += winLoss[i, 1000]
    losingValue /= 1000 - winningEpisodes
    winningValue /= winningEpisodes

    # Find the odds of winning a random episode, and the mean and median winnings to be expected of a random episode
    oddsOfWinning = winningEpisodes/1000
    totalWinnings = 0
    for i in range(0, 1000):
        totalWinnings += winLoss[i, 1000]
    meanWinnings = totalWinnings/1000
    medianWinnings = np.median(medians)

    #print(oddsOfWinning)
    #print(meanWinnings)
    #print(medianWinnings)
    #print(winningValue)
    #print(losingValue)

    # Plot the mean
    plt.plot(np.arange(len(means)), means, label='Mean Winnings')
    # Plot the mean + standard deviation
    plt.plot(np.arange(len(means)), means + stdDev, label='Mean + Std. Dev.')
    # Plot the mean - standard deviation
    plt.plot(np.arange(len(means)), means - stdDev, label='Mean - Std. Dev.')
    # Add a title
    plt.title('Figure 4: Realistic Function Mean and Deviation')
    # Set x and y limits
    plt.xlim(0, 300)
    plt.ylim(-256, +100)
    # Add labels and legend
    plt.xlabel('Spins')
    plt.ylabel('Winnings')
    plt.legend()
    # Save plot as PNG file and then clear plot
    plt.savefig('realisticMeanPlot.png')
    plt.clf()

    # Plot the median
    plt.plot(np.arange(len(medians)), medians, label='Median Winnings')
    # Plot the median + standard deviation
    plt.plot(np.arange(len(medians)), medians + stdDev, label='Median + Std. Dev.')
    # Plot the median - standard deviation
    plt.plot(np.arange(len(medians)), medians - stdDev, label='Median - Std. Dev.')
    # Set x and y limits
    plt.xlim(0, 300)
    plt.ylim(-256, +100)
    # Add a title
    plt.title('Figure 5: Realistic Function Median and Deviation')
    # Add labels and legend
    plt.xlabel('Spins')
    plt.ylabel('Winnings')
    plt.legend()
    # Save plot as PNG file
    plt.savefig('realisticMedianPlot.png')
    plt.clf()



if __name__ == "__main__":  		  	   		 	   			  		 			 	 	 		 		 	
    test_code()  		  	   		 	   			  		 			 	 	 		 		 	
