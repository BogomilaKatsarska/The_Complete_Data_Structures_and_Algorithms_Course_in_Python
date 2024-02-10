# Function to find the length of Longest repeated Subsequence
# of substring X[0..m-1] and X[0..n-1]
def LRSLength(X, m, n):
    # return if we have reached the end of either string
    if m == 0 or n == 0:
        return 0

    # if characters at index m and n matches and index is different
    if X[m - 1] == X[n - 1] and m != n:
        return LRSLength(X, m - 1, n - 1) + 1

    # else if characters at index m and n don't match
    return max(LRSLength(X, m, n - 1), LRSLength(X, m - 1, n))


def LCSLength(S1, S2, lenS1, lenS2):
    # return if we have reached the end of either sequence
    if lenS1 == 0 or lenS2 == 0:
        return 0

    # if last character of S1 and S2 matches
    if S1[lenS1 - 1] == S2[lenS2 - 1]:
        return LCSLength(S1, S2, lenS1 - 1, lenS2 - 1) + 1

    # else if last character of S1 and S2 don't match
    return max(LCSLength(S1, S2, lenS1, lenS2 - 1), LCSLength(S1, S2, lenS1 - 1, lenS2))


# Function to find LCS of X[0..m-1] and Y[0..n-1]
def LCS(X, Y, m, n, T):
    # return empty string if we have reached the end of
    # either sequence
    if m == 0 or n == 0:
        return str()

    # if last character of X and Y matches
    if X[m - 1] == Y[n - 1]:
        # append current character (X[m-1] or Y[n-1]) to LCS of
        # substring X[0..m-2] and Y[0..n-2]
        return LCS(X, Y, m - 1, n - 1, T) + X[m - 1]

    # else when the last character of X and Y are different

    # if top cell of current cell has more value than the left
    # cell, then drop current character of X and find LCS
    # of substring X[0..m-2], Y[0..n-1]

    if T[m - 1][n] > T[m][n - 1]:
        return LCS(X, Y, m - 1, n, T)
    else:
        # if left cell of current cell has more value than the top
        # cell, then drop current character of Y and find LCS
        # of substring X[0..m-1], Y[0..n-2]
        return LCS(X, Y, m, n - 1, T)


# Function to fill lookup table by finding the length of LCS
# of substring X[0..m-1] and Y[0..n-1]
def LCSLength2(X, Y, m, n, T):
    # fill the lookup table in bottom-up manner
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # if current character of X and Y matches
            if X[i - 1] == Y[j - 1]:
                T[i][j] = T[i - 1][j - 1] + 1
            # else if current character of X and Y don't match
            else:
                T[i][j] = max(T[i - 1][j], T[i][j - 1])


X = "ABCBDAB"
Y = "BDCABA"
m = len(X)
n = len(Y)

# T[i][j] stores the length of LCS of substring X[0..i-1], Y[0..j-1]
T = [[0 for x in range(n + 1)] for y in range(m + 1)]

# fill lookup table
LCSLength2(X, Y, m, n, T)

# find longest common sequence

print(LCS(X, Y, m, n, T))


# Function to display the differences between two Strings
def diff(S1, S2, m, n, lookup):
    # if last character of S1 and S2 matches
    if m > 0 and n > 0 and S1[m - 1] == S2[n - 1]:
        diff(S1, S2, m - 1, n - 1, lookup)
        print("", S1[m - 1], end='')

    # current character of S2 is present not in S1
    elif n > 0 and (m == 0 or lookup[m][n - 1] >= lookup[m - 1][n]):

        diff(S1, S2, m, n - 1, lookup)
        print(" +" + S2[n - 1], end='')

    # current character of S1 is present not in S2
    elif m > 0 and (n == 0 or lookup[m][n - 1] < lookup[m - 1][n]):

        diff(S1, S2, m - 1, n, lookup)
        print(" -" + S1[m - 1], end='')


