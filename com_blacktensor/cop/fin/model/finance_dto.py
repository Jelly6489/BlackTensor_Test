import csv
import json
import pandas as pd
from com_blacktensor.ext.db import db, openSession, engine
# from com_blacktensor.ext.routes import Resource

class FinanceDto(db.Model):
    __tablename__ = 'finance'
    __table_args__={'mysql_collate' : 'utf8_general_ci'}

    name : str = db.Column(db.String(10), primary_key = True, index = True)
    f_2015_12 : int = db.Column(db.Integer)
    f_2016_12 : int = db.Column(db.Integer)
    f_2017_12 : int = db.Column(db.Integer)
    f_2018_12 : int = db.Column(db.Integer)
    f_2019_12 : int = db.Column(db.Integer)
    f_2020_12 : int = db.Column(db.Integer)
    f_2021_12 : int = db.Column(db.Integer)
    f_2022_12 : int = db.Column(db.Integer)
    keyword : str = db.Column(db.String(10))

    def __init__(self, name, f_2015_12, f_2016_12, f_2017_12, f_2018_12, f_2019_12, f_2020_12, f_2021_12, f_2022_12, keyword):
        self.name = name
        self.f_2015_12 = f_2015_12
        self.f_2016_12 = f_2016_12
        self.f_2017_12 = f_2017_12
        self.f_2018_12 = f_2018_12
        self.f_2019_12 = f_2019_12
        self.f_2020_12 = f_2020_12
        self.f_2021_12 = f_2021_12
        self.f_2022_12 = f_2022_12
        self.keyword = keyword
    
    def __repr__(self):
        return f'Finance(name={self.name}, f_2015_12={self.f_2015_12}, f_2016_12={self.f_2016_12}, f_2017_12={self.f_2017_12},\
            f_2018_12={self.f_2018_12}, f_2019_12={self.f_2019_12}, f_2020_12={self.f_2020_12}, f_2021_12={self.f_2021_12},\
            f_2022_12={self.f_2022_12}, keyword={self.keyword})'

    def __str__(self):
        return f'Finance(name={self.name}, f_2015_12={self.f_2015_12}, f_2016_12={self.f_2016_12}, f_2017_12={self.f_2017_12},\
            f_2018_12={self.f_2018_12}, f_2019_12={self.f_2019_12}, f_2020_12={self.f_2020_12}, f_2021_12={self.f_2021_12},\
            f_2022_12={self.f_2022_12}, keyword={self.keyword})'

    def json(self):
        return {
        'name' : self.name,
        'f_2015_12' : self.f_2015_12,
        'f_2016_12' : self.f_2016_12,
        'f_2017_12' : self.f_2017_12,
        'f_2018_12' : self.f_2018_12,
        'f_2019_12' : self.f_2019_12,
        'f_2020_12' : self.f_2020_12,
        'f_2021_12' : self.f_2021_12,
        'f_2022_12' : self.f_2022_12,
        'keyword' : self.keyword
    }

class FinanceVo:
    name : str = ''
    f_2015_12 : int = 0
    f_2016_12 : int = 0
    f_2017_12 : int = 0
    f_2018_12 : int = 0
    f_2019_12 : int = 0
    f_2020_12 : int = 0
    f_2021_12 : int = 0
    f_2022_12 : int = 0
    keyword : str = ''