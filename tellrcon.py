from rcon.source import rcon
from api.sfs_colorama import TextColor, TextStyle


class TellRCon:
    def __init__(self, ip: str, port: int, password: str, command: str = None):
        self.ip = ip
        self.port = port
        self.command = command
        self.password = password

    def get_ip(self) -> str:
        return self.ip

    def get_port(self) -> int:
        return self.port

    def get_password(self) -> str:
        return self.password

    def get_command(self) -> str:
        return self.command

    def add_command(self, command: str) -> None:
        self.command = command

    def mc_formating(self, text: str) -> str:
        return (text
                .replace("§0", TextColor.BLACK)
                .replace("§1", TextColor.BLUE)
                .replace("§2", TextColor.GREEN)
                .replace("§3", TextColor.CYAN)
                .replace("§4", TextColor.RED)
                .replace("§5", TextColor.MAGENTA)
                .replace("§6", TextColor.YELLOW)
                .replace("§7", TextColor.LIGHT_GRAY)
                .replace("§8", TextColor.DEFAULT)
                .replace("§9", TextColor.LIGHT_BLUE)

                .replace("§a", TextColor.LIGHT_GREEN)
                .replace("§b", TextColor.LIGHT_CYAN)
                .replace("§c", TextColor.LIGHT_RED)
                .replace("§d", TextColor.LIGHT_MAGENTA)
                .replace("§e", TextColor.LIGHT_YELLOW)
                .replace("§f", TextColor.WHITE)

                .replace("§l", TextStyle.BOLD)
                .replace("§n", TextStyle.UNDERLINE)
                .replace("§r", TextStyle.OFF_ALL_STYLES)

                + TextColor.DEFAULT
                + TextStyle.OFF_ALL_STYLES)

    async def ask_rcon(self) -> str:
        return f"{TextColor.CYAN}[INFO]:{TextColor.DEFAULT} " + self.mc_formating(await rcon(
            self.command,
            host=self.ip, port=self.port, passwd=self.password
        ))
