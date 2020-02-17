def solution(A):
    # write your code in Python 3.6
    N = len(A)
    P = prefix_sums(A)
    position = 0
    minimal = average(P,position,position+1)
    for p in range(N-1):
        for q in range(p+1,p+3):
            if q < N:
                avg = average(P,p,q)
                if avg < minimal:
                    minimal = avg
                    position = p
    return position
    
def average (P,x,y):
    return count_total(P,x,y)/(y-x+1)
    
def count_total(P, x, y):
    return P[y + 1] - P[x]
    
def prefix_sums(A):
    N = len(A)
    P = [0] * (N + 1)
    for K in range(N):
        P[K + 1] = P[K] + A[K]
    return P

'''
A non-empty array A consisting of N integers is given. A pair of integers (P, Q), such that 0 ≤ P < Q < N, is called a slice of array A (notice that the slice contains at least two elements). The average of a slice (P, Q) is the sum of A[P] + A[P + 1] + ... + A[Q] divided by the length of the slice. To be precise, the average equals (A[P] + A[P + 1] + ... + A[Q]) / (Q − P + 1).

For example, array A such that:

    A[0] = 4
    A[1] = 2
    A[2] = 2
    A[3] = 5
    A[4] = 1
    A[5] = 5
    A[6] = 8
contains the following example slices:

slice (1, 2), whose average is (2 + 2) / 2 = 2;
slice (3, 4), whose average is (5 + 1) / 2 = 3;
slice (1, 4), whose average is (2 + 2 + 5 + 1) / 4 = 2.5.
The goal is to find the starting position of a slice whose average is minimal.

Write a function:

def solution(A)

that, given a non-empty array A consisting of N integers, returns the starting position of the slice with the minimal average. If there is more than one slice with a minimal average, you should return the smallest starting position of such a slice.

For example, given array A such that:

    A[0] = 4
    A[1] = 2
    A[2] = 2
    A[3] = 5
    A[4] = 1
    A[5] = 5
    A[6] = 8
the function should return 1, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [2..100,000];
each element of array A is an integer within the range [−10,000..10,000].
'''