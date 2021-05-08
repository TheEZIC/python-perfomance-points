from abc import abstractmethod, abstractproperty


class HitCounts:
    hit320: int = 0
    hit300: int = 0
    hit200: int = 0
    hit100: int = 0
    hit50: int = 0
    hit0: int = 0


class ScoreData:
    score: int = 0
    combo: int = 0
    accuracy: float = 0
    mods: int = 0
    hitCounts: HitCounts
