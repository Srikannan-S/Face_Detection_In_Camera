import cv2

alg="haarcascade_frontalface_default.xml"

# Loading the haarcascade algorithm

haar_cascade=cv2.CascadeClassifier(alg)

# Cam id Initialization 0 for primary cam 1 for secondary cam

cam=cv2.VideoCapture(0)

while True:
    # Reading the cam it gives 2 values 1.true/false 2.cam we can ignore the 1st
    _,img=cam.read()

    # Converting the image to Gray_Scale

    Gray_Img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    # Getting Co-ordinates
    # 3rd values indicates number of comparision to check it is face or not 
    face=haar_cascade.detectMultiScale(Gray_Img,1.3,4)

    for (x,y,w,h) in face: # To Draw Rectangle
        # 1st value is the img should draw the rectangle
        # 2nd x and y axis
        # 3rd x+width and y+height
        # 4th color (Blue,Green,Red)
        # 5th thickness
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

    # showing the image in rectangle
    cv2.imshow("Face_Detection",img)

    key=cv2.waitKey(10)
    if key==27:  # 27 is the value for Escape key if you give esc key it will terminate otherwise not
        break
    
# Releasing the camera and destroy the windows
cam.release()
cv2.destroyAllWindows()
        
