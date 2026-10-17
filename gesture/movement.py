class MovementTracker:

    def __init__(self):

        self.previous_position = None
        self.total_horizontal = 0
        self.total_vertical = 0

    def update(self, current_position):

        if self.previous_position is None:

            self.previous_position = current_position

            return None

        movement = (
            current_position[0] - self.previous_position[0],
            current_position[1] - self.previous_position[1]
        )

        self.previous_position = current_position

        self.total_horizontal += movement[0]
        self.total_vertical += movement[1]

        return movement

    def get_total_movement(self):

        return (
            self.total_horizontal,
            self.total_vertical
        )

    def reset(self):

        self.previous_position = None
        self.total_horizontal = 0
        self.total_vertical = 0