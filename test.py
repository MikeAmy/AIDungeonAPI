from aidadventure import AIDungeonAdventure
from aidclient import AIDungeonClient
import asyncio

async def callback(result):
    print(result)

async def blocking_task():
    while True:
        await asyncio.sleep(10)

async def main():
    pubid = "59a7ddbd-9746-4d40-9908-487e4f042c2f"
    aidc = await AIDungeonClient(debug=True)
    scenario = await aidc.connect_to_scenario('458627')
    prompt = await scenario.obtain_prompt()
    adventure_id = await aidc.create_adventure(scenario.id, prompt, {
        'character.name':'AIDAPI'
    })

asyncio.run(main())
