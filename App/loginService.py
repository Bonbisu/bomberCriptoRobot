import asyncio
import pyautogui
import config as c
from retryService import tries
import os
import time

class login:
    def start(count) -> bool :
        #passo - 2
        buttonsClicked = False
        while buttonsClicked is False:
            while pyautogui.locateOnScreen(c.login_connect_wallet_button, confidence=.95) is not None :
                count += 1
                buttonsClicked = tries.execute(count,c.login_connect_wallet_button)
                if buttonsClicked:
                    print("click true in image : " + c.login_connect_wallet_button)
                    break
                if count > 20:
                    print("click False in image : " + c.login_connect_wallet_button)
                    buttonsClicked =  False
                    break 
            print("click " + str(buttonsClicked) + " in image : " + c.login_connect_wallet_button)
            time.sleep(5)
            

            #passo - 3.1
            while pyautogui.locateOnScreen(c.login_metamask_light_button, confidence=.95) is not None :
                count += 1
                buttonsClicked = tries.execute(count,c.login_metamask_light_button)
                if buttonsClicked:
                    break
                if count > 20:
                    buttonsClicked =  False
                    break
            print("click " + str(buttonsClicked) + " in image : " + c.login_metamask_light_button)
            time.sleep(5)
            

            #passo - 3.2

            while  pyautogui.locateOnScreen(c.login_metamask_dark_button, confidence=.95) is not None:
                count += 1
                buttonsClicked = tries.execute(count,c.login_metamask_dark_button)
                if buttonsClicked:
                    break
                if count > 20:
                    buttonsClicked =  False
                    break
            print("click " + str(buttonsClicked) + " in image : " + c.login_metamask_dark_button)
            time.sleep(5)

            #passo - 4
            while pyautogui.locateOnScreen(c.login_assinar_button, confidence=.7) is not None :
                count += 1
                buttonsClicked = tries.execute(count,c.login_assinar_button)                
                if buttonsClicked:
                    break
                if count > 20:
                    buttonsClicked =  False
                    break
            print("click " + str(buttonsClicked) + " in image : " + c.login_assinar_button)
            time.sleep(5)

        return buttonsClicked
    # start(0) # <<<<< teste
                                

                



