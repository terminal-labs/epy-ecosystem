from timeit import timeit

from hmmpy import hmm
from chmmpy import hmm as chmm

m=hmm(2, 2)
cm=chmm(2,2)

observations=[[0,0,0,0,0,1,1,1,1,1,0,1,0,0,0,1,0,1,1,1,1],[0,0,0,0,1,0,1,1,0,1,1,0,0,1,0,0,1,1,1,1,0,0,1,0,0]]
ground_truths=[[0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1],[0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,0,0,0,0,0]]

m.learn(observations, ground_truths)
cm.learn(observations, ground_truths)

def py():
    m.viterbi(observations[1])

def cy():
    cm.viterbi(observations[1])

number = 10_000
t1 = timeit("py()", setup="from __main__ import py", number=number)
t2 = timeit("cy()", setup="from __main__ import cy", number=number)

print(f"Python: {t1}, ePython: {t2} (X {t1 / t2})")
