import os
import keyboard
import pywhatkit
import time
import random
import pyautogui


def play_youtube_video(link, runtime):
    start_time = time.time()
    while time.time < start_time + runtime:
        time.sleep(1)
        pywhatkit.playonyt(link)


def open_terminal(runtime):
    runtime = 20 if runtime < 20 else runtime
    start_time = time.time()
    while time.time < start_time + runtime:
        time.sleep(1)
        keyboard.press('Win+R')
        cmd = 'cmd.exe'
        for i in cmd:
            time.sleep(0.5)
            keyboard.press(i)
        time.sleep(0.5)
        keyboard.press('Enter')


def press_space_at_random(runtime):
    runtime = 11 if runtime < 11 else runtime
    start_time = time.time()
    while time.time < start_time + runtime:
        time.sleep(random.randrange(2, 10))
        keyboard.press('space')


def chaotic_mouse_movement(runtime):
    runtime = 11 if runtime < 11 else runtime
    start_time = time.time()
    width, height = pyautogui.size()
    while time.time < start_time + runtime:
        time.sleep(random.randrange(2, 10))
        pyautogui.moveTo(random.randrange(width), random.randrange(height), duration=2.0)

def close_current_tab():
    keyboard.press("Ctrl+W")