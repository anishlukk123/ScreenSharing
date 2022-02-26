import  cv2
import numpy as np
import pyautogui
import time


ScreenSize = (1920,1080);
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("output.avi", fourcc, 20, ScreenSize)
fps = 120
prev = 0

while True:
    timeelasped = time.time()-prev
    img = pyautogui.screenshot()

    if timeelasped> 1.0/fps :
        prev = time.time()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        out.write(frame)

    cv2.waitKey(100)
cv2.destroyAllWindows()
out.release()
