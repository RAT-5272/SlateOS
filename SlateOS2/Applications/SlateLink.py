from ...SlateOS2.TerminalUserInterface import Window, windowManager, WIDTH, HEIGHT

window = Window()
window.AddLine(WIDTH/2, 0, HEIGHT, True)
window.AddLine(0, HEIGHT/2, WIDTH/2, False)

windowManager.RenderWindow(window)