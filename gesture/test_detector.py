import cv2

from gesture.detector import GestureDetector


detector = GestureDetector()

print("Starting hand position test...")
print("Move your hand around.")
print("Press Q to quit.")

while True:

    frame, results = detector.read_frame()

    if frame is None:
        print("Could not read camera frame.")
        break

    wrist_position = detector.get_wrist_position(
        results,
        frame
    )

    if wrist_position:
        x, y = wrist_position

        print(f"Wrist position: X={x}, Y={y}")

        cv2.circle(
            frame,
            (x, y),
            10,
            (0, 0, 255),
            -1
        )

    cv2.imshow(
        "Gesture PPT - Wrist Tracking",
        frame
    )

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


detector.release()
cv2.destroyAllWindows()