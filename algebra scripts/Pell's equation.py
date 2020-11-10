"""
I solve equation | x^2 - 2 * y^2 | = 0 in integers.
And so i find units of the Z[sqrt(t)] ring.
"""

x=1
s=2**0.5
print('all +- pairs are solutions too')
print('ura!', '1', '0', 'PROVERKA:', '1')
while True:
    y=round(x/s)
    if abs(x**2 - 2*(y**2)) == 1:
        print('ura!', x, y, 'PROVERKA:', x*x-2*y*y)
    if abs(x**2 - 2*((y+1)**2)) == 1:
        print('ura!', x, y, 'PROVERKA:', x*x-2*(y+1)*(y+1))
    if abs(x**2 - 2*((y-1)**2)) == 1:
        print('ura!', x, y, 'PROVERKA:', x*x-2*(y-1)*(y-1))
    x += 1
