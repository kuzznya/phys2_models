from PIL import Image


# Read image using defined channel (default is green)
def read(img: str, channel: int = 1) -> [[int]]:
    img = Image.open(img).convert(mode='RGB')
    data = [[0 for _ in range(img.width)]
            for _ in range(img.height)]
    for i in range(img.height):
        for j in range(img.width):
            data[i][j] = img.getpixel((j, i))[channel]
    return data
