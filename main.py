import asyncio
from asyncio import AbstractEventLoop, Future
from concurrent.futures import InterpreterPoolExecutor
from time import time

from helper import square

TASK_COUNT = 256


async def test_speed(
    max_workers: int,
    pool: InterpreterPoolExecutor,
    loop: AbstractEventLoop,
):
    start_time = time()
    futures: list[Future[int]] = []
    for num in range(TASK_COUNT):
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
    loop = asyncio.get_running_loop()
    for max_workers in (1, 2, 4, 8, 16, 32, 64):
        with InterpreterPoolExecutor(max_workers) as pool:
            await test_speed(max_workers, pool, loop)


if __name__ == "__main__":
    asyncio.run(main())
