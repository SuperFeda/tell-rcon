import asyncio

from myrcon import MyRCon
from logger import Logger
from utils import mc_formating


def main():
    IP = str(input("Enter IP address of RCON >> "))
    PORT = int(input("Enter port of RCON >> "))
    PASSWORD = str(input("Enter password of RCON >> "))
    COMMAND = str(input("Enter command >> "))

    LOG = Logger()
    RCON = MyRCon(IP, PORT, PASSWORD)
    
    err: bool = False

    try:
        LOG.info(asyncio.run(RCON.ask(COMMAND)))
    except:
        LOG.fatal("Connection error")
        err = True

    if err is False:
        while True:
            COMMAND = str(input("Enter command >> "))
            LOG.info(mc_formating(asyncio.run(RCON.ask(COMMAND))))


if __name__ == '__main__':
    main()
