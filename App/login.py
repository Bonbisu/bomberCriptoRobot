import pyautogui
import config as c
import time

class login:
    def start() -> bool :
        count = 0
        #passo - 2
        buttonsClicked = False
        #repetição de código pelos lags aleatórios do jogo.         
        while buttonsClicked is False:
            
            if pyautogui.locateOnScreen(c.login_connect_wallet_button, confidence=.8) is None:
                    print("click break in image : " + c.login_connect_wallet_button)
                    break
            count = 0
            while pyautogui.locateOnScreen(c.login_connect_wallet_button, confidence=.7) is not None :
                count += 1

                if pyautogui.locateOnScreen(c.login_metamask_light_button, confidence=.8) is not None:
                    print("click true in image : " + c.login_connect_wallet_button)
                    break

                time.sleep(1)
                buttonsClicked = pyautogui.leftClick(pyautogui.locateOnScreen(c.login_connect_wallet_button, confidence=.7))
                time.sleep(1)

                if buttonsClicked:
                    print("click true in image : " + c.login_connect_wallet_button)
                    break
                
                time.sleep(0.5)
                                                
                if count > 20:
                    print("click False in image : " + c.login_connect_wallet_button + " count > " + str(count))
                    buttonsClicked =  False
                    break
                
            count = 0
            print("click " + buttonsClicked.__str__() + " in image : " + c.login_connect_wallet_button)
            time.sleep(5)
            

            #passo - 3.1
            while pyautogui.locateOnScreen(c.login_metamask_light_button, confidence=.7) is not None :
                
                if pyautogui.locateOnScreen(c.login_assinar_button, confidence=.8) is not None :
                    break

                count += 1
                time.sleep(1)                
                buttonsClicked = pyautogui.leftClick(pyautogui.locateOnScreen(c.login_metamask_light_button, confidence=.7))
                time.sleep(1)                
                
                if buttonsClicked:
                    print("click true in image : " + c.login_metamask_light_button)
                    break
               
                if count > 20:
                    buttonsClicked =  False
                    print("click False in image : " + c.login_metamask_light_button + " count > " + str(count))
                    break

            count = 0
            print("click " + buttonsClicked.__str__() + " in image : " + c.login_metamask_light_button)
            time.sleep(5)            

            #passo - 3.2

            while pyautogui.locateOnScreen(c.login_metamask_dark_button, confidence=.7) is not None :
                
                if pyautogui.locateOnScreen(c.login_assinar_button, confidence=.8) is not None :
                    break

                time.sleep(1)                
                count += 1
                buttonsClicked = pyautogui.leftClick(pyautogui.locateOnScreen(c.login_metamask_dark_button, confidence=.7))                
                time.sleep(1)                
                
                if pyautogui.locateOnScreen(c.login_metamask_dark_button, confidence=.7) is None:
                    break 

                if buttonsClicked :
                    break
                
                if count > 20 :
                    buttonsClicked =  False
                    break

            print("click " + buttonsClicked.__str__() + " in image : " + c.login_metamask_dark_button)
            time.sleep(5)
            count = 0
            #passo - 4
            while pyautogui.locateOnScreen(c.login_assinar_button, confidence=.7) is not None :
         
                if pyautogui.locateOnScreen(c.start_farm_treasure_image, confidence = 0.7 ) is not None :
                    break

                if pyautogui.locateOnScreen(c.login_assinar_button, confidence = 0.7 ) is None :
                    break
         
                count += 1

                time.sleep(1)                
                buttonsClicked = pyautogui.leftClick(pyautogui.locateOnScreen(c.login_assinar_button, confidence=.7))                
                time.sleep(1)                
                
                if buttonsClicked:
                    break
                
                if count > 20:
                    buttonsClicked = False
                    break    
                
            print("click " + buttonsClicked.__str__() + " in image : " + c.login_assinar_button)
            time.sleep(1)                
            count = 0
        return buttonsClicked
    # start(0) # <<<<< teste
                                

                



