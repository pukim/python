from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:pukimxxx@localhost:3306/total?charset=utf8mb4", echo=True)

