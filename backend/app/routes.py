# API routes (e.g., for fetching stock data, handling user requests)
from flask import request, jsonify
from app import app, db
from .models import Stock

@app.route('/stocks', methods=['GET'])
def get_stocks():
    stocks = Stock.query.all()
    return jsonify([stock.serialize() for stock in stocks])

@app.route('/stocks', methods=['POST'])
def add_stock():
    data = request.get_json()
    new_stock = Stock(symbol=data['symbol'], name=data['name'])
    db.session.add(new_stock)
    db.session.commit()
    return jsonify(new_stock.serialize()), 201
