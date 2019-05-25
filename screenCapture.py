import numpy as np
import cv2
import platform
from sys import argv

if platform.system() == 'Linux':
    import pyscreenshot as ig
else:
    from PIL import ImageGrab as ig

if len(argv) < 3 :
	print("Not enough parameters..")
	print("Usage : screenCapture.py width height")
	exit()
try:	
	width = int(argv[1])
	height = int(argv[2])
except ValueError:
	print("Error : Please provide integer values...")
	print("Usage : screenCapture.py width height")
	exit()
print("Live screen capture begin, press q to quit")

while(True):
    try:
        
        screen = np.array(ig.grab(bbox=(0,0,width,height)))
        cv2.imshow('live',cv2.cvtColor(screen,cv2.COLOR_BGR2RGB))
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            print("Exiting..")
            break
    except KeyboardInterrupt:
        print("Exiting..")
        cv2.destroyAllWindows()
        break
        
