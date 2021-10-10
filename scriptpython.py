import sys
import cv2
import asyncio


vidcap = cv2.VideoCapture('video.mp4')

async def getFrame(sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC, sec*1000)
    hasFrames,image = vidcap.read()
    print(image)
    if hasFrames:
        cv2.imwrite("image.jpg", image)     # save frame as JPG file
       
    return hasFrames


async def main():
    success = await getFrame(0)
    sys.stdout.flush()
    print('Imaged saved')

frameRate = 0.5 #//it will capture image in each 0.5 second
count=1
asyncio.run(main())
