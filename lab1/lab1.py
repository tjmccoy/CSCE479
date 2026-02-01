import time as t
import random as r

def cpu_intensive_task(iterations):
    res = 1
    for i in range(1, iterations):
        res += i
    return res

def perf_counter_test(target):
    start = t.perf_counter_ns()
    cpu_intensive_task(target)
    end = t.perf_counter_ns()
    return end - start, target

def process_time_test(target):
    start = t.process_time_ns()
    cpu_intensive_task(target)
    end = t.process_time_ns()
    return end - start, target

def thread_time_test(target):
    start = t.thread_time_ns()
    cpu_intensive_task(target)
    end = t.thread_time_ns()
    return end - start, target

def main():
    target = r.randint(100_000, 500_000)
    perf_time, perf_target = perf_counter_test(target)
    process_time, process_target = process_time_test(target)
    thread_time, thread_target = thread_time_test(target)
    
    print(f"Performance Counter Test: \n"
          f"Target iterations: {perf_target}\n"
          f"Time taken using perf_counter_ns: {perf_time} nanoseconds.\n")

    print(f"Process Time Test: \n"
          f"Target iterations: {process_target}\n"
          f"Time taken using process_time_ns: {process_time} nanoseconds.\n")

    print(f"Thread Time Test: \n"
          f"Target iterations: {thread_target}\n"
          f"Time taken using thread_time_ns: {thread_time} nanoseconds.")
    
    print()

if __name__ == "__main__":
    main()