import threading
import queue

from voice.speech import SpeechRecognizer
from voice.command_parser import CommandParser


class VoiceWorker:

    def __init__(self):

        self.command_queue = queue.Queue()

        self.parser = CommandParser()
        self.speech = SpeechRecognizer()

        self.stop_event = threading.Event()

        self.thread = threading.Thread(
            target=self._run,
            daemon=True
        )

    def start(self):

        self.thread.start()

        print("Voice worker started.")

    def stop(self):

        self.stop_event.set()

        print("Voice worker stopping...")

    def get_command(self):

        try:

            return self.command_queue.get_nowait()

        except queue.Empty:

            return None

    def _run(self):

        while not self.stop_event.is_set():

            text = self.speech.listen()

            if self.stop_event.is_set():
                break

            if not text:
                continue

            command = self.parser.parse(text)

            if command:

                print(
                    f"VOICE COMMAND: {command.name}"
                )

                self.command_queue.put(command)

            else:

                print(
                    f"Unknown voice command: {text}"
                )