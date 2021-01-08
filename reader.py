from PIL import Image


def read(img: str, channel: int = 1) -> [[int]]:
    img = Image.open(img).convert(mode='RGB')
    data = [[0 for _ in range(img.width)]
            for _ in range(img.height)]
    for i in range(img.height):
        for j in range(img.width):
            data[i][j] = img.getpixel((j, i))[channel]
    print(data[328])
    return data
