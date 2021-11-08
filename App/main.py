from asyncio.events import AbstractEventLoop
import time
import webbrowser
import pyautogui
from mouseEvents import ClickService
from screenEvents import ScreenService
from workersService import worker
from loginService import login
from registerServices import Register
import config as c

class main:
    def start():
        if webbrowser.open_new_tab(c.main_url) :
                time.sleep(30)
        while True: 

            print("start")
            #step - 1
            count = 0
            print("step - 1 - Waiting click button: " + c.login_play_now_button)
            while pyautogui.locateOnScreen(c.login_play_now_button) is None :
                print("tries = ", count)
                count += 1
                if count > 100 :
                    break
                time.sleep(5)        
            count = 0

            print("step - 1 - trying click button: " + c.login_play_now_button)
            while pyautogui.locateOnScreen(c.login_play_now_button) is not None :
                count += 1
                print("tries = " , count)
                while pyautogui.locateOnScreen(c.login_connect_wallet_button) is None :
                    count += 1
                    ClickService.executeOnscreen(pyautogui.locateOnScreen(c.login_play_now_button))
                if count > 100 :
                    break
                time.sleep(10)        
            count = 0

            #login start
            print("login - start ->")
            while pyautogui.locateOnScreen(c.start_farm_treasure_image) is None or pyautogui.locateOnScreen(c.login_connect_wallet_button) is not None:
                count += 1
                print("tries : ", count)
                if(login.start(count)):
                    break
                time.sleep(60)
            print("login - Done")

            print("waiting heroe button ->")
            while pyautogui.locateOnScreen(c.worker_heroes_button) is None :
                count += 1
                print("tries : ", count)
                if(count > 10):
                    break
                time.sleep(10)
            count = 0

            print("choose workers - start ->")
            #choose workers
            if pyautogui.locateOnScreen(c.worker_heroes_button) is not None :
                ClickService.executeOnscreen(pyautogui.locateOnScreen(c.worker_heroes_button, confidence = 0.7))
                if worker.findWorkers():
                    time.sleep(10)
                    ClickService.executeOnscreen(pyautogui.locateOnScreen(c.start_farm_treasure_image, confidence = 0.7))
                    time.sleep(1)
                print("choose workers - DONE")

            #wait for
            print("wait stamina end - start ->")
            time.sleep(1) # TODO increase first sleep after tests
            while count < 100:
                printScreen = pyautogui.screenshot()
                time.sleep(100)
                if ScreenService.checkStoppedScreen(printScreen) :
                    break
                count += 1
                print("sleep in minutes : ", count*60)
                if count > 10 :
                    break
            print("restart : ")
            count = 0
    Register.register(loop=AbstractEventLoop)
    start()