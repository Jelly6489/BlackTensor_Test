# import sys
# sys.path.insert(0, '/c/Users/Admin/VscProject/BlackTensor_Test/com_blacktensor/cop/fin/model/')
import csv
import pandas as pd
from com_blacktensor.ext.db import db, openSession, engine
from com_blacktensor.cop.fin.model.finance_dto import FinanceDto
from sqlalchemy import func

Session = openSession()
session = Session()

class FinanceDao(FinanceDto):
    
    @classmethod
    def bulk(cls, finance_dfo):
        dfo = finance_dfo.fina_pro()
        print('---------FinanceDao------------')
        print(f'[ FinanceDao ] {dfo.head()}')
        session.bulk_insert_mappings(cls, dfo.to_dict(orient="records"))
        session.commit()
        session.close()
        # Session = openSession()
        # session = Session()
        # stock_df = StockDf()
        # df = stock_df.hook()
        # print(df.head())
        # session.bulk_insert_mappings(StockDto, df.to_dict(orient='records'))
        # session.commit()
        # session.close()
    # @staticmethod
    # def save(finance):
    #     session.add(finance)
    #     session.commit()
    
    @classmethod
    def count(cls):
        return session.query(func.count(cls.no)).one()

    @classmethod
    def find_all(cls):

        result = session.query(FinanceDto).all()
        session.close()

        return result

# ===========================================================================

    # @staticmethod
    # def count():
    #     return session.query(func.count(StockDto.date)).one()

    # @staticmethod
    # def save(stock):
    #     new_stock = StockDto(date = stock['date'],
    #                        keyword = stock['keyword'],
    #                        close = stock['close'],
    #                        volume = stock['volume'])
    #     session.add(new_stock)
    #     session.commit()

# if __name__ == '__main__':
#     FinanceDao.bulk()