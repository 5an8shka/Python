#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install Pillow #python imaging library


# In[ ]:





# In[5]:


pip install opencv-python  #to perform image processing and computer vision task


# In[2]:


import cv2

imagePath = "C:\\Users\\tanis\\Pictures\\Screenshot_20230305-104053_WhatsApp.jpg"


# In[3]:


img = cv2.imread(imagePath)


# In[4]:


img.shape


# In[5]:


gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #to eliminate every form of color leaving only grey
#used because compresses image to minimum pixels


# In[6]:


gray_image.shape


# In[7]:


face_classifier = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)  
# detect objects in an image using the Viola-Jones algorithm which is already defined in cv2.CascadeClassifier
# cv2.data.haarcascades:: path to the directory where OpenCV's pre-trained classifier files are located contains details of the face like eyes nose etc.
# haarcascade_frontalface_default.xml:: name of the classifier file for detecting frontal faces


# In[8]:


face = face_classifier.detectMultiScale(  # to detect all faces
    gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40)
) 
# scalefactor specifies how much the image size is reduced at each image scale smaller scaleFactor value will increase the detection time and accuracy
# minNeighbors  how many neighboring rectangles are required for a detected object to be considered a valid face
# minSize minimum size of the face rectangle
# detected faces stored in form of tuples in face


# In[9]:


for (x, y, w, h) in face: # loop for all the values of tuple stored in face
    #x,y,w,h for x-coordinate y-coordinate width and height
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 4) #to draw rectangle around the detected face
    #(0,255,0) to determine color and 4 for thickness of box


# In[10]:


img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # to convert image from Blue Green Red (BGR) to RGB
#as the BGR color space is commonly used in OpenCV, while the RGB color space is more commonly used in other computer vision libraries and frameworks.


# In[11]:


import matplotlib.pyplot as plt
plt.figure(figsize=(20,10))#creates a new figure window with the specified size of 20 inches by 10 inches
plt.imshow(img_rgb) #displays the image


# In[13]:


plt.figure(figsize=(20,10))#creates a new figure window with the specified size of 20 inches by 10 inches
plt.imshow(img_rgb) #displays the image
plt.axis('off')# turns off the axis of the image plot by default it displays the axis and ticks the image


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


#WEB CAM FACE RECOGNITION


# In[2]:


import cv2
face_classifier = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)
# detect objects in an image using the Viola-Jones algorithm which is already defined in cv2.CascadeClassifier
# cv2.data.haarcascades:: path to the directory where OpenCV's pre-trained classifier files are located contains details of the face like eyes nose etc.
# haarcascade_frontalface_default.xml:: name of the classifier file for detecting frontal faces


# In[3]:


video_capture = cv2.VideoCapture(0) #to capture from live cam


# In[4]:


def detect_bounding_box(vid):
    gray_image = cv2.cvtColor(vid, cv2.COLOR_BGR2GRAY)#func from open cv lib converts input video to grayscale used in preporcessing
    faces = face_classifier.detectMultiScale(gray_image, 1.1, 5, minSize=(40, 40)) # uses a pre-trained face classifier to detect faces in the grayscale image. detectMultiScale function is used to detect objects at different scales in the image and minSize to determine minimum size 
    for (x, y, w, h) in faces:
        cv2.rectangle(vid, (x, y), (x + w, y + h), (0, 255, 0), 4)# iterates over the detected faces and draws a green rectangle around each face in the original color video vid
    return faces


# In[6]:


while True:
    result, video_frame = video_capture.read()  #starts an infinite loop that continuously reads frames from the video_capture
    if result is False:
        break  # terminate the loop if the frame is not read successfully

    faces = detect_bounding_box(
        video_frame
    )  # apply the function we created to the video frame

    cv2.imshow(
        "My Face Detection Project", video_frame
    )  # display the processed frame in a window named "My Face Detection Project"

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break #waits for a keypress from the user, and checks if the key pressed was the "q" key. If so, the loop is terminated using the break statement

    # Check if the user has closed the window
    if cv2.getWindowProperty("My Face Detection Project", cv2.WND_PROP_VISIBLE) < 1:
        break

video_capture.release()
cv2.destroyAllWindows()


# In[4]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[8]:


import numpy as np
import cv2
cap = cv2.VideoCapture(0)
cap.set(3,640) # set Width
cap.set(4,480) # set Height
while(True):
    ret, frame = cap.read()
    frame = cv2.flip(frame, -1) # Flip camera vertically
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    cv2.imshow('frame', frame)
    cv2.imshow('gray', gray)
    
    k = cv2.waitKey(30) & 0xff
    if k == 27: # press 'ESC' to quit
        break
cap.release()
cv2.destroyAllWindows()


# In[7]:


import numpy as np
import cv2
faceCascade = cv2.CascadeClassifier('Cascades/haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
cap.set(3,640) # set Width
cap.set(4,480) # set Height
while True:
    ret, img = cap.read()
    img = cv2.flip(img, -1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale( 
        gray,
        scaleFactor=1.2,
        minNeighbors=5,     
        minSize=(20, 20)
        )
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]  
    cv2.imshow('video',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27: # press 'ESC' to quit
        break
cap.release()
cv2.destroyAllWindows()


# In[9]:



import cv2
import os

cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video width
cam.set(4, 480) # set video height

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# For each person, enter one numeric face id
face_id = input('\n enter user id end press <return> ==>  ')

print("\n [INFO] Initializing face capture. Look the camera and wait ...")
# Initialize individual sampling face count
count = 0

while(True):

    ret, img = cam.read()
    img = cv2.flip(img, -1) # flip video image vertically
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:

        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
        count += 1

        # Save the captured image into the datasets folder
        cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])

        cv2.imshow('image', img)

    k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break
    elif count >= 30: # Take 30 face sample and stop video
         break

# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()


# In[ ]:




