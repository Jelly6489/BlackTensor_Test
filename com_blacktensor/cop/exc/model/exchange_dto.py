import csv
import json
import pandas as pd
from com_blacktensor.ext.db import db, openSession, engine
# from com_blacktensor.ext.routes import Resource

class ExchangeDto(db.Model):
    __tablename__ = 'exchange'
    __table_args__={'mysql_collate' : 'utf8_general_ci'}
    no : int = db.Column(db.Integer, primary_key = True, index = True)
    date : str = db.Column(db.String(10))
    usd : float = db.Column(db.Float)
    jpy : float = db.Column(db.Float)
    eur : float = db.Column(db.Float)
    cny : float = db.Column(db.Float)

    # def __init__(self, no, date, close, volume, keyword):
    #     self.no = no
    #     self.date = date
    #     self.close = close
    #     self.volume = volume
    #     self.keyword = keyword
    
    def __repr__(self):
        return f'Stock(no={self.no}, date={self.date}, usd={self.usd}, jpy={self.jpy}, eur={self.eur}, cny={self.cny})'

    def __str__(self):
        return f'Stock(no={self.no}, date={self.date}, usd={self.usd}, jpy={self.jpy}, eur={self.eur}, cny={self.cny})'

    @property
    def json(self):
        return {
        'no' : self.no,
        'date' : self.date,
        'usd' : self.usd,
        'jpy' : self.jpy,
        'eur' : self.eur,
        'cny' : self.cny
    }

class StockVo:
    no : int = 0
    date : str = ''
    usd : float = 0
    jpy : float = 0
    eur : float = 0
    cny : float = 0