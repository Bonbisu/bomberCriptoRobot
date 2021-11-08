import asyncio

import os
from screenEvents import ScreenService
from errorEvents import ErrorService

class Register:
    def register(loop) -> None:
        tasks = [ErrorService.CallBack(),ScreenService.CallBack()]
        asyncio.gather(*tasks)
        loop = asyncio.get_event_loop()
        for t in tasks:
            task_function = asyncio.ensure_future(t)
            loop.run_forever