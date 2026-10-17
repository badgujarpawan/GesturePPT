import cv2

from gesture.detector import GestureDetector
from gesture.movement import MovementTracker


detector = GestureDetector()
tracker = MovementTracker()

print("Starting movement test...")
print("Move your hand left and right.")
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

        movement = tracker.update(
            wrist_position
        )

        if movement:

            horizontal = movement[0]
            vertical = movement[1]

            print(
                f"Movement: X={horizontal}, Y={vertical}"
            )

        x, y = wrist_position

        cv2.circle(
            frame,
            (x, y),
            10,
            (0, 0, 255),
            -1
        )

    cv2.imshow(
        "Gesture PPT - Movement Test",
        frame
    )

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


detector.release()
cv2.destroyAllWindows()