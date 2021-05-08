from typing import List
from accessify import private
from Mods.AllMods import AllMods


class Mods:
    _allMods = AllMods()
    mods: List[int]

    def __init__(self, mods):
        if type(mods) is int:
            self.mods = self._fromNumber(mods)
        else:
            self.mods = self._fromString(mods)

    @private
    def _fromNumber(self, modsNumber: int) -> List[int]:
        temp = [];

        for i in range(31):
            if (modsNumber & (1 << i)):
                temp.append(1 << i)

        return temp

    @private
    def _fromString(self, modsString: str) -> List[int]:
        offset = 0
        buffer = ""
        mods = 0

        while offset < len(modsString):
            buffer += modsString[offset][:2]
            upperBuffer = buffer.upper()
            mod = self._allMods.findByAcronym(upperBuffer)

            if (mod):
                if not (mods & mod.bitwise):
                    mods += mod.bitwise

                buffer = ""

            offset += 1

        return self._fromNumber(mods)

    def has(self, mod: str) -> bool:
        mod1 = self._allMods.findByName(mod)
        mod2 = self._allMods.findByAcronym(mod)

        if mod1:
            return mod1.bitwise in self.mods

        if mod2:
            return mod2.bitwise in self.mods

        return False