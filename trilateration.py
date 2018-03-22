from room import get_beacons

def trelaterate(dists_3_best):
    beacons = get_beacons()
    ap = beacons[dists_3_best[0][0]]
    bp = beacons[dists_3_best[1][0]]
    cp = beacons[dists_3_best[2][0]]

    # dists_3_best = [(0, 2),(1, 3),(2, 2)]
    ra, rb, rc = dists_3_best[0][1], dists_3_best[1][1], dists_3_best[2][1]
    sqr = lambda a: a ** 2
    norm = lambda a: sum(map(lambda b: b ** 2, a)) ** 0.5
    dot = lambda a, b: sum([a[i] * b[i] for i in range(len(a))])
    vector_subtract = lambda a, b: tuple(a[i] - b[i] for i in range(len(a)))
    vector_add = lambda a, b: tuple(a[i] + b[i] for i in range(len(a)))
    vector_divide = lambda a, b: tuple(a[i] / b for i in range(len(a)))
    vector_multiply = lambda a, b: tuple(a[i] * b for i in range(len(a)))

    ex, ey, ez, i, j, d, a, x, y, z, b, p4 = [0] * 12

    ex = vector_divide(vector_subtract(bp, ap), norm(vector_subtract(bp, ap)))

    i = dot(ex, vector_subtract(cp, ap))
    a = vector_subtract(vector_subtract(cp, ap), vector_multiply(ex, i))
    ey = vector_divide(a, norm(a))
    d = norm(vector_subtract(bp, ap))
    j = dot(ey, vector_subtract(cp, ap))

    x = (sqr(ra) - sqr(rb) + sqr(d)) / (2 * d)
    y = (sqr(ra) - sqr(rc) + sqr(i) + sqr(j)) / (2 * j) - (i / j) * x

    b = sqr(ra) - sqr(x) - sqr(y)

    if abs(b) < 0.000001:
        b = 0

    a = vector_add(ap, vector_add(vector_multiply(ex, x), vector_multiply(ey, y)))
    # p4a = vector_add(a, vector_multiply(ez, z))
    # p4b = vector_subtract(a, vector_multiply(ez, z))

    return a

def trelaterate_old(dists_3_best):

    beacons = get_beacons()
    ax, ay = beacons[dists_3_best[0][0]]
    bx, by = beacons[dists_3_best[1][0]]
    cx, cy = beacons[dists_3_best[2][0]]

    # dists_3_best = [(0, 2),(1, 3),(2, 2)]
    ra, rb, rc = dists_3_best[0][1], dists_3_best[1][1], dists_3_best[2][1]

    S = (cx**2 - bx**2 + cy**2 - by**2 + rb**2 - rc**2) / 2

    T = (ax**2 - bx**2 + ay**2 - by**2 + rb**2 - ra**2) / 2
    y = ((T * (bx - cx)) - (S * (bx - ax))) / (((ay - by) * (bx - cx)) - ((cy - by) * (bx - ax)))
    x = ((y * (ay - by)) - T) / (bx - ax)

    print(x, y, )

    return x, y

def get_distance(txPower, rssi):

    if rssi == 0:
        return None

    n = 4
    d = 10**((txPower-rssi)/(10*n))

    # ratio = rssi * 1.0 / txPower
    # if ratio < 1:
    #     return ratio**10
    # else:
    #     d = 0.89976 * ratio**7.7095 + 0.111

    return d