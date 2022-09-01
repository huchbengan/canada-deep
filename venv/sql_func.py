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
    if password:
        engine = create_engine("mysql+pymysql://{}:{}@{}:{}/{}".format('root', password, 'localhost', '3306', db_name))
        try:
            df = pd.read_sql_table(table_name=talbe_name, con=engine)
            print('库:{} 表:{}数据读取成功'.format(talbe_name, db_name))
            return df
        except:
            print('读取失败')
    else:
        raise 'mysql密码为空'


def write_sql_table(table_name, db_name, df: pd.DataFrame, type='replace'):
    '''
    写入sql table
    :param table_name: 表名
    :param db_name: 库名
    :param df: 需要写入的数据，要求是df格式的数据
    :param type: 默认是先删除原表，然后写入新的数据，如果只是新增数据，则使用:append
    :return:
    '''
    if password:
        engine = create_engine("mysql+pymysql://{}:{}@{}:{}/{}".format('root', password, 'localhost', '3306', db_name))
        try:
            df.to_sql(name=table_name, con=engine, index=False, if_exists=type)
            print('{}{}数据{}成功'.format(table_name, db_name, type))
        except:
            print('写入失败')
    else:
        raise 'mysql密码为空'
    # df.to_sql(name=table_name, con=engine, index=False, if_exists=type)
    # print('{}{}数据{}成功'.format(table_name, db_name, type))


if __name__=="__main__":

    # df = pd.read_excel('浇水分类代表物种ID.xlsx',sheet_name='全物种类群分类ID')
    df = pd.DataFrame([{'uid':1,'groupid':'cwater0002'}])
    write_sql_table(table_name='test_water',db_name='testdb',df=df)
