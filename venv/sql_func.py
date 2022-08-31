import pymysql
from sqlalchemy import create_engine
import pandas as pd

password = ''


def read_sql_table(talbe_name, db_name):
    '''
    链接本地数据库，并且获取数据
    :param talbe_name: 表名
    :param db_name: 库名
    :return:
    '''
    engine = create_engine("mysql+pymysql://{}:{}@{}:{}/{}".format('root', password, 'localhost', '3306', db_name))
    try:
        pd.read_sql_table(table_name=talbe_name, engine=engine)
        print('{}{}数据读取成功'.format(talbe_name, db_name))
    except:
        print('读取失败')


def write_sql_table(table_name, db_name, df: pd.DataFrame, type='replace'):
    '''
    写入sql table
    :param table_name: 表名
    :param db_name: 库名
    :param df: 需要写入的数据，要求是df格式的数据
    :param type: 默认是先删除原表，然后写入新的数据，如果只是新增数据，则使用:append
    :return:
    '''
    engine = create_engine("mysql+pymysql://{}:{}@{}:{}/{}".format('root', password, 'localhost', '3306', db_name))
    try:
        df.to_sql(table_name, engine, index=False, if_exists=type)
        print('{}{}数据{}成功'.format(talbe_name, db_name, type))
    except:
        print('写入失败')

