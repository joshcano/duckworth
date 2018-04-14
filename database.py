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
  power_productions = relationship('PowerProduction', backref='power_production', lazy='dynamic')
  battery_percentage_states = relationship('BatteryPercentageState', backref='battery_percentage_state', lazy='dynamic')
  power_feed_ins = relationship('PowerFeedIn', backref='power_feed_in', lazy='dynamic')
  power_self_consumptions = relationship('PowerSelfConsumption', backref='power_self_consumption', lazy='dynamic')
  power_purchaseds = relationship('PowerPurchased', backref='power_purchased', lazy='dynamic')
  power_consumptions = relationship('PowerConsumption', backref='power_consumption', lazy='dynamic')

  # return all timeseriesvalues in power productions array
  @hybrid_property
  def power_production_plots(self):
    return [t.timeseriesvalue for t in self.power_productions.order_by('time')]

  # return all timestamps in power productions array
  @hybrid_property
  def power_production_time_plots(self):
    return [str(t.time) for t in self.power_productions.order_by('time')]

  # battery percentage state data
  @hybrid_property
  def battery_percentage_state_plots(self):
    return [t.timeseriesvalue for t in self.battery_percentage_states.order_by('time')]

  @hybrid_property
  def battery_percentage_state_time_plots(self):
    return [str(t.time) for t in self.battery_percentage_states.order_by('time')]

  # power feed in data
  @hybrid_property
  def power_feed_in_plots(self):
    return [t.timeseriesvalue for t in self.power_feed_ins.order_by('time')]

  @hybrid_property
  def power_feed_in_time_plots(self):
    return [str(t.time) for t in self.power_feed_ins.order_by('time')]

  # power self consumption
  @hybrid_property
  def power_self_consumption_plots(self):
    return [t.timeseriesvalue for t in self.power_self_consumptions.order_by('time')]

  @hybrid_property
  def power_self_consumption_time_plots(self):
    return [str(t.time) for t in self.power_self_consumptions.order_by('time')]

  # power purchased
  @hybrid_property
  def power_purchased_plots(self):
    return [t.timeseriesvalue for t in self.power_purchaseds.order_by('time')]

  @hybrid_property
  def power_purchased_time_plots(self):
    return [str(t.time) for t in self.power_purchaseds.order_by('time')]

  # power consumptions
  @hybrid_property
  def power_consumption_plots(self):
    return [t.timeseriesvalue for t in self.power_consumptions.order_by('time')]

  @hybrid_property
  def power_consumption_time_plots(self):
    return [str(t.time) for t in self.power_consumptions.order_by('time')]


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


# 2018-04-14 17:58:22,560 INFO sqlalchemy.engine.base.Engine (1,)
# ['2017-08-31 17:15:00', '2017-08-31 17:45:00', '2017-08-31 19:30:00', '2017-11-01 06:15:00', '2017-12-06 04:45:00', '2017-12-06 05:00:00', '2017-12-06 08:30:00', '2017-12-06 08:45:00', '2017-12-06 10:30:00', '2017-12-06 10:45:00', '2017-12-06 11:45:00', '2017-12-06 12:00:00', '2017-12-06 14:00:00', '2017-12-06 14:30:00', '2017-12-06 17:00:00', '2017-12-06 19:00:00', '2017-12-06 22:00:00', '2017-12-07 00:15:00', '2017-12-07 00:30:00', '2017-12-07 01:15:00', '2017-12-07 03:15:00', '2017-12-07 08:15:00', '2017-12-07 09:15:00', '2017-12-07 09:45:00', '2017-12-07 10:45:00', '2017-12-07 13:15:00', '2017-12-07 16:15:00', '2017-12-07 16:45:00', '2017-12-07 17:15:00', '2017-12-07 17:30:00', '2017-12-20 06:15:00', '2017-12-20 08:00:00', '2017-12-20 08:15:00', '2017-12-20 09:30:00', '2017-12-20 09:45:00', '2017-12-20 10:00:00', '2017-12-20 10:15:00', '2017-12-20 11:15:00', '2017-12-20 11:30:00', '2017-12-20 14:45:00', '2017-12-20 15:00:00', '2017-12-20 15:30:00', '2017-12-20 16:30:00', '2017-12-20 20:30:00', '2017-12-20 21:30:00', '2017-12-20 22:45:00', '2017-12-20 23:45:00', '2017-12-21 00:00:00', '2017-12-21 03:00:00', '2017-12-21 03:30:00', '2017-12-21 04:15:00', '2017-12-21 05:45:00', '2017-12-21 06:30:00', '2017-12-21 07:00:00', '2017-12-21 08:00:00', '2017-12-21 08:30:00', '2017-12-21 09:00:00', '2017-12-21 10:30:00', '2017-12-21 14:00:00', '2017-12-21 16:15:00', '2017-12-21 16:45:00', '2017-12-21 17:45:00', '2017-12-21 18:45:00', '2017-12-26 13:00:00', '2017-12-26 14:00:00', '2017-12-26 14:15:00', '2017-12-26 15:45:00', '2017-12-26 17:15:00', '2017-12-26 18:00:00', '2017-12-26 18:30:00', '2017-12-26 20:15:00', '2017-12-26 20:30:00', '2017-12-26 22:00:00', '2017-12-27 00:00:00', '2017-12-27 01:15:00', '2017-12-27 03:30:00', '2017-12-27 04:45:00', '2017-12-27 05:00:00', '2017-12-27 06:45:00', '2017-12-27 08:30:00', '2017-12-27 09:00:00', '2017-12-27 09:45:00', '2017-12-27 11:15:00', '2017-12-27 12:00:00', '2017-12-27 15:00:00', '2017-12-27 15:45:00', '2017-12-27 16:00:00', '2017-12-27 16:15:00', '2017-12-27 19:00:00', '2017-12-27 20:45:00', '2017-12-27 21:30:00', '2017-12-27 22:15:00', '2017-12-27 22:30:00', '2017-12-28 00:45:00', '2017-12-28 01:15:00', '2018-04-02 22:30:00', '2018-04-02 23:15:00', '2018-04-02 23:30:00', '2018-04-03 00:00:00', '2018-04-03 00:30:00', '2018-04-03 00:45:00', '2018-04-03 01:00:00', '2018-04-03 01:15:00', '2018-04-03 01:30:00', '2018-04-06 02:45:00', '2018-04-06 03:00:00', '2018-04-06 03:45:00', '2018-04-06 04:15:00', '2018-04-06 05:00:00', '2018-04-06 06:15:00', '2018-04-06 06:45:00', '2018-04-06 07:00:00', '2018-04-06 07:15:00', '2018-04-06 07:45:00', '2018-04-06 08:30:00', '2018-04-06 08:45:00', '2018-04-06 09:45:00', '2018-04-06 10:15:00', '2018-04-06 10:45:00', '2018-04-06 11:00:00', '2018-04-06 12:30:00', '2018-04-06 12:45:00', '2018-04-06 13:00:00', '2018-04-06 13:30:00', '2018-04-06 13:45:00', '2018-04-06 14:15:00', '2018-04-06 14:45:00', '2018-04-06 16:15:00', '2018-04-06 16:30:00', '2018-04-06 17:15:00', '2018-04-06 17:30:00', '2018-04-06 18:30:00', '2018-04-06 20:00:00', '2018-04-06 20:45:00', '2018-04-06 21:15:00', '2018-04-06 21:45:00', '2018-04-07 00:30:00', '2018-04-07 00:45:00', '2018-04-07 01:00:00', '2018-04-07 01:30:00']
