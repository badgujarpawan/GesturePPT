import cv2
import mediapipe as mp

from mediapipe.tasks import python
from mediapipe.tasks.python import vision

from config.settings import CAMERA_INDEX, CAMERA_WIDTH, CAMERA_HEIGHT


class GestureDetector:

    def __init__(self):

        self.camera = cv2.VideoCapture(CAMERA_INDEX)

        self.camera.set(
            cv2.CAP_PROP_FRAME_WIDTH,
            CAMERA_WIDTH
        )

        self.camera.set(
            cv2.CAP_PROP_FRAME_HEIGHT,
            CAMERA_HEIGHT
        )

        base_options = python.BaseOptions(
            model_asset_path="models/hand_landmarker.task"
        )

        options = vision.HandLandmarkerOptions(
            base_options=base_options,
            running_mode=vision.RunningMode.IMAGE,
            num_hands=1,
            min_hand_detection_confidence=0.7,
            min_hand_presence_confidence=0.7,
            min_tracking_confidence=0.7
        )

        self.hand_landmarker = vision.HandLandmarker.create_from_options(
            options
        )

    def read_frame(self):

        success, frame = self.camera.read()

        if not success:
            return None, None

        rgb_frame = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2RGB
        )

        mp_image = mp.Image(
            image_format=mp.ImageFormat.SRGB,
            data=rgb_frame
        )

        results = self.hand_landmarker.detect(mp_image)

        return frame, results

    def get_wrist_position(self, results, frame):

        if not results.hand_landmarks:
            return None

        hand_landmarks = results.hand_landmarks[0]

        wrist = hand_landmarks[0]

        height, width, _ = frame.shape

        x = int(wrist.x * width)
        y = int(wrist.y * height)

        return x, y

    def release(self):

        self.camera.release()
        self.hand_landmarker.close()