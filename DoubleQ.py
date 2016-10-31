import blackjack
import numpy as np
from pylab import *

numEpisodes = 2000
Q1 = {}
Q2 = {}
# initialize the two Q values:
for i in range(181):
    Q1[(i,0)] = 0
    Q1[(i,1)] = 0
    Q2[(i,0)] = 0
    Q2[(i,1)] = 0

returnSum = 0.0
for episodeNum in range(numEpisodes):
    G = 0
    S = blackjack.init()
    A = [1,0]
    a = np.random.choice(A)
    R,S = blackjack.sample(S,a)
    G += R
    while (S):
        a = np.random.choice(A)
        R,S = blackjack.sample(S,a)
        G += R
    print("Episode: ", episodeNum, "Return: ", G)
    returnSum = returnSum + G
print("Average return: ", returnSum/numEpisodes)
