from api.sfs_colorama import TextColor, TextStyle


def mc_formating(text: str) -> str:
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
