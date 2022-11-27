class Band:

    def __init__(self, name):
        self.name = name
        self.members = []

    def add(self, musician):
        """Add a musician to a list of members"""
        self.members.append(musician)

    def play(self):
        """For each member in the band, that musician "plays"."""
        return '\n'.join([musician.play() for musician in self.members])

    def __repr__(self):
        return f"{self.name} ({', '.join([str(musician) for musician in self.members])})"
