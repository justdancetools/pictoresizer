from PIL import Image
import os
inputfiles=os.listdir("input")
for inputfile in inputfiles:
    picto=Image.open("input/" + inputfile)
    result=picto.resize((128,128))
    result.save("output/" + inputfile.split(".")[0] + ".png")