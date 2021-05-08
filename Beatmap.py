class BeatmapStats:
    AR: int = 0
    OD: int = 0
    CS: int = 0
    HP: int = 0


class BeatmapObjects:
    circles: int = 0
    sliders: int = 0
    spinners: int = 0


class BeatmapDifficulty:
    stars: float = 0
    aim: float = 0
    speed: float = 0


class Beatmap:
    mode: int = 0
    maxCombo: int = 0
    stats: BeatmapStats
    objects: BeatmapObjects
    difficulty: BeatmapDifficulty
