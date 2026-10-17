import cv2

from gesture.detector import GestureDetector
from gesture.recognizer import GestureRecognizer

from presentation.controller import PresentationController

from voice.worker import VoiceWorker


def main():

    detector = GestureDetector()
    recognizer = GestureRecognizer()
    controller = PresentationController()

    voice_worker = VoiceWorker()

    voice_worker.start()

    print("================================")
    print("        GESTURE PPT")
    print("================================")
    print()
    print("Gesture control:")
    print("Hand enters → 3 second stabilization")
    print("Physical RIGHT → Next slide")
    print("Physical LEFT  → Previous slide")
    print()
    print("Voice control:")
    print("Say commands such as:")
    print("  next slide")
    print("  previous slide")
    print("  start presentation")
    print("  end presentation")
    print()
    print("Press Q to quit.")
    print()

    try:

        while True:

            # --------------------------------
            # GESTURE INPUT
            # --------------------------------

            frame, results = detector.read_frame()

            if frame is None:
                print("Could not read camera frame.")
                break

            wrist_position = detector.get_wrist_position(
                results,
                frame
            )

            gesture_command = recognizer.recognize(
                wrist_position
            )

            if gesture_command:

                print(
                    f"GESTURE COMMAND: "
                    f"{gesture_command.name}"
                )

                controller.execute(
                    gesture_command
                )

            # --------------------------------
            # VOICE INPUT
            # --------------------------------

            voice_command = voice_worker.get_command()

            if voice_command:

                print(
                    f"VOICE COMMAND RECEIVED: "
                    f"{voice_command.name}"
                )

                controller.execute(
                    voice_command
                )

            # --------------------------------
            # DISPLAY
            # --------------------------------

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

    finally:

        print()
        print("Shutting down...")

        voice_worker.stop()

        detector.release()

        cv2.destroyAllWindows()

        print("Gesture PPT stopped.")


if __name__ == "__main__":
    main()