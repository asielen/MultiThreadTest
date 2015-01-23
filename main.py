import import_example
import_example.init()

from multiprocessing import Pool

def f(x):
    return x*x

if __name__ == '__main__':
    with Pool(100) as p:
        print(p.map(f, list(range(1,500))))