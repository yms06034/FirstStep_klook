import pandas as pd
import pymysql

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

df_2['tag'] = df_2['tag'].str.replace('#', ' ')
df_2['tag'] = df_2['tag'].str.lstrip()

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='password',
    db='klook',
    charset='utf8'
)
cur = conn.cursor()

# mysql insret
cur.execute("DROP TABLE IF EXISTS travelinfo;")

t_c_travelinfo = cur.execute ("""CREATE TABLE travelinfo (
    id INT NOT NILL AUTO_INCREMENT,
    img VARCHAR(255) NOT NULL,
    place VARCHAR(255) NOT NULL,
    tag VARCHAR(255), NOT NULL,
    PRIMARY KEY (id)
);
""")

