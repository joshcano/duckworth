from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method

Base = declarative_base()

class Dataset(Base):
  __tablename__ = 'dataset'
  id = column('id', Integer, primary_key=True)
  name = column('name', String)
  power_productions = relationship('PowerProduction', backref='power_production')
  battery_percentage_states = relationship('BatteryPercentageState', backref='battery_percentage_state')
  power_feed_ins = relationship('PowerFeedIn', backref='power_feed_in')
  power_self_consumptions = relationship('PoserSelfConsumption', backref='power_self_consumption')
  power_purchaseds = relationship('PowerPurchased', backref='power_purchased')
  power_consumptions = relationship('PowerConsumption', backref='power_consumption')

class PowerProduction(Base):
  __tablename__ = 'powerproduction'
  id = column('id', Integer, primary_key=True)
  timeseriesvalue = Column(Float)
  time = Column(DateTime)
  dataset_id = Column(Integer, ForeignKey('dataset.id'))
  dataset = relationship('Dataset', back_populates='power_plots')

class BatteryPercentageState(Base):
  __tablename__ = 'batterypercentagestate'
  id = column('id', Integer, primary_key=True)
  timeseriesvalue = Column(Float)
  time = Column(DateTime)
  dataset_id = Column(Integer, ForeignKey('dataset.id'))
  dataset = relationship('Dataset', back_populates='power_plots')

class PowerFeedIn(Base):
  __tablename__ = 'powerfeedin'
  id = column('id', Integer, primary_key=True)
  timeseriesvalue = Column(Float)
  time = Column(DateTime)
  dataset_id = Column(Integer, ForeignKey('dataset.id'))
  dataset = relationship('Dataset', back_populates='power_plots')

class PowerSelfConsumption(Base):
  __tablename__ = 'powerselfconsumption'
  id = column('id', Integer, primary_key=True)
  timeseriesvalue = Column(Float)
  time = Column(DateTime)
  dataset_id = Column(Integer, ForeignKey('dataset.id'))
  dataset = relationship('Dataset', back_populates='power_plots')

class PowerPurchased(Base):
  __tablename__ = 'powerpurchased'
  id = column('id', Integer, primary_key=True)
  timeseriesvalue = Column(Float)
  time = Column(DateTime)
  dataset_id = Column(Integer, ForeignKey('dataset.id'))
  dataset = relationship('Dataset', back_populates='power_plots')

class PowerConsumption(Base):
  __tablename__ = 'powerconsumption'
  id = column('id', Integer, primary_key=True)
  timeseriesvalue = Column(Float)
  time = Column(DateTime)
  dataset_id = Column(Integer, ForeignKey('dataset.id'))
  dataset = relationship('Dataset', back_populates='power_plots')
  

engine = create_engine('sqlite:///duckworth.db', echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)

session = Session()
