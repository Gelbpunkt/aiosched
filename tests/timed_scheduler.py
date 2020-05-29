import asyncio
import sys

from datetime import datetime, timedelta

sys.path.insert(0, ".")

from aioscheduler import TimedScheduler


async def work(n: int) -> None:
    await asyncio.sleep(5)
    print(f"I am doing heavy work: {n}")


async def main() -> None:
    starting_time = datetime.utcnow()
    scheduler = TimedScheduler()
    scheduler.start()
    tasks = []

    for i in range(60):
        tasks.append(
            scheduler.schedule(work(i), starting_time + timedelta(seconds=5 + i))
        )

    while True:
        print(scheduler.cancel(tasks[10]))
        del tasks[10]
        await asyncio.sleep(5)


asyncio.run(main())
