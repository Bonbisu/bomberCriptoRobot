from asyncio.events import AbstractEventLoop
import time
import webbrowser
import pyautogui
#from mouseEvents import ClickService
from screenEvents import ScreenService
from workersService import worker
from loginService import login
from registerServices import Register
import config as c

class main:
    def start():
        count = 0

        if webbrowser.open_new_tab(c.main_url) :
                time.sleep(5)

        print("step - 1 - Waiting click button: " + c.login_play_now_button)

        while pyautogui.locateOnScreen(c.login_play_now_button, confidence = 0.7) is None and count < 100 :
            print("tries = ", count)
            count += 1
            time.sleep(5)        
        count = 0

        while True:
            print("start")
            #step - 1

            if pyautogui.locateOnScreen(c.general_back_button, confidence = 0.7) is not None :
                while pyautogui.locateOnScreen(c.general_back_button, confidence = 0.7) is not None and count < 10 :
                    pyautogui.leftClick(pyautogui.locateOnScreen(c.general_back_button))
                    print("tries = ", count)
                    count += 1
                    time.sleep(5)        
                count = 0

            print("step - 1 - trying click button: " + c.login_play_now_button)
            
            while pyautogui.locateOnScreen(c.login_play_now_button, confidence = 0.7) is not None and count < 10 :
                count += 1
                print("tries = " , count)

                while pyautogui.locateOnScreen(c.login_connect_wallet_button, confidence = 0.7) is None and count < 10 :
                    count += 1
                    pyautogui.leftClick(pyautogui.locateOnScreen(c.login_play_now_button))
                time.sleep(10)        
            count = 0

            #login start
            print("login - start ->")
            
            while pyautogui.locateOnScreen(c.start_farm_treasure_image, confidence = 0.7) is None and count < 100:
                while pyautogui.locateOnScreen(c.login_connect_wallet_button, confidence = 0.7) is not None and count < 100:
                    print("tries : ", count)
                    count += 1
                    if login.start(count) is True:
                        count += 1
                    time.sleep(10)
            count = 0
            print("login - Done")

            print("waiting heroe button ->")
            
            while pyautogui.locateOnScreen(c.worker_heroes_button, confidence = 0.7) is None and count < 10:
                count += 1
                print("tries : ", count)
                time.sleep(10)
            count = 0

            print("choose workers - start ->")
            
            #choose workers
            if pyautogui.locateOnScreen(c.worker_heroes_button, confidence = 0.7) is not None and count < 100 :
                pyautogui.leftClick(pyautogui.locateOnScreen(c.worker_heroes_button, confidence = 0.7))
                if worker.findWorkers():
                    time.sleep(10)
                    pyautogui.leftClick(pyautogui.locateOnScreen(c.start_farm_treasure_image, confidence = 0.7))
                    time.sleep(1)
                else:
                    pyautogui.hotkey(c.closeTabCmd)

                while count < 60:
                    time.sleep(60)
                    count += 1

                print("sleep in minutes : ", count*65)

                print("choose workers - DONE")

            #wait for
            print("wait stamina end - start ->")
            time.sleep(1) # TODO increase first sleep after tests

            
            print("restart : ")
            count = 0

    Register.register(loop=AbstractEventLoop)
    start()