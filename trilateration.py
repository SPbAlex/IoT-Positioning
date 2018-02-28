
def trelaterate(rb, ra, rc):

    cx, cy = 0, 4

    ax, ay = 1, 0

    bx, by = 8, 1

    rb, ra, rc = 5, 40, 4

    S = (cx**2 - bx**2 + cy**2 - by**2 + rb**2 - rc**2) / 2

    T = (ax**2 - bx**2 + ay**2 - by**2 + rb**2 - ra**2) / 2
    y = ((T * (bx - cx)) - (S * (bx - ax))) / (((ay - by) * (bx - cx)) - ((cy - by) * (bx - ax)))
    x = ((y * (ay - by)) - T) / (bx - ax)

    print(x, y)

    return x, y