from PIL import Image
import numpy as np
import random
import math

# Thank you to Chris Stone (Harvey Mudd College)
# for much of the inspiration behind this code.

class ImageHandler:

    def display(self):
        self.im.show()

    def load(self, name):
        self.im = Image.open(name)
        self.im = self.im.resize((self.w, self.h))

    def save(self, name):
        self.im.save(name)

    #given a pixel coordinte (x, y) write rgb value to the pixel
    def setPixel(self, x, y, rgb):
        self.im.putpixel((x, y), rgb)

    def getPixels(self):
        arr = list(self.im.getdata())
        new = []
        for y in range(self.h):
            row = []
            for x in range(self.w):
                row.append(tuple(arr[y * self.w + x]))
            new.append(row)
        return new

    #maybe have them write this method as a class?
    def applyFunctionToAllPixels(self, f, depth, seed, bright, tint):
        for x in range(self.w):
            for y in range(self.h):
                self.setPixel(x, y, f(x,y,self.w, depth, seed, bright, tint)) #TODO: get w out of there. I'm just being lazy.

    def fromArray(self, arr):
        for x in range(self.w):
            for y in range(self.h):
                self.setPixel(x, y, (arr[y][x]))
#        self.pixels = [item for sublist in arr for item in sublist]
 #       self.im = Image.fromarray(np.asarray(arr), 'RGB')

    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.im = Image.new('RGB', (w, h))



#converts an int i from range [-N, N] to float in [-1, 1]
def toFloatInRange(i, N):
    return float(i) / float(N)

#converts float in [-1, 1] to int in range [0, 255]
def toRGBVal(i):
    return int(round(127.5 + (127.5 * i)))

def grayscaleBuildHelper(x, y, w):
    n = int(w / 2) #TODO: Right now width must be == height and w and h must be odd.

    xminusN = x - n #now these guys are in the range [-N, N]
    yminusN = y - n

    #convert x, y to floats float_x and float_y which are in [-1, 1]
    float_x = toFloatInRange(xminusN, n)
    float_y = toFloatInRange(yminusN, n)

    #reaaal important to keep everything between [-1, 1]

    #TODO: feed seed and depth in as arguments or smthing.
    depth = 5
    random.seed(15)

    v = build(depth, 0, (float_x,float_y))
    v = toRGBVal(v) #normalize it to [0, 255]
    return (v, v, v) #grayscale for now.

def colorBuildHelper(x, y, w, depth, seed, bright, tint):
    n = int(w / 2) #TODO: Right now width must be == height and w and h must be odd.

    xminusN = x - n #now these guys are in the range [-N, N]
    yminusN = y - n

    #convert x, y to floats float_x and float_y which are in [-1, 1]
    float_x = toFloatInRange(xminusN, n)
    float_y = toFloatInRange(yminusN, n)

    #reaaal important to keep everything between [-1, 1]

    #TODO: feed seed and depth in as arguments or smthing.
    random.seed(seed)

    r = build(depth, 0, (float_x,float_y))
    r = int(toRGBVal(r) * bright)
    g = build(depth, 0, (float_x,float_y))
    g = int(toRGBVal(g) * bright)
    b = build(depth, 0, (float_x,float_y))
    b = int(toRGBVal(b) * bright)

    return tuple(map(sum,zip((r,g,b),tint)))

#every function in build has to be able to take two floats in the range [-1, 1]
#and return two floats in the range [-1, 1]. that's how to garuntee it's pretty (i think.)
def build(depth, value, xy):
    x,y = xy
    
    if depth <= 0:
        r = random.randint(0,1)
        if r ==0:
            return x
        else:
            return y
    else:
        randNum = random.randint(1,20)
        if randNum == 1:
            return x
        elif randNum == 2:
            return y
        elif randNum >= 3 and randNum < 8:
            #return the sin
            v = build(depth - 1, value, xy)
            v = math.sin(v * 3.14)
            return v
        elif randNum >= 8 and randNum < 13:
            #return the cosin
            v = build(depth - 1, value, xy)
            v = math.cos(v * 3.14)
            return v
        elif randNum >= 13 and randNum <18:
            #find average
            v1 = build(depth - 1, value, xy)
            v2 = build(depth - 1, value, xy)
            v = (v1 + v2) / 2 
            return v
        elif randNum >= 18 and randNum < 19:
            #find square
            v = build(depth - 1, value, xy)
            v *= v
            return v
        elif randNum >= 19 and randNum <20:
            #find cube
            v = build(depth - 1, value, xy)
            v = v * v * v
            return v
        elif randNum >= 20 and randNum <21:
            #find mult 3
            v1 = build(depth - 1, value, xy)
            v2 = build(depth - 1, value, xy)
            v3 = build(depth - 1, value, xy)
            v = v1 * v2 * v3
            return v
        else:
            #find mult 2
            v1 = build(depth - 1, value, xy)
            v2 = build(depth - 1, value, xy)
            v = v1 * v2
            return v

######## PUT YOUR CODE BELOW THIS LINE #########

def addPixels(pix1, pix2):
    return tuple([pix1[0] + pix2[0], pix1[1] + pix2[1], pix1[2] + pix2[2]])

if __name__ == '__main__':
    width = 300
    height = 300
    ih = ImageHandler(width, height)

    # YOU MAY WANT TO TRY SOME OF THIS CODE
    #ih.load("example.jpg")
    depth = 5
    seed = 50
    brightness = 1
    tint = (0, 0, 0)
    ih.applyFunctionToAllPixels(colorBuildHelper, depth, seed, brightness, tint)

    pixels = ih.getPixels()

    # WRITE A LOOP TO ITERATE THROUGH YOUR PIXEL ARRAY
    
    ih.fromArray(pixels)
    ih.display()
    ih.save("test.jpg")




