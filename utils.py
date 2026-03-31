import cv2

def detect_edges(frame):

    # convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # reduce noise
    blur = cv2.GaussianBlur(gray, (5,5), 0)

    # detect edges
    edges = cv2.Canny(blur, 50, 150)

    return edges
