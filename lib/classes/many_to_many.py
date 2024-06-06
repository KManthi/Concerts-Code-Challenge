class Band:
    def __init__(self, name, hometown):
        self.name = name
        self.hometown = hometown

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) > 0:
            self._name = name
        else:
            raise ValueError("Band name must be a non-empty string")
        
    @property
    def hometown(self):
        return self._hometown
    
    @hometown.setter
    def hometown(self, hometown):
        if  not isinstance(hometown, str) and len(hometown) > 0:
            raise ValueError('Band homwtown must be a non-empty string')
        if hasattr(self, '_hometown'):
            raise AttributeError('Band hometown cannot be changed')
        self._hometown = hometown



    def concerts(self):
        pass

    def venues(self):
        pass

    def play_in_venue(self, venue, date):
        pass

    def all_introductions(self):
        pass


class Concert:
    def __init__(self, date, band, venue):
        self.date = date
        self.band = band
        self.venue = venue

    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, date):
        if isinstance(date, str) and len(date) > 0:
            self._date = date
        else:
            raise ValueError("Concert date must be a non-empty string")

    def hometown_show(self):
        pass

    def introduction(self):
        pass


class Venue:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
         if isinstance(name, str) and len(name) > 0:
            self._name = name
         else:
            raise ValueError("Venue name must be a non-empty string")
         
    @property
    def city(self):
        return self._city
    
    @city.setter
    def city(self, city):
        if isinstance(city, str) and len(city) > 0:
            self._city = city
        else:
            raise ValueError("City name must be a non-empty string")

    def concerts(self):
        pass

    def bands(self):
        pass
