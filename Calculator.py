from abc import abstractmethod, abstractproperty
from accessify import protected

from Score import ScoreData
from Beatmap import Beatmap
from Mods.Mods import Mods


class PP():
    def __init__(self, SS: float, FC: float, current: float):
        self.SS = SS
        self.FC = FC
        self.PP = current


class Calculator():
    def __init__(self, beatmap: Beatmap, score: ScoreData):
        self.beatmap: Beatmap = beatmap
        self.score: ScoreData = score
        self.mods: Mods = Mods(score.mods)

    @abstractmethod
    def __calcPP(self) -> float:
        pass

    @abstractmethod
    def __calcFC(self) -> float:
        pass

    @abstractmethod
    def __calcSS(self) -> float:
        pass

    def __applyMultiplier(self, multiplier: float, *args):
        sum = 0

        for arg in args:
            sum += pow(arg, 1.1)

        return pow(sum, 1 / 1.1) * multiplier

    def calculate(self) -> PP:
        ss = self.__calcSS()
        fc = self.__calcFC()
        pp = self.__calcPP()

        return PP(ss, fc, pp)