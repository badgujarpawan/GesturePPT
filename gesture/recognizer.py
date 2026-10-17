import time

from presentation.commands import Command


class GestureRecognizer:

    def __init__(self):

        self.swipe_threshold = 100

        # Time required when a new hand enters the camera.
        self.entry_delay = 1.5

        # Hand must be absent this long before we consider
        # it genuinely gone.
        self.hand_lost_timeout = 1.0

        self.hand_detected_time = None
        self.last_seen_time = None

        self.reference_position = None

        self.active = False

    def recognize(self, current_position):

        current_time = time.time()

        # -------------------------------------------------
        # HAND NOT DETECTED
        # -------------------------------------------------

        if current_position is None:

            if self.last_seen_time is None:
                return None

            # Do not immediately reset because MediaPipe
            # can temporarily lose the hand.
            if current_time - self.last_seen_time >= self.hand_lost_timeout:

                self._reset()

            return None

        # -------------------------------------------------
        # HAND DETECTED
        # -------------------------------------------------

        self.last_seen_time = current_time

        # -------------------------------------------------
        # NEW HAND ENTERED CAMERA
        # -------------------------------------------------

        if self.hand_detected_time is None:

            self.hand_detected_time = current_time
            self.reference_position = current_position
            self.active = False

            return None

        # -------------------------------------------------
        # ENTRY STABILIZATION
        # -------------------------------------------------

        if not self.active:

            # Keep updating the reference while the presenter
            # positions the hand.
            self.reference_position = current_position

            if current_time - self.hand_detected_time >= self.entry_delay:

                self.active = True
                self.reference_position = current_position

                print("Gesture control active.")

            return None

        # -------------------------------------------------
        # NORMAL GESTURE DETECTION
        # -------------------------------------------------

        horizontal = (
            current_position[0] -
            self.reference_position[0]
        )

        vertical = (
            current_position[1] -
            self.reference_position[1]
        )

        # Ignore mainly vertical movement.
        if abs(horizontal) <= abs(vertical):
            return None

        command = None

        # Mirrored camera mapping:
        # Physical right -> NEXT
        # Physical left  -> PREVIOUS

        if horizontal <= -self.swipe_threshold:

            command = Command.NEXT_SLIDE

        elif horizontal >= self.swipe_threshold:

            command = Command.PREVIOUS_SLIDE

        if command:

            # Current position becomes the reference
            # for the next gesture.
            self.reference_position = current_position

            return command

        return None

    def _reset(self):

        self.hand_detected_time = None
        self.last_seen_time = None
        self.reference_position = None
        self.active = False