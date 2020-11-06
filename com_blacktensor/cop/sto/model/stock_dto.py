import csv
import json
import pandas as pd
from com_blacktensor.ext.db import db, openSession, engine
# from com_blacktensor.ext.routes import Resource

class StockDto(db.Model):
    __tablename__ = 'stock'
    __table_args__={'mysql_collate' : 'utf8_general_ci'}

    date : str = db.Column(db.String(10), primary_key = True, index = True)
    close : int = db.Column(db.Integer)
    volume : int = db.Column(db.Integer)
    keyword : str = db.Column(db.String(10))

    def __init__(self, date, close, volume, keyword):
        self.date = date
        self.close = close
        self.volume = volume
        self.keyword = keyword
    
    def __repr__(self):
        return f'Stock(date={self.date}, close={self.close}, volume={self.volume}, keyword={self.keyword})'

    def __str__(self):
        return f'Stock(date={self.date}, close={self.close}, volume={self.volume}, keyword={self.keyword})'

    def json(self):
        return {
        'date' : self.date,
        'close' : self.close,
        'volume' : self.volume,
        'keyword' : self.keyword
    }

class StockVo:
    date : str = ''
    close : int = 0
    volume : int = 0
    keyword : str = ''