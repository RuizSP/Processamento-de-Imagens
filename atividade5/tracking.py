import numpy as np
import cv2

cap = cv2.VideoCapture(0)

trackbarWindow = "trackbar window"
cv2.namedWindow(trackbarWindow)

def onChange(val):
    pass

cv2.createTrackbar("Min Hue", trackbarWindow, 0, 255, onChange)
cv2.createTrackbar("Max Hue", trackbarWindow, 255, 255, onChange)
cv2.createTrackbar("Min Saturation", trackbarWindow, 0, 255, onChange)
cv2.createTrackbar("Max Saturation", trackbarWindow, 255, 255, onChange)
cv2.createTrackbar("Min Value", trackbarWindow, 0, 255, onChange)
cv2.createTrackbar("Max Value", trackbarWindow, 255, 255, onChange)

def setLimitations():
    hue = {}
    hue["min"] = cv2.getTrackbarPos("Min Hue", trackbarWindow)
    hue["max"] = cv2.getTrackbarPos("Max Hue", trackbarWindow)

    if hue["min"] > hue["max"]:
        cv2.setTrackbarPos("Max Hue", trackbarWindow, hue["min"])
        hue["max"] = cv2.getTrackbarPos("Max Hue", trackbarWindow)

    saturation = {}
    saturation["min"] = cv2.getTrackbarPos("Min Saturation", trackbarWindow)
    saturation["max"] = cv2.getTrackbarPos("Max Saturation", trackbarWindow)

    if saturation["min"] > saturation["max"]:
        cv2.setTrackbarPos("Max Saturation", trackbarWindow, saturation["min"])
        saturation["max"] = cv2.getTrackbarPos("Max Saturation", trackbarWindow)

    value = {}
    value["min"] = cv2.getTrackbarPos("Min Value", trackbarWindow)
    value["max"] = cv2.getTrackbarPos("Max Value", trackbarWindow)

    if value["min"] > value["max"]:
        cv2.setTrackbarPos("Max Value", trackbarWindow, value["min"])
        value["max"] = cv2.getTrackbarPos("Max Value", trackbarWindow)

    return hue, saturation, value

def computeTracking(frame, hue, sat, value):
    hsvimg = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #converte a imagem para hsv
    
    lowerColor = np.array([hue['min'], sat['min'], value['min']])
    upperColor = np.array([hue['max'], sat['max'], value['max']])
    mask = cv2.inRange(hsvimg, lowerColor, upperColor) # cria a mascara de cor 
    
    result = cv2.bitwise_and(frame, frame, mask=mask)
    
    gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
    _, gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY|cv2.THRESH_OTSU)
    contours, hierarchy = cv2.findContours(gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    if contours:
        maxArea = cv2.contourArea(contours[0])
        contourMaxAreaId = 0
        i = 0
        for cnt in contours:
            if maxArea < cv2.contourArea(cnt):
                maxArea = cv2.contourArea(cnt)
                contourMaxAreaId = i
            i += 1
        cntMaxArea = contours[contourMaxAreaId]
        x, y, w, h = cv2.boundingRect(cntMaxArea)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
    
    return frame, gray

while True:
    success, frame = cap.read()
    hue, sat, value = setLimitations()
    frame, gray =  computeTracking(frame, hue, sat, value)
    cv2.imshow("Webcam", frame)
    cv2.imshow("Result", gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

