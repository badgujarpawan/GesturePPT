import pyautogui

from presentation.commands import Command


class PresentationController:

    def execute(self, command):

        if command == Command.NEXT_SLIDE:

            self.next_slide()

        elif command == Command.PREVIOUS_SLIDE:

            self.previous_slide()

        elif command == Command.START_PRESENTATION:

            self.start_presentation()

        elif command == Command.PAUSE_PRESENTATION:

            self.pause_presentation()

        elif command == Command.RESUME_PRESENTATION:

            self.resume_presentation()

        elif command == Command.END_PRESENTATION:

            self.end_presentation()

        elif command == Command.GO_TO_SLIDE:

            self.go_to_slide()

        elif command == Command.QUIT_APPLICATION:

            self.quit_application()

        else:

            print("Unknown command")

    def next_slide(self):

        pyautogui.press("right")

        print("PowerPoint: Next slide")

    def previous_slide(self):

        pyautogui.press("left")

        print("PowerPoint: Previous slide")

    def start_presentation(self):

        pyautogui.press("f5")

        print("PowerPoint: Presentation started")

    def pause_presentation(self):

        pyautogui.press("b")

        print("PowerPoint: Presentation paused")

    def resume_presentation(self):

        pyautogui.press("b")

        print("PowerPoint: Presentation resumed")

    def end_presentation(self):

        pyautogui.press("esc")

        print("PowerPoint: Presentation ended")

    def go_to_slide(self):

        print("PowerPoint: Go to slide command received")

    def quit_application(self):

        print("Gesture PPT: Quit requested")