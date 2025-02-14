# Database models (SQLAlchemy models)
class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(80), unique=True, nullable=False)
    name = db.Column(db.String(120), nullable=False)
    
    def serialize(self):
        return {'id': self.id, 'symbol': self.symbol, 'name': self.name}
