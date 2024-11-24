from api.sfs_colorama import TextColor, TextStyle


mc_colors = {
    "§0": TextColor.BLACK,
    "§1": TextColor.BLUE,
    "§2": TextColor.GREEN,
    "§3": TextColor.CYAN,
    "§4": TextColor.RED,
    "§5": TextColor.MAGENTA,
    "§6": TextColor.YELLOW,
    "§7": TextColor.LIGHT_GRAY,
    "§8": TextColor.DEFAULT,
    "§9": TextColor.LIGHT_BLUE,

    "§a": TextColor.LIGHT_GREEN,
    "§b": TextColor.LIGHT_CYAN,
    "§c": TextColor.LIGHT_RED,
    "§d": TextColor.LIGHT_MAGENTA,
    "§e": TextColor.LIGHT_YELLOW,
    "§f": TextColor.WHITE,

    "§l": TextStyle.BOLD,
    "§n": TextStyle.UNDERLINE,
    "§r": TextStyle.OFF_ALL_STYLES,
}


def mc_formating(text: str) -> str:
    for key, value in mc_colors.items():
        text = text.replace(key, value)

    return text + TextColor.DEFAULT + TextStyle.OFF_ALL_STYLES
