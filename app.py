
from flask import Flask, render_template
import csv
import os

from collections import defaultdict

# Flask MUST see this exact line:
app = Flask(__name__, template_folder='template')

@app.route('/')
def index():
    data = []
    product_prices = defaultdict(list)
    
    # Using the file you forcefully created
    if os.path.exists('market_data.csv'):
        with open('market_data.csv', mode='r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                price = float(row['price'])
                row['recommendation'] = round(price * 0.95, 2)
                data.append(row)
                product_prices[row['product_name']].append(price)
    
    labels = list(product_prices.keys())
    values = [round(sum(prices)/len(prices), 2) for prices in product_prices.values()]
    
    return render_template('frontend.html', data=data, labels=labels, values=values)

if __name__ == '__main__':
    app.run(port=8080)