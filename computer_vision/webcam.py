# to close by esc button
import cv2

webcam=cv2.VideoCapture(0)#videocaputer- capture video (0-first camera or 1-second camer(maybe a webcam)even we can pass a video we want by copying the video path and passing it in this way(r'enter path here'))
while webcam.isOpened():#will work till webcam is open
    status, frame=webcam.read()
    if not status:
        print("Camera not working")
        break
    cv2.imshow("Webcam", frame)#update frame in webcam window
    # press Esc to exit
    if cv2.waitKey(5)==27:#if we'll press escpae in 1milisecond the webcam will close here 1 passed is 1milisec)
            break

webcam.release()
cv2.destroyAllWindows()