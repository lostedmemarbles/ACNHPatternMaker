from PIL import Image
from pixelateFunctions import *
import sys
import extcolors
import numpy as np


if len(sys.argv) < 3:
    print("NEED GRID SIZE")
    sys.exit()
    
gridWidth = int(sys.argv[1]    )
gridHeight = int(sys.argv[2])
    
fileName = "JJpic.jpg"
numOfColors = 10
tol = 10


im = Image.open(fileName)
print(im.size)
width = im.size[0]
height = im.size[1]
pixels = im.load()
print(pixels[10,10])
pixelated = Image.new("RGB", im.size)
diffColors, numOfPixels = extcolors.extract_from_image(im,tolerance=tol,limit=numOfColors)
print(diffColors)
for color in diffColors:
    exec("rgb_to_hex"+str(color[0]))
widthJump = width / gridWidth
heightJump = height / gridHeight
startWidth = 0
endWidth = int(widthJump - 1)
startHeight = 0
endHeight = int(heightJump - 1)

for i in range(gridWidth):
    for j in range(gridHeight):
        if endWidth >= width:
            endWidth = width - 1
        if endHeight >= height:
            endHeight = height - 1
        squareColor = getAverage(pixels,startWidth,endWidth,startHeight,endHeight)
        print(squareColor)
        pixelated = setColors(np.asarray(pixelated),startWidth,endWidth,startHeight,endHeight,squareColor)
    Image.fromarray(pixelated).save("pixelated"+fileName)