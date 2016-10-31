import blackjack
from pylab import *


def run(numEpisodes):
    returnSum = 0.0
    for episodeNum in range(numEpisodes):
        G = 0
        S = blackjack.init()
        A = [1, 0]
        a = np.random.choice(A)
        R, S = blackjack.sample(S, a)
        G += R
        while (S):
            a = np.random.choice(A)
            R, S = blackjack.sample(S, a)
            G += R
        print("Episode: ", episodeNum, "Return: ", G)
        returnSum = returnSum + G
    return returnSum / numEpisodes


run(2000)
