import os
import random

def change_wallpaper():
    wallpapers=os.listdir("E:\Wallpaper")
    num = len(wallpapers)

    wallpaper=random.choices(wallpapers)
    print(wallpaper)

change_wallpaper()