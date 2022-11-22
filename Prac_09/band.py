class Band:

    def __init__(self, name):
        self.name = name
        self.members = []

    def add(self, musician):
        """Add a musician to a list of members"""
        self.members.append(musician)

    def play(self):
        """Calls the play function for each member of the band"""
        for musician in self.members:
            print(musician.play())
