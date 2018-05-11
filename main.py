class Territory:
    COASTAL = 0
    INLAND = 1
    OCEAN = 2
    def __init__(self, name, abbrev, type, hasSupply, control, adjacentTerritories):
        # Name of the territory
        self.name = name
        # Three letter abbreviation of the territory
        self.abbrev = abbrev
        # type = Territory.COASTAL, Territory.INLAND, or Territory.OCEAN
        self.type = type
        # hasSupply = bool, true if the territory has a supply center, otherwise false
        self.hasSupply = hasSupply
        # control = nation which currently has a unit on the territory or the last nation to have had a unit on it
        self.control = control
        # adjacentTerritories = list of all territories which are adjacent to this one (abbreviations)
        self.adjacentTerritories = adjacentTerritories

    def checkName(self, input):
        if input == self.name or input == self.abbrev:
            return True
        return False

    def
