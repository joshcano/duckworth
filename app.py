from flask import Flask, render_template
from datetime import datetime
from database import session, Dataset, PowerProduction, BatteryPercentageState, PowerFeedIn, PowerSelfConsumption, PowerPurchased, PowerConsumption

app = Flask(__name__)

app.debug = True

@app.route('/')
def index():
  return render_template('index.html', datasets = session.query(Dataset).all())

@app.route('/dataset/<dataset_id>')
def dataset(dataset_id):
  return render_template('dataset.html', dataset = session.query(Dataset).get(dataset_id))

if __name__ == '__main__':
  app.run(host='0.0.0.0')
