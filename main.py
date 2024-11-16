import asyncio

from tellrcon import TellRCon
from api.sfs_colorama import TextColor

IP: str = str(input("Enter IP address of RCON >> "))
PORT: int = int(input("Enter port of RCON >> "))
PASSWORD: str = str(input("Enter password of RCON >> "))
COMMAND: str = str(input("Enter command >> "))

ask = TellRCon(IP, PORT, PASSWORD)
ask.add_command(COMMAND)

if __name__ == '__main__':
    try:
        print(asyncio.run(ask.ask_rcon()))
    except:
        print(f"{TextColor.RED}Connection error{TextColor.DEFAULT}")

    while True:
        COMMAND: str = str(input("Enter command >> "))
        ask.add_command(COMMAND)
        print(asyncio.run(ask.ask_rcon()))
