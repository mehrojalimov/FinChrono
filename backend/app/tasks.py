# Celery tasks (for background jobs like notifications)
from celery import Celery
from app import celery
from .models import Stock

@celery.task
def send_stock_notification(stock_id):
    stock = Stock.query.get(stock_id)
    # Logic to send notification to the user (via Firebase or other methods)
    print(f"Stock notification sent for: {stock.symbol}")
