import blackjack
from pylab import *

Q1 = 0.00001*rand(181, 2)  # NumPy array of correct size
Q2 = 0.00001*rand(181, 2)  # NumPy array of correct size
Q1[0,:] = 0
Q2[0,:] = 0
GAMMA = 1


def learn(alpha, eps, numTrainingEpisodes):
    returnSum = 0.0
    for episodeNum in range(numTrainingEpisodes):
        G = 0
        S = blackjack.init()
        R, S = blackjack.sample(S, 1)
        G += R
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
            G += R
            S_prime = int(S_prime)

            prob2 = np.random.choice([1, 2])
            if prob2 == 1:
                Q1[S, A] = Q1[S, A] + alpha * (
                R + GAMMA * Q2[S_prime, (Q1[S_prime]).argmax()] - Q1[S, A])
            else:
                Q2[S, A] = Q2[S, A] + alpha * (R + GAMMA * Q1[S_prime, (Q2[S_prime]).argmax()] - Q2[S, A])

            S = S_prime
        #print("Episode: ", episodeNum, "Return: ", G)
        returnSum = returnSum + G
        if episodeNum % 100000 == 0 and episodeNum != 0:
            print("Average return so far: ", returnSum/episodeNum)


def evaluate(numEvaluationEpisodes):
    returnSum = 0.0
    for episodeNum in range(numEvaluationEpisodes):
        G = 0
        S = blackjack.init()
        R, S = blackjack.sample(S, 1)
        G += R
        while (S):
            Q = Q1[S,:]+Q2[S,:]
            A = Q.argmax()
            R, S = blackjack.sample(S, A)
            G += R

        returnSum = returnSum + G

    return returnSum / numEvaluationEpisodes

def policy(state):
    Q = Q1[state,:]+Q2[state,:]
    return Q.argmax()

def getOurPolicy():
    Q = Q1+Q2
    P = zeros(181)
    for row in range(181):
        P[row] = Q[row].argmax()
    return P

def getOptimal():
    p = np.array([0] + ([1]*5+[0]*4) + ([1]*1+[0]*8)*2 + ([0]*9)*3 + ([1]*5+[0]*4)*4 +
                 ([1]*7+[0]*2) + ([1]*6+[0]*3)*7 + ([1]*7+[0]*2)*2)
    return p

def optimal(state):
    p=getOptimal()
    return p[state]
#blackjack.printPolicy(optimal)

# to find the best policy:
training = 1000000
best = [0,0,0,99999999] # alpha,eps,training,error
P = getOptimal()

for alpha in [0.002]:
    for eps in [0.345]:
        Q1 = 0.00001*rand(181, 2)  # NumPy array of correct size
        Q2 = 0.00001*rand(181, 2)  # NumPy array of correct size
        Q1[0,:] = 0
        Q2[0,:] = 0
        learn(alpha,eps,training)
        eP = getOurPolicy()
        error = norm(eP[1:]-P[1:])
        if error <= 1.5:
            blackjack.printPolicy(policy)
        print("########## ",alpha,eps,training," #######",error)
        if error <= 1.5:
            print("==============",evaluate(1000000),"================\n")
        if error < best[3]:
            best[0]=alpha
            best[1]=eps
            best[2]=training
            best[3]=error

print(best)
