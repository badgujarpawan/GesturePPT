from enum import Enum, auto


class Command(Enum):

    NEXT_SLIDE = auto()

    PREVIOUS_SLIDE = auto()

    START_PRESENTATION = auto()

    PAUSE_PRESENTATION = auto()

    RESUME_PRESENTATION = auto()

    END_PRESENTATION = auto()

    GO_TO_SLIDE = auto()

    QUIT_APPLICATION = auto()