# Function to fill lookup table by finding the length of LCS
# of subS1[0..m-1] and S2[0..n-1]
def LCSLength(S1, S2, m, n, lookup):
    # first column of the lookup table will be all 0
    for i in range(m + 1):
        lookup[i][0] = 0

    # first row of the lookup table will be all 0
    for j in range(n + 1):
        lookup[0][j] = 0

    # fill the lookup table in bottom-up manner
    for i in range(1, m + 1):

        for j in range(1, n + 1):
            # if current character of S1 and S2 matches
            if S1[i - 1] == S2[j - 1]:
                lookup[i][j] = lookup[i - 1][j - 1] + 1
            # else if current character of S1 and S2 don't match
            else:
                lookup[i][j] = max(lookup[i - 1][j], lookup[i][j - 1])


S1 = "ABCDFGHJQZ"
S2 = "ABCDEFGIJKRXYZ"

# lookup[i][j] stores the length of LCS of subS1[0..i-1], S2[0..j-1]
lookup = [[0 for x in range(len(S2) + 1)] for y in range(len(S1) + 1)]

# fill lookup table
LCSLength(S1, S2, len(S1), len(S2), lookup)

# find difference

diff(S1, S2, len(S1), len(S2), lookup)


def SCSLength(X, Y, m, n):
    # if we have reached the end of either sequence, return
    # length of other sequence
    if m == 0 or n == 0:
        return n + m

    # if last character of X and Y matches
    if X[m - 1] == Y[n - 1]:
        return SCSLength(X, Y, m - 1, n - 1) + 1

    # last character of X and Y don't match
    return min(SCSLength(X, Y, m, n - 1) + 1, SCSLength(X, Y, m - 1, n) + 1)


def lps(str):
    n = len(str)

    L = [[0 for x in range(n)] for x in range(n)]

    for i in range(n):
        L[i][i] = 1

    for cl in range(2, n + 1):
        for i in range(n - cl + 1):
            j = i + cl - 1
            if str[i] == str[j] and cl == 2:
                L[i][j] = 2
            elif str[i] == str[j]:
                L[i][j] = L[i + 1][j - 1] + 2
            else:
                L[i][j] = max(L[i][j - 1], L[i + 1][j])

    return L[0][n - 1]


def isSubsetSum(set, n, sum):
    # The value of subset[i][j] will be
    # true if there is a
    # subset of set[0..j-1] with sum equal to i
    subset = ([[False for i in range(sum + 1)]
               for i in range(n + 1)])

    # If sum is 0, then answer is true
    for i in range(n + 1):
        subset[i][0] = True

    for i in range(1, sum + 1):
        subset[0][i] = False

    for i in range(1, n + 1):
        for j in range(1, sum + 1):
            if j < set[i - 1]:
                subset[i][j] = subset[i - 1][j]
            if j >= set[i - 1]:
                subset[i][j] = subset[i - 1][j] or subset[i - 1][j - set[i - 1]]

    return subset[n][sum]


INT_MAX = 32767


# Function to get minimum number of trials needed in worst
# case with n eggs and k floors
def eggDrop(n, k):
    # A 2D table where entery eggFloor[i][j] will represent minimum
    # number of trials needed for i eggs and j floors.
    eggFloor = [[0 for x in range(k + 1)] for x in range(n + 1)]

    # We need one trial for one floor and0 trials for 0 floors
    for i in range(1, n + 1):
        eggFloor[i][1] = 1
        eggFloor[i][0] = 0

    # We always need j trials for one egg and j floors.
    for j in range(1, k + 1):
        eggFloor[1][j] = j

        # Fill rest of the entries in table using optimal substructure
    # property
    for i in range(2, n + 1):
        for j in range(2, k + 1):
            eggFloor[i][j] = INT_MAX
            for x in range(1, j + 1):
                res = 1 + max(eggFloor[i - 1][x - 1], eggFloor[i][j - x])
                if res < eggFloor[i][j]:
                    eggFloor[i][j] = res

                    # eggFloor[n][k] holds the result
    return eggFloor[n][k]


class Pair(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b


def maxChainLength(arr, n):
    maximum = 0

    mcl = [1 for i in range(n)]

    for i in range(1, n):
        for j in range(0, i):
            if arr[i].a > arr[j].b and mcl[i] < mcl[j] + 1:
                mcl[i] = mcl[j] + 1

    for i in range(n):
        if maximum < mcl[i]:
            maximum = mcl[i]

    return maximum
