
def transform(color):
    if color == "red":
        return (255, 0, 0)
    elif color == "green":
        return (0, 255, 0)
    elif color == "blue":
        return (0, 0, 255)
    elif color == "orange":
        return (255, 165, 0)
    elif color == "yellow":
        return (255, 255, 0)
    elif color == "purple":
        return (128, 0, 128)
    elif color == "pink":
        return (255, 192, 203)
    elif color == "brown":
        return (165, 42, 42)
    elif color == "gray":
        return (128, 128, 128)
    elif color == "cyan":
        return (0, 255, 255)
    elif color == "magenta":
        return (255, 0, 255)
    elif color == "white":
        return (255, 255, 255)
    elif color == "black":
        return (0, 0, 0)
    else:
        return (0, 0, 0)