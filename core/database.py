from sqlalchemy import Integer, create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base


# Veritabanı motoru
engine = create_engine('sqlite:///userbot.db')

# ORM taban sınıfı
Base = declarative_base()

# Kullanici tablosunu temsil eden sınıf
class Environment(Base):
    __tablename__ = 'envs'
    id = Column(Integer, primary_key=True, autoincrement=True)
    started_time = Column(String)

# Veritabanı tablolarını oluştur
Base.metadata.create_all(engine)
