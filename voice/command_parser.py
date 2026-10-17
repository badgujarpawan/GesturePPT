from presentation.commands import Command


class CommandParser:

    def parse(self, text):

        if not text:
            return None

        text = text.lower().strip()

        if text in (
            "next",
            "next slide",
            "next page",
            "go next"
        ):
            return Command.NEXT_SLIDE

        if text in (
            "previous",
            "previous slide",
            "previous page",
            "go back",
            "go to previous"
        ):
            return Command.PREVIOUS_SLIDE

        if text in (
            "start",
            "start presentation",
            "start slideshow",
            "begin presentation"
        ):
            return Command.START_PRESENTATION

        if text in (
            "pause",
            "pause presentation"
        ):
            return Command.PAUSE_PRESENTATION

        if text in (
            "resume",
            "resume presentation"
        ):
            return Command.RESUME_PRESENTATION

        if text in (
            "end",
            "end presentation",
            "exit presentation",
            "stop presentation"
        ):
            return Command.END_PRESENTATION

        if text in(
            "quit",
            "quit application",
            "exit application",
            "close application"
        ):

            return Command.QUIT_APPLICATION

        return None