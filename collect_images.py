# Import necessary libraries
import cv2
import os
from datetime import datetime
 
# set path in which you want to save images
path = r'D:/sensor_based_registration/camera_calibration results/cam3_images_rifle_rgb'
 
# changing directory to given path
os.chdir(path)
 
# i variable is to give unique name to images
i = 1
 
wait = 0
 
# Open the camera
video = cv2.VideoCapture("D:/sensor_based_registration/camera_calibration results/Rifle_RGB/XQE_0071.mp4")
 
 
while True:
    # Read video by read() function and it
    # will extract and  return the frame
    ret, img = video.read()
 
    # Put current DateTime on each frame
    font = cv2.FONT_HERSHEY_PLAIN
    cv2.putText(img, str(datetime.now()), (20, 40),
                font, 2, (255, 255, 255), 2, cv2.LINE_AA)
 
    # Display the image
    cv2.imshow('live video', img)
 
    # wait for user to press any key
    key = cv2.waitKey(50)
 
    # wait variable is to calculate waiting time
    wait = wait+50
 
    if key == ord('q'):
        break
    # when it reaches to 5000 milliseconds
    # we will save that frame in given folder
    if wait == 3000:
        filename = 'Frame_'+str(i)+'.jpg'
         
        # Save the images in given path
        cv2.imwrite(filename, img)
        i = i+1
        wait = 0
 
# close the camera
video.release()
 
# close open windows
cv2.destroyAllWindows()
