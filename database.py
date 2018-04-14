import datetime
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method

Base = declarative_base()


class Dataset(Base):
  __tablename__ = 'dataset'
  id = Column('id', Integer, primary_key=True)
  name = Column('name', String)
  power_productions = relationship('PowerProduction', backref='power_production')
  battery_percentage_states = relationship('BatteryPercentageState', backref='battery_percentage_state')
  power_feed_ins = relationship('PowerFeedIn', backref='power_feed_in')
  power_self_consumptions = relationship('PowerSelfConsumption', backref='power_self_consumption')
  power_purchaseds = relationship('PowerPurchased', backref='power_purchased')
  power_consumptions = relationship('PowerConsumption', backref='power_consumption')

  # return all timeseriesvalues in power productions array
  @hybrid_property
  def power_production_plots(self):
    return [t.timeseriesvalue for t in self.power_productions]

  # return all timestamps in power productions array
  @hybrid_property
  def power_production_time_plots(self):
    return [str(t.time) for t in self.power_productions]


  # battery percentage state data
  @hybrid_property
  def battery_percentage_state_plots(self):
    return [t.timeseriesvalue for t in self.battery_percentage_states]

  @hybrid_property
  def battery_percentage_state_time_plots(self):
    return [str(t.time) for t in self.battery_percentage_states]

  # power feed in data
  @hybrid_property
  def power_feed_in_plots(self):
    return [t.timeseriesvalue for t in self.power_feed_ins]

  @hybrid_property
  def power_feed_in_time_plots(self):
    return [str(t.time) for t in self.power_feed_ins]

  # power self consumption
  @hybrid_property
  def power_self_consumption_plots(self):
    return [t.timeseriesvalue for t in self.power_self_consumptions]

  @hybrid_property
  def power_self_consumption_time_plots(self):
    return [str(t.time) for t in self.power_self_consumptions]

  # power purchased
  @hybrid_property
  def power_purchased_plots(self):
    return [t.timeseriesvalue for t in self.power_purchaseds]

  @hybrid_property
  def power_purchased_time_plots(self):
    return [str(t.time) for t in self.power_purchaseds]

  # power consumptions
  @hybrid_property
  def power_consumption_plots(self):
    return [t.timeseriesvalue for t in self.power_consumptions]

  @hybrid_property
  def power_consumption_time_plots(self):
    return [str(t.time) for t in self.power_consumptions]


class PowerProduction(Base):
  __tablename__ = 'power_production'
  id = Column(Integer, primary_key=True)
  timeseriesvalue = Column(Float)
  time = Column(DateTime)
  dataset_id = Column(Integer, ForeignKey('dataset.id'))
  dataset = relationship('Dataset', back_populates='power_productions')


class BatteryPercentageState(Base):
  __tablename__ = 'battery_percentage_state'
  id = Column('id', Integer, primary_key=True)
  timeseriesvalue = Column(Float)
  time = Column(DateTime)
  dataset_id = Column(Integer, ForeignKey('dataset.id'))
  dataset = relationship('Dataset', back_populates='battery_percentage_states')


class PowerFeedIn(Base):
  __tablename__ = 'power_feed_in'
  id = Column('id', Integer, primary_key=True)
  timeseriesvalue = Column(Float)
  time = Column(DateTime)
  dataset_id = Column(Integer, ForeignKey('dataset.id'))
  dataset = relationship('Dataset', back_populates='power_feed_ins')


class PowerSelfConsumption(Base):
  __tablename__ = 'power_self_consumption'
  id = Column('id', Integer, primary_key=True)
  timeseriesvalue = Column(Float)
  time = Column(DateTime)
  dataset_id = Column(Integer, ForeignKey('dataset.id'))
  dataset = relationship('Dataset', back_populates='power_self_consumptions')


class PowerPurchased(Base):
  __tablename__ = 'power_purchased'
  id = Column('id', Integer, primary_key=True)
  timeseriesvalue = Column(Float)
  time = Column(DateTime)
  dataset_id = Column(Integer, ForeignKey('dataset.id'))
  dataset = relationship('Dataset', back_populates='power_purchaseds')


class PowerConsumption(Base):
  __tablename__ = 'power_consumption'
  id = Column('id', Integer, primary_key=True)
  timeseriesvalue = Column(Float)
  time = Column(DateTime)
  dataset_id = Column(Integer, ForeignKey('dataset.id'))
  dataset = relationship('Dataset', back_populates='power_consumptions')

engine = create_engine('sqlite:///duckworth.db', echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)

session = Session()
