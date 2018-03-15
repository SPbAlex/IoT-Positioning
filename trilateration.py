from room import get_beacons
def trelaterate(dists_3_best):

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
        return 0

    ratio = rssi * 1.0 / txPower
    if ratio < 1:
        return ratio**10
    else:
        accuracy = 0.89976 * ratio**7.7095 + 0.111

    return accuracy