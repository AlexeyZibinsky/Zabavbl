""" Программа находит все элементы мультипликативной
группы кольца из элементов a+bi, где a,b целые числа по модулю 4"""

hui = 0
for i in range(4):
    for j in range(4):
        for k in range(4):
            for l in range(4):
                hui+=1
                a = i*k-j*l
                b = i*l+k*j
                if a>0:
                    while a>=4:
                        a -= 4
                if a<0:
                    while a<=-4:
                        a += 4
                    a = 4 + a
                if b>0:
                    while b>=4:
                        b -= 4
                if b<0:
                    while b<=-4:
                        b += 4
                    b = 4 + b
                if a == 1 and b ==0:
                    print((i,j),'*',(k,l),'=',(a,b))
print('hui =', hui)
