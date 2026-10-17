import cv2

from gesture.detector import GestureDetector
from gesture.recognizer import GestureRecognizer
from presentation.controller import PresentationController


def main():

    detector = GestureDetector()
    recognizer = GestureRecognizer()
    controller = PresentationController()

    print("================================")
    print("        GESTURE PPT")
    print("================================")
    print()
    print("Starting gesture control...")
    print("Hand enters → 3 second stabilization")
    print("Physical RIGHT → Next slide")
    print("Physical LEFT  → Previous slide")
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

        # Always send the position to the recognizer.
        # None tells it that the hand is not visible.
        command = recognizer.recognize(
            wrist_position
        )

        if command:

            print(
                f"GESTURE COMMAND: {command.name}"
            )

            controller.execute(command)

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
            "Gesture PPT",
            frame
        )

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    detector.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()