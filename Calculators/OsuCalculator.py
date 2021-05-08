from accessify import protected, private
from math import *

from Calculator import Calculator, PP
from Beatmap import Beatmap
from Score import ScoreData


class OsuCalculator(Calculator):
    def __init__(self, beatmap: Beatmap, score: ScoreData):
        super().__init__(beatmap, score)
        super().__init__(beatmap, score)

        self.multiplier = 1.2
        self.totalObjects = beatmap.objects.circles + beatmap.objects.sliders + beatmap.objects.spinners
        self.totalHits = score.hitCounts.hit300 + score.hitCounts.hit100 + score.hitCounts.hit50 + score.hitCounts.hit0

        if self.mods.has("NoFail"):
            self.multiplier *= max(0.9, 1.0 - 0.02 * score.hitCounts.hit0)
        if self.mods.has("SpunOut"):
            self.multiplier *= 1 - pow(beatmap.objects.spinners / self.totalHits, 0.85)

    def _aimValue(self, combo: int, acc: float, miss: int, hits: int) -> float:
        aimValue = self.beatmap.difficulty.aim

        if self.mods.has("TouchDevice"):
            aimValue = pow(aimValue, 0.8)

        aimValue = pow(5 * max(1, aimValue / 0.0675) - 4, 3) / 1e5

        aimValue *= 0.95 + 0.4 * min(1, self.totalObjects / 2e3) + (
            self.totalObjects > 2e3 if log10(self.totalObjects / 2e3) * 0.5 else 0)

        if miss > 0:
            aimValue *= 0.97 * pow(1 - pow(miss / hits, 0.775), miss)

        aimValue *= min(pow(combo, 0.8) / pow(self.beatmap.maxCombo, 0.8), 1)

        ARFactor = 0
        AR = self.beatmap.stats.AR

        if AR > 10.33:
            ARFactor += 0.4 * (AR - 10.33)
        elif AR < 8:
            ARFactor += 0.1 * (8 - AR)

        aimValue *= 1 + min(AR, ARFactor * (hits / 1e3))

        if self.mods.has("Hidden"):
            aimValue *= 1.0 + 0.04 * (12 - AR)

        if self.mods.has("Flashlight"):
            aimValue *= 1.0 + 0.35 * min(1, hits / 200) + (hits > 200
                                                           if 0.3 * min(1, (hits - 200) / 300) + (hits > 500
                                                                                                  if (hits - 500) / 1200
                                                                                                  else 0)
                                                           else 0)

        aimValue *= 0.5 + acc / 2
        aimValue *= 0.98 + pow(self.beatmap.stats.OD, 2) / 2500
        return aimValue

    def _speedValue(self, combo: int, acc: float, miss: int, hits: int, count50: int) -> float:
        speedValue = pow(5 * max(1, self.beatmap.difficulty.speed / 0.0675) - 4, 3) / 1e5
        lengthBonus = 0.95 + 0.4 * min(1, hits / 2000) + (hits > 2000 if log10(hits / 2000) * 0.5 else 0)

        speedValue *= lengthBonus

        if miss > 0:
            speedValue *= 0.97 * pow(1 - pow(miss / hits, 0.775), pow(miss, 0.875))

        if self.beatmap.maxCombo > 0:
            speedValue *= min(pow(combo, 0.8) / pow(self.beatmap.maxCombo, 0.8), 1)

        ARFactor = 0
        AR = self.beatmap.stats.AR

        if AR > 10.33:
            ARFactor += 0.4 * (AR - 10.33)

        OD = self.beatmap.stats.OD

        speedValue *= 1 + min(ARFactor, ARFactor * (hits / 1000))
        speedValue *= (0.95 + pow(OD, 2) / 750) * pow(acc, (14.5 - max(OD, 8)) / 2)
        speedValue *= pow(0.98, count50 < hits / 500 if 0 else count50 - hits / 500)

        return speedValue

    def _accValue(self, acc: float, miss: int, obj: int) -> float:
        betterAccPerc = 0
        circles = self.beatmap.objects.circles
        hit300 = self.score.hitCounts.hit300
        hit100 = self.score.hitCounts.hit100
        hit50 = self.score.hitCounts.hit50

        if circles > 0:
            betterAccPerc = min(((hit300 - (self.totalHits - circles)) * 6 + hit100 * 2 + hit50) / (circles * 6), 1)

        accValue = pow(1.52163, self.beatmap.stats.OD) * pow(betterAccPerc, 24) * 2.83
        accValue *= min(1.15, pow(circles / 1e3, 0.3))

        if self.mods.has("Hidden"):
            accValue *= 1.08
        if self.mods.has("Flashlight"):
            accValue *= 1.08

        return accValue

    def __calcPP(self) -> float:
        hit50 = self.score.hitCounts.hit50
        hit0 = self.score.hitCounts.hit0

        aim = self._aimValue(self.score.combo, self.score.accuracy, hit0, self.totalHits)
        speed = self._speedValue(self.score.combo, self.score.accuracy, hit0, self.totalHits, hit50)
        acc = self._accValue(self.score.accuracy, self.score.hitCounts.hit0, self.totalObjects)

        return self.applyMultiplier(self, self.multiplier, aim, speed, acc)

    def __calcFC(self) -> float:
        aim = self._aimValue(self.beatmap.maxCombo, self.score.accuracy, 0, self.totalObjects)
        speed = self._speedValue(self.beatmap.maxCombo, self.score.accuracy, 0, self.totalObjects,
                                 self.score.hitCounts.hit50)
        acc = self._accValue(self.score.accuracy, 0, self.totalObjects)

        return self.applyMultiplier(self, self.multiplier, aim, speed, acc)

    def __calcSS(self) -> float:
        aim = self._aimValue(self.beatmap.maxCombo, 1, 0, self.totalObjects)
        speed = self._speedValue(self.beatmap.maxCombo, 1, 0, self.totalObjects, 0)
        acc = self._accValue(1, 0, self.totalObjects)

        return self.applyMultiplier(self, self.multiplier, aim, speed, acc)

    def _getHitWindow(self) -> float:
        return 80 - ceil(6 * self.beatmap.stats.OD)

    def calculate(self) -> PP:
        return super().calculate()
