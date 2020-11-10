"""
I solve equation x^2 = 1 in ring Z/n.
"""

def solver(n):
    solution = []
    print ('work in ring Z /', n)
    for i in range(n):
        temp = i**2
        while True:
            if temp >= n:
                temp -= n
            if temp < n:
                break
        if temp == 1:
            solution.append(i)
    return solution

n1 = int(input())

print(solver(n1))
