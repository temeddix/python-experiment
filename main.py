import asyncio
from asyncio import Future
from concurrent.futures import InterpreterPoolExecutor
from time import time
from helper import square


async def test_speed(max_workers: int):
    start_time = time()
    pool = InterpreterPoolExecutor(max_workers)
    loop = asyncio.get_running_loop()
    futures: list[Future[int]] = []
    for num in range(100):
        future = loop.run_in_executor(pool, square, num)
        futures.append(future)
    results = await asyncio.gather(*futures)
    result_sum = sum(results)
    time_taken = time() - start_time
    print(
        f"Max Workers: {max_workers}"
        f", Sum: {result_sum}"
        f", Time taken: {time_taken:.2f} seconds"
    )


async def main():
    for max_workers in (1, 2, 4, 8, 16, 32, 64):
        await test_speed(max_workers)


if __name__ == "__main__":
    asyncio.run(main())
