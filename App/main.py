import time
import webbrowser
import pyautogui
from workersService import worker
from loginService import login
import config as c
import random

class ErrorChecker :
        def ErrorChecker():
            if pyautogui.locateOnScreen(c.general_erro_center_modal,confidence=.8) is not None:
                print("general_erro_center_modal - tries = ")
                pyautogui.click(pyautogui.locateOnScreen(c.general_error_button,confidence=.8))
            time.sleep(1)

            if pyautogui.locateOnScreen(c.general_error_button,confidence=.8) is not None:
                print("general_error_button - tries = ")
                pyautogui.click(pyautogui.locateOnScreen(c.general_erro_center_modal,confidence=.8))
            time.sleep(1)

            if pyautogui.locateOnScreen(c.general_error_header_modal,confidence=.8) is not None:
                print("general_error_header_modal - tries = ")
                pyautogui.click(pyautogui.locateOnScreen(c.general_erro_center_modal,confidence=.8))
            time.sleep(1)

            if pyautogui.locateOnScreen(c.general_new_map_button,confidence=.8) is not None:
                print("general_new_map_button - tries = ")
                pyautogui.click(pyautogui.locateOnScreen(c.general_new_map_button,confidence=.8))
            time.sleep(1)

            if pyautogui.locateOnScreen(c.general_new_map_cartoon,confidence=.8) is not None:
                print("general_new_map_cartoon - tries = ")
                pyautogui.click(pyautogui.locateOnScreen(c.general_new_map_button,confidence=.8))
            time.sleep(1)

class main:

    def start():
        count = 0

        if webbrowser.open_new_tab(c.main_url) :
                time.sleep(1)

        print("step - 1 - Waiting click button: " + c.login_play_now_button)

        while pyautogui.locateOnScreen(c.login_play_now_button, confidence = 0.7) is None and count < 10 :
            print("login_play_now_button - tries = ", count)
            count += 1
            time.sleep(5)        
            if pyautogui.locateOnScreen(c.general_back_button, confidence = 0.8) is not None :
                break
        count = 0

        while True:
            print("start")
            #step - 1
            ErrorChecker.ErrorChecker()

            while pyautogui.locateOnScreen(c.general_back_button, confidence = 0.8) is not None and count < 10 :
                pyautogui.leftClick(pyautogui.locateOnScreen(c.general_back_button, confidence = 0.8))
                count += 1
                print("general_back_button - tries = ", count)
                time.sleep(0.5)        
            count += 1

            if pyautogui.locateOnScreen(c.general_back_button, confidence = 0.8):
                pyautogui.keyDown('f5')
                time.sleep(5) 

            print("step - 1 - trying click button: " + c.login_play_now_button)
            ErrorChecker.ErrorChecker()
            while pyautogui.locateOnScreen(c.login_play_now_button, confidence = 0.7) is not None and count < 2 :
                if pyautogui.locateOnScreen(c.start_farm_treasure_image, confidence = 0.8) is not None :
                    break
                count += 1
                print("tries = " , count)

                while pyautogui.locateOnScreen(c.login_connect_wallet_button, confidence = 0.7) is None and count < 2 :
                    count += 1
                    pyautogui.leftClick(pyautogui.locateOnScreen(c.login_play_now_button))
                time.sleep(1)        
            count = 0

            #login start
            print("login - start ->")
            ErrorChecker.ErrorChecker()
            
            while pyautogui.locateOnScreen(c.login_connect_wallet_button, confidence = 0.7) is not None  and pyautogui.locateOnScreen(c.start_farm_treasure_image, confidence = 0.99) is None and count < 10:
                print("tries : ", count)
                count += 1
                if login.start(count) is True:
                    break
                time.sleep(1)
            count = 0
            print("login - Done")

            print("waiting heroe button ->")
            ErrorChecker.ErrorChecker()
            while pyautogui.locateOnScreen(c.worker_heroes_button, confidence = 0.7) is None and count < 10:
                count += 1
                print("tries : ", count)
                time.sleep(1)
            count = 0

            print("choose workers - start ->")
            ErrorChecker.ErrorChecker()
            #choose workers
            if pyautogui.locateOnScreen(c.worker_heroes_button, confidence = 0.7) is not None and count < 10 :
                pyautogui.leftClick(pyautogui.locateOnScreen(c.worker_heroes_button, confidence = 0.7))
                if worker.findWorkers():
                    time.sleep(1)
                    pyautogui.leftClick(pyautogui.locateOnScreen(c.start_farm_treasure_image, confidence = 0.7))
                    time.sleep(1)
                    print("choose workers - DONE")
                else:
                    pyautogui.hotkey(c.closeTabCmd)

                while count < 400 + random.randrange(100,200,2) :
                    print("sleeping --> ", count)
                    time.sleep(5 + random.randrange(5,10,2))
                    ErrorChecker.ErrorChecker()
                    time.sleep( random.randrange(1,10,2))
                    count += 1
            print("restart : ")
            count = 0
    start()