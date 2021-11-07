import asyncio

import os
from loopExecution import loopExecution

from errorEvents import ErrorService

class Register:
    async def register(loop) -> None:
        tasks = [ErrorService.CallBack()]
        asyncio.gather(*tasks)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(register(loop))
        


        


        
    