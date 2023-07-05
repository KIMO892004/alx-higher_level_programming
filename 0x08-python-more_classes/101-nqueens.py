#!/usr/bin/python3
"""
the nqueens backtracking program to print the coordinates of n queens
on an nxn grid such that they are all in non-attacking positions
"""


from sys import argv

if __name__ == "__main__":
    k = []
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if argv[1].isdigit() is False:
        print("N must be a number")
        exit(1)
    n = int(argv[1])
    if n < 4:
        print("N must be at least 4")
        exit(1)

    # initializing the answer list
    for r in range(n):
        k.append([r, None])

    def already_exists(y):
        """checking that a queen does not already exist in that y value"""
        for x in range(n):
            if y == k[x][1]:
                return True
        return False

    def reject(x, y):
        """determining whether or not to reject the solution"""
        if (already_exists(y)):
            return False
        r = 0
        while(r < x):
            if abs(k[r][1] - y) == abs(r - x):
                return False
            r += 1
        return True

    def clear_a(x):
        """clearing the answers from the point of failure on"""
        for r in range(x, n):
            k[r][1] = None

    def nqueens(x):
        """recursiving backtracking function to find the solution"""
        for y in range(n):
            clear_a(x)
            if reject(x, y):
                k[x][1] = y
                if (x == n - 1):  # accepting the solution
                    print(k)
                else:
                    nqueens(x + 1)  # moveing on to next x value to continue

    # starting the recursive process at x = 0
    nqueens(0)
