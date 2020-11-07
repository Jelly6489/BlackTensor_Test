import csv
import pandas as pd
# # from sqlalchemy import create_engine
from com_blacktensor.ext.db import db, openSession, engine
from sqlalchemy import func
from com_blacktensor.util.file_handler import FileHandler
# from com_blacktensor.ext.routes import Resource

class StockDfo(object):
    def __init__(self, colums):
        self.fileHandler = FileHandler()  
        self.colums = colums

    def get_df(self, data):
        return pd.DataFrame(data, columns=self.colums)