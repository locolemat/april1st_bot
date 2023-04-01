import os
import keyboard
import pywhatkit
import time
import random
import pyautogui
import ctypes
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
import requests
from PIL import Image
import pygame


def play_sound(sound):
    if sound == 'kurwa':
        pygame.mixer.init()
        pygame.mixer.music.load("kurwa.mp3")
        pygame.mixer.music.play()


def image_wallpaper(link):
    id = link.split('/')[-1]
    filename = f'image{id}.jpg'
    response = requests.get(link)
    with open(filename, "wb") as f:
        f.write(response.content)
    directory = os.path.dirname(os.path.realpath(__file__))
    wallpaper_path = os.path.join(directory, filename)
    os.system('REG ADD "HKCU\Control Panel\Desktop" /v Wallpaper /t REG_SZ /d "{}" /f'.format(wallpaper_path))
    os.system('RUNDLL32.EXE user32.dll,UpdatePerUserSystemParameters')

def image_download(link):
    id = link.split('/')[-1]
    filename = f'image{id}.jpg'
    response = requests.get(link)
    with open(filename, "wb") as f:
        f.write(response.content)
    image = Image.open(filename)
    image.show()



def change_volume(vol):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        ISimpleAudioVolume._iid_, ctypes.CLSCTX_ALL, None)
    interface.SetMasterVolume(vol, None)

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