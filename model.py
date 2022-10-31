import pandas as pd
import pymysql
from sqlalchemy import create_engine

df = pd.read_csv('klook.csv')
df = pd.read_csv('klook.csv', names=['img_scr', 'title', 'place', 'tag'] ,header=0)

# 데이터 전처리
df = df.dropna(axis=0)

df = df.astype('string')
df = df.drop_duplicates()

df['title'] = df['title'].str.replace('\[한국관광 품질인증/Korea Quality]', '')
df['title'] = df['title'].str.replace('\[유네스코 세계유산]', '')
df['title'] = df['title'].str.replace('\[유네스코 세계문화유산]', '')
df['title'] = df['title'].str.replace('\[한국관광품질인증/Korea Quality]', '')

dr = df[df['img_scr'].str.contains('undefined')].index

df.drop(dr, inplace=True)

df['title'] = df['title'].str.strip()
df['tag'] = df['tag'].str.strip()
df.columns = df.columns.str.replace(' ', '')

df_2 = df.copy()

df_2.drop(df.index[355],inplace=True)

df_2['tag'] = df_2['tag'].str.replace('#', ' ')
df_2['tag'] = df_2['tag'].str.lstrip()

pymysql.install_as_MySQLdb()
import MySQLdb

# conn = pymysql.connect(
#     host='localhost',
#     user='root',
#     password='password',
#     db='klook',
#     charset='utf8'
# )
# cur = conn.cursor()

# # mysql insret
# cur.execute("DROP TABLE IF EXISTS travelinfo;")
DB_CONNECT_PATH = 'mysql+pymysql://root:password@localhost/klook?charset=utf8'

engine = create_engine(DB_CONNECT_PATH)
conn = engine.connect()

df_2.to_sql(name='travelinfo', con=engine, if_exists='append')