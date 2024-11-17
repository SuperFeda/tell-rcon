from api.sfs_colorama import TextColor


class Logger:
    def __init__(self):
        super().__init__()

    def info(self, message: str) -> None:
        print(f"{TextColor.CYAN}[INFO]:{TextColor.DEFAULT} " + message)

    def error(self, message: str) -> None:
        print(f"{TextColor.YELLOW}[ERROR]:{TextColor.DEFAULT} " + message)

    def fatal(self, message: str) -> None:
        print(f"{TextColor.LIGHT_RED}[FATAL]:{TextColor.DEFAULT} " + message)
