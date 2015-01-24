import multi_function
import import_example2
import import_example
if __name__ == "__main__": import_example.init()

from multiprocessing import Pool

if __name__ == '__main__':
    import_example2.test()
    with Pool(100) as p:
        print(p.map(multi_function.f, list(range(1,500))))