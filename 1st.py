'''print('My Name is priya Singh')'''

from itertools import product
print('now we take an experiment is of tossing two coins')
n=2
sample_space=set(product(['H','T'],repeat=n))
print('Here sample space is = ',sample_space,' : here total number of possible outcomes is = 4')
length=len(sample_space)
print('here question 1 is complete print the sample space')
print()
print()
print('here we assume that the outcomes(A) will be head appear first')
A={OH for OH in sample_space if OH[0]=='H'}
print('outcomes of A=',A,'= 2')
def prob(X):
    return len(X)/len(sample_space)
print('probability of head appear first is : P(A)=',prob(A))
print('here question 2 is complete')
