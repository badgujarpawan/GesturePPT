import io
import wave

import sounddevice as sd
import speech_recognition as sr

from config.settings import (
    VOICE_LANGUAGE,
    VOICE_TIMEOUT,
    VOICE_PHRASE_TIME_LIMIT
)


class SpeechRecognizer:

    def __init__(self):

        self.recognizer = sr.Recognizer()

        self.sample_rate = 16000
        self.channels = 1

        self.noise_threshold = 300
        self.silence_duration = 0.8

    def listen(self):

        print("Listening...")

        try:

            recording = sd.rec(
                int(
                    VOICE_PHRASE_TIME_LIMIT *
                    self.sample_rate
                ),
                samplerate=self.sample_rate,
                channels=self.channels,
                dtype="int16"
            )

            sd.wait()

            recording = recording[
                abs(recording[:, 0])
                > self.noise_threshold
            ]

        except Exception as error:

            print(
                f"Microphone error: {error}"
            )

            return None

        audio_data = self._convert_to_audio_data(
            recording
        )

        if audio_data is None:
            return None

        try:

            text = self.recognizer.recognize_google(
                audio_data,
                language=VOICE_LANGUAGE
            )

            print(
                f"Recognized: {text}"
            )

            return text

        except sr.UnknownValueError:

            print(
                "Could not understand the speech."
            )

            return None

        except sr.RequestError as error:

            print(
                f"Speech recognition service error: {error}"
            )

            return None

    def _convert_to_audio_data(
        self,
        recording
    ):

        try:

            buffer = io.BytesIO()

            with wave.open(
                buffer,
                "wb"
            ) as wav_file:

                wav_file.setnchannels(
                    self.channels
                )

                wav_file.setsampwidth(2)

                wav_file.setframerate(
                    self.sample_rate
                )

                wav_file.writeframes(
                    recording.tobytes()
                )

            buffer.seek(0)

            with wave.open(
                buffer,
                "rb"
            ) as wav_file:

                audio_bytes = (
                    wav_file.readframes(
                        wav_file.getnframes()
                    )
                )

            return sr.AudioData(
                audio_bytes,
                self.sample_rate,
                2
            )

        except Exception as error:

            print(
                f"Audio conversion error: {error}"
            )

            return None