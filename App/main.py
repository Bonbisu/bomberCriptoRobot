import time
import webbrowser
import pyautogui
from worker import worker
from login import login
import config as c
import random

class Checker :
        def Screen():
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
                time.sleep(5)

        print("step - 1 - Waiting click button: " + c.login_play_now_button)

        while pyautogui.locateOnScreen(c.login_play_now_button, confidence = 0.9) is None and count < 10 :
            print("login_play_now_button - tries = ", count)
            count += 1
            time.sleep(5)        
            if pyautogui.locateOnScreen(c.general_back_button, confidence = 0.99) is not None :
                break
        count = 0

        while True:
            print("start")
            #step - 1
            Checker.Screen()

            #if is logged, back to options screen
            while pyautogui.locateOnScreen(c.general_back_button, confidence = 0.99) is not None and count < 10 :
                pyautogui.leftClick(pyautogui.locateOnScreen(c.general_back_button, confidence = 0.8))
                count += 1
                print("general_back_button - tries = ", count)
                time.sleep(0.5)        
            count += 1

            if pyautogui.locateOnScreen(c.general_back_button, confidence = 0.99):
                pyautogui.keyDown('f5')
                time.sleep(5) 

            Checker.Screen()
            #click play now on home page
            while pyautogui.locateOnScreen(c.login_play_now_button, confidence = 0.7) is not None and count < 2 :
                pyautogui.leftClick(pyautogui.locateOnScreen(c.login_play_now_button))
                if pyautogui.locateOnScreen(c.start_farm_treasure_image, confidence = 0.8) is not None :
                    break
                count += 1
                print("login_play_now_button tries = " , count)

                while pyautogui.locateOnScreen(c.login_connect_wallet_button, confidence = 0.99) is None and count < 2 :
                    count += 1
                    pyautogui.leftClick(pyautogui.locateOnScreen(c.login_play_now_button))
                time.sleep(1)        
            count = 0

            #login start
            print("login - start ->")
            Checker.Screen()
            
            while pyautogui.locateOnScreen(c.login_connect_wallet_button, confidence = 0.7) is not None  and pyautogui.locateOnScreen(c.start_farm_treasure_image, confidence = 0.99) is None and count < 10:
                print("login_connect_wallet_button tries : ", count)
                count += 1
                if login.start() is True:
                    break
                time.sleep(1)
            count = 0
            print("login - Done")

            print("waiting heroes button ->")
            Checker.Screen()
            while pyautogui.locateOnScreen(c.worker_heroes_button, confidence = 0.7) is None and count < 10:
                count += 1
                print("tries : ", count)
                time.sleep(1)
            count = 0

            print("choose workers - start ->")
            Checker.Screen()
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

                #sleep 10 - 20 min
                while count < 25:
                    print("sleeping --> ", count)
                    time.sleep(5 + random.randrange(5,10,2))
                    Checker.Screen()
                    time.sleep( random.randrange(1,10,2))
                    count += 1
                    time.sleep(5 + random.randrange(5,10,2))
                
                #restart screen to provente heroes not putting bomb ( bug)
                while count < count +10 and pyautogui.locateOnScreen(c.general_back_button, confidence = 0.7):
                    count += 1
                    pyautogui.leftClick(pyautogui.locateOnScreen(c.general_back_button, confidence = 0.8))
                
                #back to farm
                while count < count +10 and pyautogui.locateOnScreen(c.start_farm_treasure_image, confidence = 0.7):
                    count += 1
                    pyautogui.leftClick(pyautogui.locateOnScreen(c.start_farm_treasure_image, confidence = 0.7))

                #sleep ~1h
                while count < 150 :
                    Checker.Screen()
                    print("sleeping --> ", count,)
                    time.sleep(random.randrange(15,20,1))
                    count += 1
            print("restart : ")
            count = 0
    start()