# MorixOS 
A Python Console Operating System Simulation

MorixOS is a Windows-style operating system simulation written in Python.

It runs entirely in the terminal and provides a simple login system, built-in apps, and the ability to launch real Windows programs via file paths.

This project is for learning and fun purposes only. It is not a real operating system.

# Features

User login & password system

Boot sequence simulation

Calculator (supports 2–5 numbers)

Timer

Game launcher (starts real .exe files)

Fake bank application

Browser launcher

Windows-like console interface

Requirements

Python 3.10 or newer

Windows OS (required for os.startfile())

# User System

On first start, MorixOS will ask for a username and password

Login data is stored locally in:

os_data.txt


On the next launch, you must log in with your password

# Available Commands
morix/help	Show all commands

morix/off	Shut down MorixOS

morix/calculator	Open calculator

morix/timer	Start a timer

morix/games	Open game launcher

morix/bank	Open bank app

morix/browser	Launch browser

# Adding Games

MorixOS can launch real Windows applications using absolute paths.

Example:
if game == "Game Name":
    os.startfile(r"C:\Program Files\Game\game.exe")

# Steps:

Replace "Game Name" with the name you want to type in MorixOS

Replace the path with the full path to the .exe file

You can add multiple games using elif

# Browser Path

The browser launcher also uses a hardcoded path.

Example:
os.startfile(r"C:\Program Files\Google\Chrome\Application\chrome.exe")


Replace the path with your installed browser location.
