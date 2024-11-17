import asyncio

from tellrcon import TellRCon
from logger import Logger

IP = str(input("Enter IP address of RCON >> "))
PORT = int(input("Enter port of RCON >> "))
PASSWORD = str(input("Enter password of RCON >> "))
COMMAND = str(input("Enter command >> "))


LOG = Logger()

rcon = TellRCon(IP, PORT, PASSWORD)
rcon.set_command(COMMAND)

if __name__ == '__main__':
    err: bool = False

    try:
        LOG.info(asyncio.run(rcon.ask_rcon()))
    except:
        LOG.fatal("Connection error")
        err = True

    if err is False:
        while True:
            COMMAND = str(input("Enter command >> "))
            rcon.set_command(COMMAND)
            LOG.info(asyncio.run(rcon.ask_rcon()))
