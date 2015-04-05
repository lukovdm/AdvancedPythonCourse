import time

def russian_peasant_rec_bin(x, y):
    if x == 1:
        return y
    elif x % 2 == 0:
        return russian_peasant_rec_bin(x >> 1, y << 1)
    else:
        return russian_peasant_rec_bin(x >> 1, y << 1) + y