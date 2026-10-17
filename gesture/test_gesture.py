import cv2

from gesture.detector import GestureDetector
from gesture.recognizer import GestureRecognizer


detector = GestureDetector()
recognizer = GestureRecognizer()

print("================================")
print("       GESTURE TEST")
print("================================")
print()
print("Hand enters -> wait 5 seconds.")
print("Then move left/right to control slides.")
print("Remove hand and re-enter -> wait 5 seconds again.")
print("Press Q to quit.")
print()

while True:

    frame, results = detector.read_frame()

    if frame is None:
        print("Could not read camera frame.")
        break

    wrist_position = detector.get_wrist_position(
        results,
        frame
    )

    # Always call recognizer.
    # This allows it to detect when the hand disappears.
    command = recognizer.recognize(
        wrist_position
    )

    if command:
        print(
            f"GESTURE DETECTED: {command.name}"
        )

    if wrist_position:

        x, y = wrist_position

        cv2.circle(
            frame,
            (x, y),
            10,
            (0, 0, 255),
            -1
        )

    cv2.imshow(
        "Gesture PPT - Gesture Test",
        frame
    )

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


detector.release()
cv2.destroyAllWindows()