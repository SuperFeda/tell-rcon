from rcon.source import rcon


class MyRCon:
    def __init__(self, ip: str, port: int, password: str):
        self.ip = ip
        self.port = port
        self.password = password

    def get_ip(self) -> str:
        return self.ip

    def get_port(self) -> int:
        return self.port

    def get_password(self) -> str:
        return self.password

    def change_ip(self, ip: str) -> None:
        self.ip = ip

    def change_port(self, port: int) -> None:
        self.port = port

    def change_password(self, password: str) -> None:
        self.password = password

    async def ask(self, command: str) -> str:
        return await rcon(
            command,
            host=self.ip, port=self.port, passwd=self.password
        )
