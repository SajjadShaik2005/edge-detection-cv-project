import cv2
from utils import detect_edges

def main():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Cannot access webcam")
        return

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        edges = detect_edges(frame)

        cv2.imshow("Original Video", frame)
        cv2.imshow("Edge Detection", edges)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
