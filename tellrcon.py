from rcon.source import rcon


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

    def set_command(self, command: str) -> None:
        self.command = command

    async def ask_rcon(self) -> str:
        return await rcon(
            self.command,
            host=self.ip, port=self.port, passwd=self.password
        )
