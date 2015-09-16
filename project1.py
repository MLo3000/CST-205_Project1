from pprint import pprint

pictures = []
redPixelList = []
bluePixelList = []
greenPixelList = []

def median(myList):
  sortedList = sorted(myList)
  if (len(sortedList)%2) == 0:
    middleIndex = len(sortedList)/2
    return sortedList[middleIndex]
  else:
    middleIndex = (len(sortedList)/2) + 1
    return sortedList[middleIndex]
    
height = 557
width = 495
    
newPic = makeEmptyPicture(width, height)

folder = "/Users/Miguel/Desktop/CSUMB/Fall 2015/CST205/Project1/Images/"


pic1 = folder + "1.png" 
img1 = makePicture(pic1)
pictures.append(img1)

pic2 = folder + "2.png"
img2 = makePicture(pic2)
pictures.append(img2)

pic3 = folder + "3.png"
img3 = makePicture(pic3)
pictures.append(img3)

pic4 = folder + "4.png"
img4 = makePicture(pic4)
pictures.append(img4)

pic5 = folder + "5.png"
img5 = makePicture(pic5)
pictures.append(img5)

pic6 = folder + "6.png"
img6 = makePicture(pic6)
pictures.append(img6)

pic7 = folder + "7.png"
img7 = makePicture(pic7)
pic1 = folder + "7.png"

pic8 = folder + "8.png"
img8 = makePicture(pic8)
pictures.append(img7)

pic9 = folder + "9.png"
img9 = makePicture(pic9)
pictures.append(img9)

for x in range(0, width):
  for y in range(0, height):
    for imageNumber in range(0, 8):
      pixel = getPixel(pictures[imageNumber], x, y)
      red = getRed(pixel)
      green = getGreen(pixel)
      blue = getBlue(pixel)
      
      redPixelList.append(red)
      greenPixelList.append(green)
      bluePixelList.append(blue)
      
    redPix = median(redPixelList)
    greenPix = median(greenPixelList)
    bluePix = median(bluePixelList)
    
    newImagePixel = getPixel(newPic, x, y)
    setRed(newImagePixel, redPix)
    setGreen(newImagePixel, greenPix)
    setBlue(newImagePixel, bluePix)
    
    redPixelList = []
    greenPixelList = []
    bluePixelList = []
