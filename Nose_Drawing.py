import cv2 as cv

def draw_nose(img_color, locations):
    for i in range(len(locations) - 1):
        if len(locations) < 2:
            continue
        cv.line(img_color, tuple(locations[i]), tuple(locations[i + 1]), (0, 255, 255), 3)

    return img_color

cap = cv.VideoCapture(0)

list_nose_location = []
history_nose_locations = []
isDraw = True

face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
    ret, img_color = cap.read()

    img_color = cv.flip(img_color, 1)

    gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv.rectangle(img_color, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img_color[y:y + h, x:x + w]

        nose_center_x = x + w // 2
        nose_center_y = y + h // 2
        cv.circle(img_color, (nose_center_x, nose_center_y), 10, (0, 255, 0), -1)

        if isDraw:
            list_nose_location.append((nose_center_x, nose_center_y))
        else:
            history_nose_locations.append(list_nose_location.copy())
            list_nose_location.clear()

    img_color = draw_nose(img_color, list_nose_location)

    for nose_locations in history_nose_locations:
        img_color = draw_nose(img_color, nose_locations)

    cv.imshow('Result', img_color)

    key = cv.waitKey(1)
    if key == 27:  # esc
        break
    elif key == 32:  # space bar
        list_nose_location.clear()
        history_nose_locations.clear()
    elif key == ord('v'):
        isDraw = not isDraw

# 종료 시 비디오 캡처 객체 해제
cap.release()

# 모든 창 닫기
cv.destroyAllWindows()
