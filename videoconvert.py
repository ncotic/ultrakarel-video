import cv2
import os
import shutil
from PIL import Image
vidIn = input("Full path to video file: ")
resize = int(input("Canvas size (will be square so just put 1 number): "))
frame = int(input("Framerate for video: "))
os.system(f"./ffmpeg -y -i {vidIn} -vf scale={resize}:{resize},setsar=1 -r {frame} resize.mp4")
vidFi = cv2.VideoCapture("resize.mp4")
success,image = vidFi.read()
count = 0
if os.path.exists('./frames'):
    shutil.rmtree('./frames')
os.makedirs('./frames')

while success:
    cv2.imwrite("frames/frame%d.jpg" % count, image)   
    success,image = vidFi.read()
    count += 1

os.remove('resize.mp4')
if os.path.exists('animation.txt'):
    os.remove('animation.txt')
f = open("animation.txt", "w")
for i in range(len([entry for entry in os.listdir(r'./frames') if os.path.isfile(os.path.join(r'./frames', entry))])):
    image = Image.open("frames/frame%i.jpg" % i, "r")
    width, height = image.size
    pixel_values = list(image.getdata())
    f.write(f"a{i} = {pixel_values}\n")
f.close()

shutil.rmtree('./frames')
print("Completed. Data is in animation.txt")
