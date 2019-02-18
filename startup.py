# author: Francisco J Lopez
# date: 2/18/2019

import pyautogui
import time


def run():

    try:
        homePoint = ()
        homeFound = go_home(homePoint)

        chromeLoc = pyautogui.locateOnScreen('chrome.png')
        chromePoint = pyautogui.center(chromeLoc)
        chromeX, chromeY = chromePoint
        pyautogui.moveTo(chromeX, chromeY)
        pyautogui.click(clicks=2)

        time.sleep(2)
        pyautogui.click()

        searchLoc = pyautogui.locateOnScreen('Search.png')
        searchPoint = pyautogui.center(searchLoc)
        searchX, searchY = searchPoint
        pyautogui.moveTo(searchX, searchY)
        pyautogui.click()
        pyautogui.typewrite('youtube.com')
        pyautogui.press('enter')

        time.sleep(3)
        youtubeLoc = pyautogui.locateOnScreen('youtube-search.PNG')
        youtubePoint = pyautogui.center(youtubeLoc)
        youX, youY = youtubePoint
        pyautogui.click(youX, youY)
        pyautogui.typewrite('lofi kpop')
        pyautogui.press('enter')

        time.sleep(1)
        lofiLoc = pyautogui.locateOnScreen('lofi-kpop.PNG')
        lofiPoint = pyautogui.center(lofiLoc)
        lofiX , lofiY = lofiPoint
        pyautogui.click(lofiX, lofiY)

        time.sleep(3)
        pyautogui.click()
        go_home(homeFound)

        time.sleep(1)
        rustLoc = pyautogui.locateOnScreen('rust.PNG')
        rustPoint = pyautogui.center(rustLoc)
        rustX, rustY = rustPoint
        pyautogui.click(rustX, rustY, clicks=2)


        time.sleep(30)
        playLoc = pyautogui.locateOnScreen('rustPlay.PNG')
        playPoint = pyautogui.center(playLoc)
        playX, playY = playPoint
        pyautogui.click(playX, playY)

        time.sleep(25)
        pyautogui.press('win')
        pyautogui.click()

        # rust requires to runs of go_home for it to actually go home
        go_home(homeFound)
        go_home(homeFound)

    except:
        pyautogui.alert('This program has encountered an error when looking for an image')


def go_home(homePoint):

    if homePoint == ():
        homeLoc = pyautogui.locateOnScreen('windows.PNG')
        homePoint = pyautogui.center(homeLoc)
    homeX, homey = homePoint
    pyautogui.moveTo(homeX, homey)
    pyautogui.click(button='right')
    pyautogui.click()
    return homePoint


run()
