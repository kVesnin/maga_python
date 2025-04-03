import time
import threading
import multiprocessing

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

def main():
    n = 33
    results = {}

    start = time.time()
    for _ in range(10):
        fib(n)
    results['sync'] = time.time() - start

    start = time.time()
    threads = []
    for _ in range(10):
        t = threading.Thread(target=fib, args=(n,))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    results['thread'] = time.time() - start

    start = time.time()
    processes = []
    for _ in range(10):
        p = multiprocessing.Process(target=fib, args=(n,))
        p.start()
        processes.append(p)
    for p in processes:
        p.join()
    results['process'] = time.time() - start

    with open('artifacts/task1/results.txt', 'w') as f:
        f.write(f"Синхронное выполнение: {results['sync']:.2f} сек\n")
        f.write(f"Потоки: {results['thread']:.2f} сек\n")
        f.write(f"Процессы: {results['process']:.2f} сек\n")

if __name__ == '__main__':
    main()