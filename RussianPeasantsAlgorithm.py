import time

def russian_peasant_rec(x, y):
    if x == 1:
        return y
    elif x % 2 == 0:
        return russian_peasant_rec(x >> 1, y << 1)
    else:
        return russian_peasant_rec(x >> 1, y << 1) + y

def test_russian():
    t = time.time()
    print russian_peasant_rec(357, 16)
    print "russian paeasant algoritm took %f seconds." % (time.time()-t)
    assert russian_peasant_rec(357, 16) == 5712

if __name__ == "__main__":
    test_russian()