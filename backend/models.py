from sqlalchemy import create_engine, Column, Integer, String, Float
from config import db

class MostWicketsAllSeasons(db.Model):
    __tablename__ = 'MostWicketsAllSeasonsCombine'  

    c2 = Column(String(100), primary_key=True, nullable=False)
    c3 = Column(Integer, nullable=False)
    c4 = Column(String(100), nullable=False)
    c5 = Column(String(100), nullable=False)
    c6 = Column(String(100), nullable=False)
    c7 = Column(String(100), nullable=False)
    c9 = Column(String(100), nullable=False)
    c10 = Column(String(100), nullable=False)
    c11 = Column(String(100), nullable=False)
    c12 = Column(String(100), nullable=False)
    c13 = Column(String(100), nullable=False)

    def to_dict(self):
        return {
            'Player': self.c2,
            'Matches': self.c3,
            'Inns': self.c4,
            'Overs': self.c5,
            'Runs': self.c6,
            'Wickets': self.c7,
            'Avg': self.c9,
            'Eco': self.c10,
            'SR': self.c11,
            '4W': self.c12,
            '5W' : self.c13        
        }
    
class MostSixesAllSeasonsCombined(db.Model):
    __tablename__ = 'MostSixesInnings'  

    c2 = Column(String(100), primary_key=True, nullable=False)
    c3 = Column(String(100), nullable=False)
    c4 = Column(String(100), nullable=False)
    c5 = Column(String(100), nullable=False)
    c6 = Column(Integer, nullable=False)
    c7 = Column(Integer, nullable=False)
    c8 = Column(Float, nullable=False)
    c9 = Column(Integer, nullable=False)
    c10 = Column(Integer, nullable=False)

    def to_dict(self):
        return {
            'Player': self.c2,
            'Runs': self.c3,
            'BF': self.c4,
            'SR': self.c5,
            '4s': self.c6,
            '6s': self.c7,
            'Against': self.c8,
            'Venue': self.c9,
            'MatchDate': self.c10
        }

class MostRunsConcededPerInningsAllSeasonsCombine(db.Model):
    __tablename__ = 'MostRunsConcededPerInningsAllSeasonsCombine'  

    c2 = Column(String(100), primary_key=True, nullable=False)
    c3 = Column(Integer, nullable=False)
    c4 = Column(String(100), nullable=False)
    c5 = Column(String(100), nullable=False)
    c6 = Column(String(100), nullable=False)
    c7 = Column(String(100), nullable=False)
    c8 = Column(String(100), nullable=False)
    c9 = Column(String(100), nullable=False)

    def to_dict(self):
        return {
            'Player': self.c2,
            'Overs': self.c3,
            'Runs': self.c4,
            'Wickets': self.c5,
            'SR': self.c6,
            'Against': self.c7,
            'Venue' : self.c8,
            'Match Date': self.c9    
        }
    

class MostRunsPerOverAllSeasonsCombine(db.Model):
    __tablename__ = 'MostRunsPerOverAllSeasonsCombine'  

    c2 = Column(String(100), primary_key=True, nullable=False)
    c3 = Column(String(100), nullable=False)
    c4 = Column(String(100), nullable=False)
    c5 = Column(String(100), nullable=False)
    c6 = Column(String(100), nullable=False)
    c7 = Column(String(100), nullable=False)
    c8 = Column(String(100), nullable=False)
    c9 = Column(String(100), nullable=False)
    c10 = Column(String(100), nullable=False)

    def to_dict(self):
        return {
            'Player': self.c2,
            'Runs': self.c3,
            'BF': self.c4,
            'SR': self.c5,
            '4s': self.c6,
            '6s': self.c7,
            'Against': self.c8,
            'Venue': self.c9,
            'Match Date': self.c10 
        }

class MostRunsAllSeasonsCombine(db.Model):
    __tablename__ = 'MostRunsAllSeasonsCombine'  

    c2 = Column(String(100), primary_key=True, nullable=False)
    c3 = Column(String(100), nullable=False)
    c4 = Column(String(100), nullable=False)
    c5 = Column(String(100), nullable=False)
    c6 = Column(String(100), nullable=False)
    c7 = Column(String(100), nullable=False)
    c8 = Column(String(100), nullable=False)
    c9 = Column(String(100), nullable=False)
    c10 = Column(String(100), nullable=False)
    c11 = Column(String(100), nullable=False)
    c12 = Column(String(100), nullable=False)
    c13 = Column(String(100), nullable=False)
    c14 = Column(String(100), nullable=False)

    def to_dict(self):
        return {
            'Player': self.c2,
            'Matches': self.c3,
            'Inns': self.c4,
            'NO': self.c5,
            'Runs': self.c6,
            'HS': self.c7,
            'Avg' : self.c8,
            'BF' : self.c9,
            'SR' : self.c10,
            '100' : self.c11,
            '50' : self.c12,
            '4s' : self.c13,
            '6s' : self.c14
        }
    
