import pymysql
from sqlalchemy import create_engine
import pandas as pd


# 初始化数据库连接
# 按实际情况依次填写MySQL的用户名、密码、IP地址、端口、数据库名

engine = create_engine("mysql+pymysql://{}:{}@{}:{}/{}".format('root', '13896766981', 'localhost', '3306', 'testdb'))

# df = pd.read_excel('xiujian.xlsx')

df=pd.DataFrame([{'uid':'a','groupid':'a-3'}])
df.to_sql('testtable', engine, index=False,if_exists='append')
df1 = pd.read_sql_table('water_uid_groupid', engine)
print(df1.head())
