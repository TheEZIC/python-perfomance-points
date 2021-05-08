from accessify import private

class Mod():
    def __init__(self, bitwise: int, name: str, acronym: str):
        self.bitwise: int = bitwise
        self.name: str = name
        self.acronym: str = acronym

class AllMods():    
    _allMods = [
        Mod(0, "NoMod", "NM"),
        Mod(1 << 0, "NoFail", "NF"),
        Mod(1 << 1, "Easy", "EZ"),
        Mod(1 << 2, "TouchDevice", "TD"),
        Mod(1 << 3, "Hidden", "HD"),
        Mod(1 << 4, "HardRock", "HR"),
        Mod(1 << 5, "SuddenDeath", "SD"),
        Mod(1 << 6, "DoubleTime", "DT"),
        Mod(1 << 7, "Relax", "RX"),
        Mod(1 << 8, "HalfTime", "HT"),
        Mod(1 << 9, "NightCore", "NC"),
        Mod(1 << 10, "Flashlight", "FL"),
        Mod(1 << 11, "Autoplay", "AT"),
        Mod(1 << 12, "SpunOut", "SO"),
        Mod(1 << 13, "AutoPilot", "AP"),
        Mod(1 << 14, "Perfect", "PF"),
        Mod(1 << 15, "Key4", "K4"),
        Mod(1 << 16, "Key5", "K5"),
        Mod(1 << 17, "Key6", "K6"),
        Mod(1 << 18, "Key7", "K7"),
        Mod(1 << 19, "Key8", "K8"),
        Mod(1 << 20, "FadeIn", "FI"),
        Mod(1 << 21, "Random", "RN"),
        Mod(1 << 22, "Cinema", "CN"),
        Mod(1 << 23, "Target", "TP"),
        Mod(1 << 24, "Key9", "K9"),
        Mod(1 << 25, "Key10", "KX"),
        Mod(1 << 26, "Key1", "K1"),
        Mod(1 << 27, "Key3", "K3"),
        Mod(1 << 28, "Key2", "K2"),
        Mod(1 << 29, "ScoreV2", "V2"),
        Mod(1 << 30, "Mirror", "MR"),
    ]

    def findByBitwise(self, bitwise: int) -> Mod:
        for mod in self._allMods:
            if (mod.bitwise == bitwise):
                return mod

    def findByName(self, name: str) -> Mod:
        for mod in self._allMods:
            if (mod.name == name):
                return mod

    def findByAcronym(self, acronym: int) -> Mod:
        for mod in self._allMods:
            if (mod.acronym == acronym):
                return mod