class SpaceAge:
    def __init__(self, seconds):
        self.second = seconds
        self.day_seconds = self.second / 60 / 60 / 24
        self.Earth = 365.25
        self.Mercury = 0.2408467 * self.Earth
        self.Venus = 0.61519726 * 365.25
        self.Mars = 1.8808158 * 365.25
        self.Jupiter = 11.862615 * 365.25
        self.Saturn = 29.447498 * 365.25
        self.Uranus = 84.016846 * 365.25
        self.Neptune = 164.79132 * 365.25


    def on_earth(self):
        return round(self.day_seconds/self.Earth, 2)


    def on_mercury(self):
        return round(self.day_seconds / self.Mercury, 2)


    def on_venus(self):
        return round(self.day_seconds / self.Venus, 2)


    def on_mars(self):
        return round(self.day_seconds / self.Mars, 2)


    def on_jupiter(self):
        return round(self.day_seconds / self.Jupiter, 2)


    def on_saturn(self):
        return round(self.day_seconds / self.Saturn, 2)


    def on_uranus(self):
        return round(self.day_seconds / self.Uranus, 2)


    def on_neptune(self):
        return round(self.day_seconds / self.Neptune, 2)        
