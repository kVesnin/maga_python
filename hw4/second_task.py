import math
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import os

def integrate_part(f, a, step, start, end):
    partial_acc = 0
    for i in range(start, end):
        partial_acc += f(a + i * step) * step
    return partial_acc

def integrate(f, a, b, *, n_jobs=1, n_iter=10000000, executor):
    step = (b - a) / n_iter
    chunk_size = n_iter // n_jobs
    futures = []
    with executor(max_workers=n_jobs) as pool:
        for j in range(n_jobs):
            start = j * chunk_size
            end = start + chunk_size
            if j == n_jobs - 1:
                end = n_iter
            future = pool.submit(integrate_part, f, a, step, start, end)
            futures.append(future)
        total = sum(f.result() for f in futures)
    return total

def main():
    cpu_num = os.cpu_count()
    n_jobs_values = list(range(1, cpu_num * 2 + 1))
    results = []

    for n_jobs in n_jobs_values:
        start = time.time()
        integrate(math.cos, 0, math.pi/2, n_jobs=n_jobs, executor=ThreadPoolExecutor)
        thread_time = time.time() - start

        start = time.time()
        integrate(math.cos, 0, math.pi/2, n_jobs=n_jobs, executor=ProcessPoolExecutor)
        process_time = time.time() - start

        results.append((n_jobs, thread_time, process_time))
        print(f"n_jobs={n_jobs:2}: threads={thread_time:.3f}s | processes={process_time:.3f}s")

    with open("artifacts/task2/timing_report.csv", "w") as f:
        f.write("n_jobs,thread_time(s),process_time(s)\n")
        for n_jobs, thread, process in results:
            f.write(f"{n_jobs},{thread:.5f},{process:.5f}\n")

if __name__ == "__main__":
    main()