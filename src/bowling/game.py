from . import FRAME_QUANTITY
from functools import reduce
from typing import List

from bowling.frame import Frame


class BowlingGame:
    frames: List[Frame]
    bonus: Frame

    def __init__(self) -> None:
        self.frames = []
        self.bonus = Frame(0, 0)

    def add_frame(self, frame: Frame):
        """ Add a frame to the game """
        if self.is_next_frame_bonus():
            self.set_bonus(frame.first_throw, frame.second_throw)
            return

        self.frames.append(frame)

    def set_bonus(self, first_throw: int, second_throw: int):
        """ The the bonus throw """
        self.bonus = Frame(first_throw, second_throw)

    def score(self) -> int:
        """ Get the score from the game """
        score = 0
        for i in range(FRAME_QUANTITY):
            frame = self.frames[i]
            next_frame = (
                self.frames[i+1]
                if i < FRAME_QUANTITY - 1
                else self.bonus
            )
            second_next_frame = (
                self.frames[i+2]
                if i < FRAME_QUANTITY - 2
                else self.bonus
            )

            score = (
                score +
                self.frame_score(frame, next_frame, second_next_frame)
            )

        return score

    def frame_score(self, frame: Frame, next_frame: Frame, second_next_frame: Frame):
        score = frame.score()

        if(frame.is_strike()):
            score = score + next_frame.score()

            if (next_frame.is_strike()):
                score = score + second_next_frame.first_throw

        if(frame.is_spare()):
            score = score + next_frame.first_throw
        return score

    def is_next_frame_bonus(self) -> bool:
        """ Get if the next frame is bonus """
        return len(self.frames) == FRAME_QUANTITY
