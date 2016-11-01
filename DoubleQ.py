import blackjack
from pylab import *

Q1 = 0.00001*rand(181, 2)  # NumPy array of correct size
Q2 = 0.00001*rand(181, 2)  # NumPy array of correct size
Q1[0,:] = 0
Q2[0,:] = 0
GAMMA = 1


def learn(alpha, eps, numTrainingEpisodes):
    for episodeNum in range(numTrainingEpisodes):
        S = blackjack.init()
        R, S = blackjack.sample(S, 1)
        while (S):
            Q = Q1[S,:]+Q2[S,:]
            prob1 = np.random.random()
            if prob1 < eps:
                # explore
                A = np.random.choice([0, 1])
            else:
                # greedy
                A = Q.argmax()

            R, S_prime = blackjack.sample(S, A)
            S_prime = int(S_prime)

            prob2 = np.random.choice([1, 2])
            if prob2 == 1:
                Q1[S, A] = Q1[S, A] + alpha * (
                R + GAMMA * Q2[S_prime, (Q1[S_prime]).argmax()] - Q1[S, A])
            else:
                Q2[S, A] = Q2[S, A] + alpha * (R + GAMMA * Q1[S_prime, (Q2[S_prime]).argmax()] - Q2[S, A])

            S = S_prime


def evaluate(numEvaluationEpisodes):
    returnSum = 0.0
    for episodeNum in range(numEvaluationEpisodes):
        G = 0
        S = blackjack.init()
        R, S = blackjack.sample(S, 1)
        while (S):
            Q = Q1[S,:]+Q2[S,:]
            A = Q.argmax()
            R, S = blackjack.sample(S,A)
            G += R

        returnSum = returnSum + G
    return returnSum / numEvaluationEpisodes


learn(0.001,0.01,10000)
for i in range(10000,91000,100):
    print(evaluate(i))