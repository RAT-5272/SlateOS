"""


│
│
┌—————————————————————————————————————————
|                                        |
|                                        |
|                Current                 |
|                 open                   |
|                window                  |
|                                        |
|                                        |
|Taskbar e.g. slatelink, settings, login |
——————————————————————————————————————————


"""

BOX_DRAWING_CHARACTERS = {
    "Heavy": {
        "Vertical": "┃",
        "Horizontal": "━",
        "TopLeft": "┏",
        "TopRight": "┓",
        "BottomLeft": "┗",
        "BottomRight": "┛",
        "VerticalTLeft": "┣",
        "VerticalTRight": "┫",
        "VerticalTUp": "┻",
        "VerticalTDown": "┳",
        "Cross": "╋"
    },
    "Light": {
        "Vertical": "│",
        "Horizontal": "─",
        "TopLeft": "┌",
        "TopRight": "┐",
        "BottomLeft": "└",
        "BottomRight": "┘",
        "VerticalTLeft": "├",
        "VerticalTRight": "┤",
        "VerticalTUp": "┴",
        "VerticalTDown": "┬",
        "Cross": "┼"
    },
    "Round": {
        "Vertical": "│",
        "Horizontal": "─",
        "TopLeft": "╭",
        "TopRight": "╮",
        "BottomLeft": "╰",
        "BottomRight": "╯",
        "VerticalTLeft": "├",
        "VerticalTRight": "┤",
        "VerticalTUp": "┴",
        "VerticalTDown": "┬",
        "Cross": "┼"
    }
}


class WindowManager:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def PrintCurrentWindow(self):
        print(BOX_DRAWING_CHARACTERS["Heavy"]["TopLeft"] + BOX_DRAWING_CHARACTERS["Heavy"]["Horizontal"] * self.width + BOX_DRAWING_CHARACTERS["Heavy"]["TopRight"])
        print(f'{BOX_DRAWING_CHARACTERS["Heavy"]["Vertical"]}{' '*self.width}{BOX_DRAWING_CHARACTERS["Heavy"]["Vertical"]}\n'*self.height, end="")
        print(BOX_DRAWING_CHARACTERS["Heavy"]["VerticalTLeft"] + BOX_DRAWING_CHARACTERS["Heavy"]["Horizontal"] * self.width + BOX_DRAWING_CHARACTERS["Heavy"]["VerticalTRight"])
        print(BOX_DRAWING_CHARACTERS["Heavy"]["Vertical"] + " " * self.width + BOX_DRAWING_CHARACTERS["Heavy"]["Vertical"])
        print(BOX_DRAWING_CHARACTERS["Heavy"]["BottomLeft"] + BOX_DRAWING_CHARACTERS["Heavy"]["Horizontal"] * self.width + BOX_DRAWING_CHARACTERS["Heavy"]["BottomRight"])
        print("  SlateLink | Settings | Blackjack")
        
windowManager = WindowManager(64, 12)
windowManager.PrintCurrentWindow()