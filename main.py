
import import_example
import_example.init()
import import_example2

import multi_function

from multiprocessing import Pool


if __name__ == '__main__':
    with Pool(100) as p:
        print(p.map(multi_function.f, list(range(1,500))))