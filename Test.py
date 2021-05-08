from Mods.Mods import Mods
from Calculators.OsuCalculator import OsuCalculator
from Calculator import Calculator
from Beatmap import *
from Score import *

beatmapStats = BeatmapStats()
beatmapStats.AR = 9.2
beatmapStats.CS = 4
beatmapStats.OD = 9
beatmapStats.HP = 6.5

beatmapObjects = BeatmapObjects()
beatmapObjects.circles = 308
beatmapObjects.sliders = 178
beatmapObjects.spinners = 0

beatmapDifficulty = BeatmapDifficulty()
beatmapDifficulty.aim = 2.7849
beatmapDifficulty.speed = 2.50933
beatmapDifficulty.stars = 5.43202

beatmap = Beatmap()
beatmap.mode = 0
beatmap.maxCombo = 680
beatmap.stats = beatmapStats
beatmap.objects = beatmapObjects
beatmap.difficulty = beatmapDifficulty

hitcounts = HitCounts()
hitcounts.hit320 = 0
hitcounts.hit300 = 478
hitcounts.hit200 = 0
hitcounts.hit100 = 8
hitcounts.hit50  = 0
hitcounts.hit0   = 0

score = ScoreData()
score.hitCounts = hitcounts
score.score = 10613660
score.mods = 0
score.combo = 680
score.accuracy = 0.989

pp = OsuCalculator(beatmap, score).calculate()
#should be 244
print(pp.SS)
#should be 212
print(pp.PP)
