def isAscending(v1, v2):
    """Comparator function"""
    return v1 <= v2


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


def smoothSort(A):
    """The main SmoothSort function
        Variables: q,r,p,b,c,r1,b1,c1,N
    """

    def sift():
        nonlocal r1, b1, c1
        r0 = r1
        T = A[r0]
        while b1 >= 3:
            r2 = r1 - b1 + c1

            if not isAscending(A[r1 - 1], A[r2]):
                r2 = r1 - 1
                b1, c1 = down(b1, c1)
            if isAscending(A[r2], T):
                b1 = 1
            else:
                A[r1] = A[r2]
                r1 = r2
                b1, c1 = down(b1, c1)
        if r1 != r0:
            A[r1] = T

    def trinkle():
        nonlocal p, b1, c1, b, c, r1
        p1 = p
        b1 = b
        c1 = c
        r0 = r1
        T = A[r0]
        while p1 > 0:
            while (p1 & 1) == 0:
                p1 >>= 1
                b1, c1 = up(b1, c1)
            r3 = r1 - b1
            if p1 == 1 or isAscending(A[r3], T):
                p1 = 0
            else:
                p1 -= 1
                if b1 == 1:
                    A[r1] = A[r3]
                    r1 = r3
                elif b1 >= 3:
                    r2 = r1 - b1 + c1
                    if not isAscending(A[r1 - 1], A[r2]):
                        r2 = r1 - 1
                        b1, c1 = down(b1, c1)
                        p1 <<= 1
                    if isAscending(A[r2], A[r3]):
                        A[r1] = A[r3]
                        r1 = r3
                    else:
                        A[r1] = A[r2]
                        r1 = r2
                        b1, c1 = down(b1, c1)
                        p1 = 0
        if r0 != r1:
            A[r1] = T
        sift()

    def semitrinkle():
        nonlocal r1, r, c
        r1 = r - c
        if not isAscending(A[r1], A[r]):
            A[r], A[r1] = A[r1], A[r]
            trinkle()

    # Start of main function
    N = len(A)
    q = 1
    r = 0
    p = 1
    b = 1
    c = 1
    #building the tree
    while q < N:
        r1 = r

        if (p & 7) == 3:
            b1 = b
            c1 = c
            sift()
            p = (p + 1) >> 2
            b, c = up(b, c)
            b, c = up(b, c)
        elif (p & 3) == 1:
            if (q + c) < N:
                b1 = b
                c1 = c
                sift()
            else:
                trinkle()
            b, c = down(b, c)
            p <<= 1
            while b > 1:
                b, c = down(b, c)
                p <<= 1
            p += 1
        q += 1
        r += 1

    r1 = r
    trinkle()

    #build the sorted array
    while q > 1:
        q -= 1
        if b == 1:
            r -= 1
            p -= 1
            while (p & 1) == 0:
                p >>= 1
                b, c = up(b, c)
        elif b >= 3:
            p -= 1
            r = r - b + c
            if p > 0:
                semitrinkle()
            b, c = down(b, c)
            p = (p << 1) + 1
            r += c
            semitrinkle()
            b, c = down(b, c)
            p = (p << 1) + 1
            # element q is done
            # element 0 is done

