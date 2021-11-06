import webbrowser
import pyautogui
from mouseEvents import ClickService
from screenEvents import ScreenService
import config as c
import time
import random


def retry(retries, imgAddress, clicker, screen):
    if retries > 10:
        print("Passo : Retry - ", retries)
        return False
    else:
        while retries <= 10 and screen.checkExist():
            print("Passo : loop para clicar ", retries)
            time.sleep(.2)
            if imgAddress != c.imagePath + 'work_button.png':
                if clicker.executeOnscreen() is not False:
                    break
            else:
                if clicker.findWorkers() is not False:
                    break
            print("Tentativa de Clicar = @ tentativas ", retries)
            print("Tentativa de Clicar = @ tentativas " + imgAddress)
            retries += 1
            time.sleep(.2)
    if screen.checkExist() is True:
        time.sleep(1)
        print("Tela Travada - Tentativas = ", retries)
        print("Tela Travada" + imgAddress)
        return retry(1+retries, imgAddress, clicker, screen)
    return True


def lockRobot(executionLockTimer):
    time.sleep(.2)
    if executionLockTimer >= 0 and executionLockTimer <= 7200:
        print("Locked")
        return True
    print("Unlocked")
    return False


def loopExecution(executionLockTimer):
    webbrowser.open_new_tab("https://bombcrypto.io/")
    addSeconds = random.randint(1, 8)
    screen = ScreenService('')
    waitTimer = 5
    clicker = ClickService(None, '', 15)
    retries = 0

    print("iniciando")

    if screen.checkError() is True:
        clicker.update(None, c.errorButtonImage, 1)
        if(retry(retries, c.newMapButtonImage, clicker, screen)):
            print("checkError : @img -", c.errorButtonImage)
            executionLockTimer += addSeconds

    if screen.checkNewMap(waitTimer) is True:
        clicker.update(None, c.newMapButtonImage, 1)
        if(retry(retries, c.newMapButtonImage, clicker, screen)):
            print("checkNewMap : @img - OK", c.newMapButtonImage)

    for imgAddress in c.imageAddresses:
        try:
            clicker.update(None, imgAddress, 2)
            screen.update(imgAddress)
            loaders = 0
            while screen.checkExist() is not True:
                print("checkExist : @img - OK", imgAddress)
                time.sleep(3.5)
                loaders += 1
                if loaders > 10:
                    addSeconds = random.randint(60, 300)
                    time.sleep(addSeconds)
                    pyautogui.hotkey(c.closeTabCmd)
                    loopExecution(executionLockTimer)
            if(retry(retries, imgAddress, clicker, screen) is True):
                print("Tentativa : @img - OK", imgAddress)
            else:
                print("Passo Falhou", imgAddress)
        except:
            print("Passo - fail")
    while lockRobot(executionLockTimer) is True:
        addSeconds = random.randint(1, 8)
        executionLockTimer += addSeconds
        time.sleep(1)
        print("lock realizado por x @executionLockTimer ", executionLockTimer)
        if screen.checkError() is True or screen.checkNewMap(5) is True:
            time.sleep(1)
            break
    pyautogui.hotkey(c.closeTabCmd)
    loopExecution(executionLockTimer)


loopExecution(0)
