import cv2
import numpy as np

path="./assets/images/lambo.jpeg"

def empty(a):
  pass

# Creating a TrackBar
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",640,240)
cv2.createTrackbar("Hue Min","TrackBars",0,179,empty)
cv2.createTrackbar("Hue Max","TrackBars",179,179,empty)
cv2.createTrackbar("Sat Min","TrackBars",0,255,empty)
cv2.createTrackbar("Sat Max","TrackBars",255,255,empty)
cv2.createTrackbar("Val Min","TrackBars",0,255,empty)
cv2.createTrackbar("Val Max","TrackBars",255,255,empty)

while True:
  # Getting Trackbars values
  h_min = cv2.getTrackbarPos("Hue Min","TrackBars")
  h_max = cv2.getTrackbarPos("Hue Max","TrackBars")
  s_min = cv2.getTrackbarPos("Sat Min","TrackBars")
  s_max = cv2.getTrackbarPos("Sat Max","TrackBars")
  v_min = cv2.getTrackbarPos("Val Min","TrackBars")
  v_max = cv2.getTrackbarPos("Val Max","TrackBars")
  print(h_min,h_max,s_min,s_max,v_min,v_max)

  # Original Image
  img=cv2.imread(path)

  # Creating HSV Image
  imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

  # Creating Mask Image
  lower= np.array([h_min,s_min,v_min])
  upper= np.array([h_max,s_max,v_max])
  mask = cv2.inRange(imgHSV,lower,upper)

  # Final Image which will merge original iamge and masked image
  imgResult = cv2.bitwise_and(img,img,mask=mask)

  # Displaying Images
  cv2.imshow("Original",img)
  cv2.imshow("HSV",imgHSV)
  cv2.imshow("Mask",mask)
  cv2.imshow("Result",imgResult)

  # Press q to exit
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

cv2.destroyAllWindows()