class MostFoursPerInningsAllSeasonsCombine(db.Model):
    __tablename__ = 'MostFoursPerInningsAllSeasonsCombine'  

    c2 = Column(String(100), primary_key=True, nullable=False)
    c3 = Column(String(100), nullable=False)
    c4 = Column(String(100), nullable=False)
    c5 = Column(String(100), nullable=False)
    c6 = Column(Integer, nullable=False)
    c7 = Column(Integer, nullable=False)
    c8 = Column(Float, nullable=False)
    c9 = Column(Integer, nullable=False)
    c10 = Column(Integer, nullable=False)

    def to_dict(self):
        return {
            'Player': self.c2,
            'Runs': self.c3,
            'BF': self.c4,
            'SR': self.c5,
            '4s': self.c6,
            '6s': self.c7,
            'Against': self.c8,
            'Venue': self.c9,
            'MatchDate': self.c10
        }


class FastestCenturiesAllSeasonsCombine(db.Model):
    __tablename__ = 'FastestCenturiesAllSeasonsCombine'  

    c2 = Column(String(100), primary_key=True, nullable=False)
    c3 = Column(String(100), nullable=False)
    c4 = Column(String(100), nullable=False)
    c5 = Column(Integer, nullable=False)
    c6 = Column(Integer, nullable=False)
    c7 = Column(Float, nullable=False)
    c8 = Column(Integer, nullable=False)
    c9 = Column(Integer, nullable=False)

    def to_dict(self):
        return {
            'Player': self.c2,
            'Runs': self.c3,
            'BF': self.c4,
            '4s': self.c5,
            '6s': self.c6,
            'Against': self.c7,
            'Venue': self.c8,
            'MatchDate': self.c9
        }

class FastestFiftiesAllSeasonsCombine(db.Model):
    __tablename__ = 'FastestFiftiesAllSeasonsCombine'  

    c2 = Column(String(100), primary_key=True, nullable=False)
    c3 = Column(String(100), nullable=False)
    c4 = Column(String(100), nullable=False)
    c5 = Column(Integer, nullable=False)
    c6 = Column(Integer, nullable=False)
    c7 = Column(Float, nullable=False)
    c8 = Column(Integer, nullable=False)
    c9 = Column(Integer, nullable=False)

    def to_dict(self):
        return {
            'Player': self.c2,
            'Runs': self.c3,
            'BF': self.c4,
            '4s': self.c5,
            '6s': self.c6,
            'Against': self.c7,
            'Venue': self.c8,
            'MatchDate': self.c9
        }

class MostDotBallsPerInnings(db.Model):
    __tablename__ = 'MostDotBallsPerInningsAllSeasonsCombine'

    c2 = Column(String(100), primary_key=True, nullable=False)
    c3 = Column(Integer, nullable=False)
    c4 = Column(String(100), nullable=False)
    c5 = Column(String(100), nullable=False)
    c6 = Column(String(100), nullable=False)
    c7 = Column(String(100), nullable=False)
    c8 = Column(String(100), nullable=False)
    c9 = Column(String(100), nullable=False)
    c10 = Column(String(100), nullable=False)
    c11 = Column(String(100), nullable=False)

    def to_dict(self):
        return {
            'Player': self.c2,
            'Overs': self.c3,
            'Runs': self.c4,
            'Wickets': self.c5,
            'Maid': self.c6,
            'Dots' : self.c7 , 
            'SR' : self.c8 , 
            'Against': self.c9,
            'Venue' : self.c10,
            'Match Date': self.c11    
        }

class BestBowlingStrikeRatePerInningsAllSeasonsCombine(db.Model):
    __tablename__ = 'BestBowlingStrikeRatePerInningsAllSeasonsCombine'  

    c2 = Column(String(100), primary_key=True, nullable=False)
    c3 = Column(Integer, nullable=False)
    c4 = Column(String(100), nullable=False)
    c5 = Column(String(100), nullable=False)
    c6 = Column(String(100), nullable=False)
    c7 = Column(String(100), nullable=False)
    c8 = Column(String(100), nullable=False)

    def to_dict(self):
        return {
            'Player': self.c2,
            'Overs': self.c3,
            'Runs': self.c4,
            'Wickets': self.c5,
            'SR': self.c6,
            'Against': self.c7,
            'Venue' : self.c8  
        }

class BestBowlingEconomyPerInningsAllSeasonsCombine(db.Model):
    __tablename__ = 'BestBowlingEconomyPerInningsAllSeasonsCombine'  

    c2 = Column(String(100), primary_key=True, nullable=False)
    c3 = Column(String(100), nullable=False)
    c4 = Column(String(100), nullable=False)
    c5 = Column(String(100), nullable=False)
    c6 = Column(String(100), nullable=False)
    c7 = Column(String(100), nullable=False)
    c8 = Column(String(100), nullable=False)
    c9 = Column(String(100), nullable=False)
    c10 = Column(String(100), nullable=False)
    c11 = Column(String(100), nullable=False)

    def to_dict(self):
        return {
            'Player': self.c2,
            'Overs': self.c3,
            'Runs': self.c4,
            'Wickets': self.c5,
            'Dots': self.c6,
            'Economy': self.c7,
            'SR': self.c8,
            'Against': self.c9,
            'Venue': self.c10,
            'Match Date': self.c11,     
        }


