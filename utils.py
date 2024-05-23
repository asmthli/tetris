import time


def average_run_timer(func):
    cumulative_time = 0
    times_recorded = 0

    def wrapper(*args):
        nonlocal cumulative_time, times_recorded
        before = time.time()
        output = func(*args)
        delta = time.time() - before

        cumulative_time += delta
        times_recorded += 1

        if times_recorded == 30:
            avg_time = cumulative_time / times_recorded
            print(f"Avg time for {func.__name__} over {times_recorded} runs: {avg_time * 1000:.1f}ms")
            cumulative_time = 0
            times_recorded = 0

        return output

    return wrapper
