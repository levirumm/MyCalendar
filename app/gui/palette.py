PALETTE = {
    "blue": {
        "lightest": "#ebf8fc",
        "light": "#CFECF7",
        "base": "#aaddf0",
        "dark": "#81c3db",
        "darkest": "#438da8"
    },

    "gray": {"base": "#434343"}, 

    # Button colors
    "red": "#cf4c4c",
    "orange": "#edb253",
    "yellow": "#ece24e",
    "green": "#6fd35f",
    "purple": "#a975c7",
    "pink": "#c75598",
}


BUTTON_COLORS: dict[str, str] = {
    "light_blue": PALETTE["blue"]["light"],
    "base_blue": PALETTE["blue"]["base"],
    "dark_blue": PALETTE["blue"]["dark"],
    "darkest_blue": PALETTE["blue"]["darkest"],
    
    "white": "#FFFFFF",

    "red": PALETTE["red"],
    "orange": PALETTE["orange"],
    "yellow": PALETTE["yellow"],
    "green": PALETTE["green"],
    "purple": PALETTE["purple"],
    "pink": PALETTE["pink"]
}


CLASS_COLORS: list[str] = [
    "red", "orange", "yellow", 
    "green", "dark_blue", "darkest_blue", 
    "purple", "pink"
]