"""

┌—————————————————————————————————————————
|                                        |
|                                        |
|                Current                 |
|                 open                   |
|                window                  |
|                                        |
|————————————————————————————————————————|
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

class Line:
    def __init__(self, startX: int, startY: int, length: int, isVertical: bool):
        self.startX = startX
        self.startY = startY
        self.length = length
        self.isVertical = isVertical

class TextBox:
    def __init__(self, startX: int, startY: int, width: int, height: int, text: str, isEditable: bool = False):
        self.startX = startX
        self.startY = startY
        self.width = width
        self.height = height
        self.text = text
        self.isEditable = isEditable
        
class Window:
    def __init__(self):
        self.lines: dict[int, Line] = {}
        self.textBoxes: dict[int, TextBox] = {}

    def AddLine(self, startX: int, startY: int, length: int, isVertical: bool) -> int:
        ID = max(self.lines.keys(), default=0)
        self.lines[ID+1] = Line(round(startX), round(startY), round(length), isVertical)
        return ID

    def CreateBox(self, startX: int, startY: int, width: int, height: int) -> tuple[int, int, int, int]:
        startX, startY, width, height = round(startX), round(startY), round(width), round(height)
        ID1 = self.AddLine(startX, startY, width+1, False)
        ID2 = self.AddLine(startX+width+1, startY, height+2, True)
        ID3 = self.AddLine(startX, startY+height+1, width+2, False)
        ID4 = self.AddLine(startX, startY, height+1, True)
        return (ID1, ID2, ID3, ID4)

    def AddTextBox(self, startX: int, startY: int, width: int, height: int, text: str) -> int:
        ID = max(self.textBoxes.keys(), default=0)
        self.textBoxes[ID+1] = TextBox(round(startX), round(startY), round(width), round(height), text)
        return ID

class WindowManager:
    def __init__(self, width: int, height: int, detachedTaskbar: bool = False):
        self.width = width
        self.height = height
        self.openWindows = {"SlateLink": {}, "Settings": {}}
        self.lineStyle = "Round"
        self.detachedTaskbar = detachedTaskbar
        """
        {
            "SlateLink": {
                "Windows": {}
            }
        
        }
        """

    def RenderWindow(self, window: Window):
        windowContent = []
        for i in range(self.height):
            windowContent.append([" "] * self.width)

        for yCoord in range(self.height):
            for xCoord in range(self.width):
                for lineID in window.lines:
                    line = window.lines[lineID]
                    if line.startY > yCoord or line.startX > xCoord: continue
                    if line.startY != yCoord and line.startX != xCoord: continue

                    if line.isVertical:
                        if line.startX == xCoord and (line.startY + line.length) > yCoord:
                            windowContent[yCoord][xCoord] = BOX_DRAWING_CHARACTERS[self.lineStyle]["Vertical"]
                    else:
                        if line.startY == yCoord and (line.startX + line.length) > xCoord:
                            windowContent[yCoord][xCoord] = BOX_DRAWING_CHARACTERS[self.lineStyle]["Horizontal"]

        for textBoxID in window.textBoxes:
            textBox = window.textBoxes[textBoxID]

            text = textBox.text
            xCoord = textBox.startX
            yCoord = textBox.startY

            for character in text:
                if character == "\n":
                    xCoord = textBox.startX
                    yCoord += 1

                if xCoord >= (textBox.startX + textBox.width):
                    xCoord = textBox.startX
                    yCoord += 1

                if yCoord >= (textBox.startY + textBox.height):
                    continue

                if character != "\n":
                    windowContent[yCoord][xCoord] = character
                    xCoord += 1

        # Post Processing: Turn lines into corners
        for yCoord in range(self.height):
            for xCoord in range(self.width):
                # Get 3x3 grid of neighboring box draw characters (plus sign shaped)
                vertical = BOX_DRAWING_CHARACTERS[self.lineStyle]["Vertical"]
                horizontal = BOX_DRAWING_CHARACTERS[self.lineStyle]["Horizontal"]
                centre = windowContent[yCoord][xCoord]
                above = windowContent[yCoord-1][xCoord] if yCoord != 0 else " "
                left = windowContent[yCoord][xCoord-1] if xCoord != 0 else " "
                below = windowContent[yCoord+1][xCoord] if yCoord != self.height-1 else " "
                right = windowContent[yCoord][xCoord+1] if xCoord != self.width-1 else " "
                newCentre = None
                if (centre == vertical or centre == horizontal) and above == vertical and below == vertical and left == horizontal and right == horizontal: newCentre = "Cross"
                elif (centre == vertical or centre == horizontal) and above == vertical and below == vertical and left == horizontal and right != horizontal: newCentre = "VerticalTRight"
                elif (centre == vertical or centre == horizontal) and above == vertical and below == vertical and left != horizontal and right == horizontal: newCentre = "VerticalTLeft"
                elif (centre == vertical or centre == horizontal) and above == vertical and below != vertical and left == horizontal and right == horizontal: newCentre = "VerticalTUp"
                elif (centre == vertical or centre == horizontal) and above != vertical and below == vertical and left == horizontal and right == horizontal: newCentre = "VerticalTDown"
                elif (centre == vertical or centre == horizontal) and above != vertical and below == vertical and left != horizontal and right == horizontal: newCentre = "TopLeft"
                elif (centre == vertical or centre == horizontal) and above != vertical and below == vertical and left == horizontal and right != horizontal: newCentre = "TopRight"
                elif (centre == vertical or centre == horizontal) and above == vertical and below != vertical and left != horizontal and right == horizontal: newCentre = "BottomLeft"
                elif (centre == vertical or centre == horizontal) and above == vertical and below != vertical and left == horizontal and right != horizontal: newCentre = "BottomRight"
                if newCentre:
                    windowContent[yCoord][xCoord] = BOX_DRAWING_CHARACTERS[self.lineStyle][newCentre]


        firstRow = ""
        lastRow = ""
        for char in windowContent[0]:
            firstRow += BOX_DRAWING_CHARACTERS[self.lineStyle]["VerticalTDown"] if char == BOX_DRAWING_CHARACTERS[self.lineStyle]["Vertical"] or char == BOX_DRAWING_CHARACTERS[self.lineStyle]["BottomRight"] or char == BOX_DRAWING_CHARACTERS[self.lineStyle]["BottomLeft"] or char == BOX_DRAWING_CHARACTERS[self.lineStyle]["VerticalTLeft"] or char == BOX_DRAWING_CHARACTERS[self.lineStyle]["VerticalTRight"] or char == BOX_DRAWING_CHARACTERS[self.lineStyle]["VerticalTUp"] else BOX_DRAWING_CHARACTERS[self.lineStyle]["Horizontal"]
        for char in windowContent[-1]:
            lastRow += BOX_DRAWING_CHARACTERS[self.lineStyle]["VerticalTUp"] if char == BOX_DRAWING_CHARACTERS[self.lineStyle]["Vertical"] or char == BOX_DRAWING_CHARACTERS[self.lineStyle]["TopRight"] or char == BOX_DRAWING_CHARACTERS[self.lineStyle]["TopLeft"] or char == BOX_DRAWING_CHARACTERS[self.lineStyle]["VerticalTLeft"] or char == BOX_DRAWING_CHARACTERS[self.lineStyle]["VerticalTRight"] or char == BOX_DRAWING_CHARACTERS[self.lineStyle]["VerticalTDown"] else BOX_DRAWING_CHARACTERS[self.lineStyle]["Horizontal"]
        
        print(BOX_DRAWING_CHARACTERS[self.lineStyle]["TopLeft"] + firstRow + BOX_DRAWING_CHARACTERS[self.lineStyle]["TopRight"])
        
        for row in windowContent:
            rowString = ''.join(row)
            leftSide = BOX_DRAWING_CHARACTERS[self.lineStyle]["VerticalTLeft"] if rowString[0] == BOX_DRAWING_CHARACTERS[self.lineStyle]["Horizontal"] or rowString[0] == BOX_DRAWING_CHARACTERS[self.lineStyle]["VerticalTUp"] or rowString[0] == BOX_DRAWING_CHARACTERS[self.lineStyle]["VerticalTDown"] or rowString[0] == BOX_DRAWING_CHARACTERS[self.lineStyle]["TopRight"] or rowString[0] == BOX_DRAWING_CHARACTERS[self.lineStyle]["BottomRight"] or rowString[0] == BOX_DRAWING_CHARACTERS[self.lineStyle]["VerticalTRight"] else BOX_DRAWING_CHARACTERS[self.lineStyle]["Vertical"]
            rightSide = BOX_DRAWING_CHARACTERS[self.lineStyle]["VerticalTRight"] if rowString[-1] == BOX_DRAWING_CHARACTERS[self.lineStyle]["Horizontal"] or rowString[-1] == BOX_DRAWING_CHARACTERS[self.lineStyle]["VerticalTUp"] or rowString[-1] == BOX_DRAWING_CHARACTERS[self.lineStyle]["VerticalTDown"] or rowString[-1] == BOX_DRAWING_CHARACTERS[self.lineStyle]["TopLeft"] or rowString[-1] == BOX_DRAWING_CHARACTERS[self.lineStyle]["BottomLeft"] or rowString[-1] == BOX_DRAWING_CHARACTERS[self.lineStyle]["VerticalTLeft"] else BOX_DRAWING_CHARACTERS[self.lineStyle]["Vertical"]
            print(f'{leftSide}{''.join(row)}{rightSide}')
        
        allOpenWindows = self.openWindows.keys()
        openWindowsString = " | ".join(allOpenWindows)

        if self.detachedTaskbar:
            print(BOX_DRAWING_CHARACTERS[self.lineStyle]["BottomLeft"] + lastRow + BOX_DRAWING_CHARACTERS[self.lineStyle]["BottomRight"])
            print(BOX_DRAWING_CHARACTERS[self.lineStyle]["TopLeft"] + BOX_DRAWING_CHARACTERS[self.lineStyle]["Horizontal"] * self.width + BOX_DRAWING_CHARACTERS[self.lineStyle]["TopRight"])
        else:
            print(BOX_DRAWING_CHARACTERS[self.lineStyle]["VerticalTLeft"] + lastRow + BOX_DRAWING_CHARACTERS[self.lineStyle]["VerticalTRight"])
        print(BOX_DRAWING_CHARACTERS[self.lineStyle]["Vertical"] + f"{openWindowsString:^{self.width}}" + BOX_DRAWING_CHARACTERS[self.lineStyle]["Vertical"])
        print(BOX_DRAWING_CHARACTERS[self.lineStyle]["BottomLeft"] + BOX_DRAWING_CHARACTERS[self.lineStyle]["Horizontal"] * self.width + BOX_DRAWING_CHARACTERS[self.lineStyle]["BottomRight"])
              


WIDTH, HEIGHT = 128, 32
windowManager = WindowManager(WIDTH, HEIGHT, detachedTaskbar=False)

slateLinkWindow = Window()
#slateLinkWindow.AddLine(WIDTH/2, 0, HEIGHT/2+1, True)
#slateLinkWindow.AddLine(0, HEIGHT/2, WIDTH/2, False)

slateLinkWindow.CreateBox(-1, -1, WIDTH/3, HEIGHT)
slateLinkWindow.CreateBox(WIDTH/3, 2*(HEIGHT/3)-1, 2*WIDTH/3, HEIGHT/3)
slateLinkWindow.AddTextBox(WIDTH/3+1, 2*(HEIGHT/3), 2*WIDTH/3-1, 3, "hello world\nlorem ipsum dolor sit amet, cogito ergo sum wrhwhrwh tjj ty4j4ae6t teahjcvhjgadvh toy")

#windowManager.PrintCurrentWindow()
windowManager.RenderWindow(slateLinkWindow)