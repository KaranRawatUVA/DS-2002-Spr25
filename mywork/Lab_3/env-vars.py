#!/bin/env /usr/bin/python3

import os



FAV_TEAM = input('What is your favorite sports team? ')
FAV_PLAYER = input('Who is your favorite athlete? ')
FAV_SPORT = input('What is your favorite sport? ')

os.environ["FAV_TEAM"] = FAV_TEAM
os.environ["FAV_PLAYER"] = FAV_PLAYER
os.environ["FAV_SPORT"] = FAV_SPORT

print(os.getenv("FAV_TEAM"))
print(os.getenv("FAV_PLAYER"))
print(os.getenv("FAV_SPORT"))
