#Задача "Асинхронные силачи"
import asyncio

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования')
    for i in range(1, 6):
        time = 1/power
        asyncio.sleep(time)
        print(f'Силач {name} поднял {i}')
    print(f'Силач {name} закончил соревнования')

async def start_tournament():
    task_1 = asyncio.create_task(start_strongman('Misha', 3))
    task_2 = asyncio.create_task(start_strongman('Vlad', 4))
    task_3 = asyncio.create_task(start_strongman('Innokentii', 5))
    await task_1
    await task_2
    await task_3

asyncio.run(start_tournament())