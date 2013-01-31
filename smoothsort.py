def isAscending(v1, v2):
    """Comparator function"""
    return v1 <= v2

def smoothSort(A):
    """The main SmoothSort function
        Variables: q,r,p,b,c,r1,b1,c1,N
    """

    def up(vb, vc):
        temp = vb
        vb += vc + 1
        vc = temp
        return vb, vc

    def down(vb, vc):
        temp = vc
        vc = vb - vc - 1
        vb = temp
        return vb, vc

    def sift():
        r0 = smoothSort.r1
        T = A[r0]
        while smoothSort.b1 >= 3:
            r2 = smoothSort.r1 - smoothSort.b1 + smoothSort.c1

            if not isAscending(A[smoothSort.r1 - 1], A[r2]):
                r2 = smoothSort.r1 - 1
                smoothSort.b1, smoothSort.c1 = down(smoothSort.b1, smoothSort.c1)
            if isAscending(A[r2], T):
                smoothSort.b1 = 1
            else:
                A[smoothSort.r1] = A[r2]
                smoothSort.r1 = r2
                smoothSort.b1, smoothSort.c1 = down(smoothSort.b1, smoothSort.c1)
        #print((smoothSort.r1 - r0))
        if smoothSort.r1 != r0:
            A[smoothSort.r1] = T

    def trinkle():
        p1 = smoothSort.p
        smoothSort.b1 = smoothSort.b
        smoothSort.c1 = smoothSort.c
        r0 = smoothSort.r1
        T = A[r0]
        while p1 > 0:
            while (p1 & 1) == 0:
                p1 >>= 1
                smoothSort.b1, smoothSort.c1 = up(smoothSort.b1, smoothSort.c1)
            r3 = smoothSort.r1 - smoothSort.b1
            if p1 == 1 or isAscending(A[r3], T):
                p1 = 0
            else:
                p1 -= 1
                if smoothSort.b1 == 1:
                    A[smoothSort.r1] = A[r3]
                    smoothSort.r1 = r3
                elif smoothSort.b1 >= 3:
                    r2 = smoothSort.r1 - smoothSort.b1 + smoothSort.c1
                    if not isAscending(A[smoothSort.r1 - 1], A[r2]):
                        r2 = smoothSort.r1 - 1
                        smoothSort.b1, smoothSort.c1 = down(smoothSort.b1, smoothSort.c1)
                        p1 <<= 1
                    if isAscending(A[r2], A[r3]):
                        A[smoothSort.r1] = A[r3]
                        smoothSort.r1 = r3
                    else:
                        A[smoothSort.r1] = A[r2]
                        smoothSort.r1 = r2
                        smoothSort.b1, smoothSort.c1 = down(smoothSort.b1, smoothSort.c1)
                        p1 = 0
        if r0 != smoothSort.r1:
            A[smoothSort.r1] = T
        sift()

    def semitrinkle():
        smoothSort.r1 = smoothSort.r - smoothSort.c
        if not isAscending(A[smoothSort.r1], A[smoothSort.r]):
            A[smoothSort.r], A[smoothSort.r1] = A[smoothSort.r1], A[smoothSort.r]
            trinkle()

    # Start of main function
    smoothSort.N = len(A)
    smoothSort.q = 1
    smoothSort.r = 0
    smoothSort.p = 1
    smoothSort.b = 1
    smoothSort.c = 1
    #building the tree
    while smoothSort.q < smoothSort.N:
        smoothSort.r1 = smoothSort.r

        if (smoothSort.p & 7) == 3:
            smoothSort.b1 = smoothSort.b
            smoothSort.c1 = smoothSort.c
            sift()
            smoothSort.p = (smoothSort.p + 1) >> 2
            smoothSort.b, smoothSort.c = up(smoothSort.b, smoothSort.c)
            smoothSort.b, smoothSort.c = up(smoothSort.b, smoothSort.c)
        elif (smoothSort.p & 3) == 1:
            if (smoothSort.q + smoothSort.c) < smoothSort.N:
                smoothSort.b1 = smoothSort.b
                smoothSort.c1 = smoothSort.c
                sift()
            else:
                trinkle()
            smoothSort.b, smoothSort.c = down(smoothSort.b, smoothSort.c)
            smoothSort.p = smoothSort.p << 1
            while smoothSort.b > 1:
                smoothSort.b, smoothSort.c = down(smoothSort.b, smoothSort.c)
                smoothSort.p = smoothSort.p << 1
            smoothSort.p += 1
        smoothSort.q += 1
        smoothSort.r += 1

    smoothSort.r1 = smoothSort.r
    trinkle()

    #build the sorted array
    while smoothSort.q > 1:
        smoothSort.q -= 1
        if smoothSort.b == 1:
            smoothSort.r = smoothSort.r - 1
            smoothSort.p = smoothSort.p - 1
            while (smoothSort.p & 1) == 0:
                smoothSort.p = smoothSort.p >> 1
                smoothSort.b, smoothSort.c = up(smoothSort.b, smoothSort.c)
        elif (smoothSort.b >= 3):
            smoothSort.p -= 1
            smoothSort.r = smoothSort.r - smoothSort.b + smoothSort.c
            if smoothSort.p > 0:
                semitrinkle()
            smoothSort.b, smoothSort.c = down(smoothSort.b, smoothSort.c)
            smoothSort.p = (smoothSort.p << 1) + 1
            smoothSort.r = smoothSort.r + smoothSort.c
            semitrinkle()
            smoothSort.b, smoothSort.c = down(smoothSort.b, smoothSort.c)
            smoothSort.p = (smoothSort.p << 1) + 1
            # element q is done
            # element 0 is down