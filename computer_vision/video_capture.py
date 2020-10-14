import cv2
import time
import pandas as pd
from datetime import datetime

first_frame = None
times = []
status_list = [None, None]
video = cv2.VideoCapture(0)
df = pd.DataFrame(columns=['Start', 'End'])
while True:
    status = 0
    check, frame = video.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)

    if first_frame is None:
        first_frame = gray
        continue

    delta_frame = cv2.absdiff(first_frame, gray)
    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)

    (cnts, _) = cv2.findContours(thresh_frame.copy(),
                                 cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv2.contourArea(contour) < 10000:
            continue
        status = 1
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

    cv2.imshow('capturing', frame)
    key = cv2.waitKey(1)

    status_list.append(status)
    status_list = status_list[-2:]
    if (status_list[-1] == 1 and status_list[-2] == 0) or (status_list[-1] == 0 and status_list[-2] == 1):
        times.append(datetime.now())

    if key == ord('q'):
        if status == 1:
            times.append(datetime.now())
        break


for i in range(0, len(times), 2):
    df = df.append({"Start": times[i], "End": times[i + 1]}, ignore_index=True)
df.to_csv("Times.csv")
video.release()
cv2.destroyAllWindows()
