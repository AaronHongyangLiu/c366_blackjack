import blackjack
from pylab import *


def run(numEvaluationEpisodes):
    returnSum = 0.0
    for episodeNum in range(numEvaluationEpisodes):
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
        #print("Episode: ", episodeNum, "Return: ", G)
        returnSum = returnSum + G
    return returnSum / numEvaluationEpisodes


run(2000)
