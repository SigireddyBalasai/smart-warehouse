from quart_sqlalchemy import SQLAlchemy
from app import get_app, get_db,create_database
import json
from quart_sqlalchemy import SQLAlchemy
import asyncio
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
app = get_app()
db = get_db()

class Data(db.Model, Base):
    """Data model"""
    timestamp = db.Column(db.String, primary_key=True)
    temperature = db.Column(db.Integer, nullable=False)
    humidity = db.Column(db.Integer, nullable=False)
    gas = db.Column(db.Integer, nullable=False)
    __abstract__ = True
    def __repr__(self):
        """Return a string representation of a data"""
        return f"Data('{self.timestamp}', '{self.temperature}', '{self.humidity}', '{self.gas}')"

    def to_dict(self):
        """Convert a data to a dictionary"""
        return {
            "timestamp": self.timestamp,
            "temperature": self.temperature,
            "humidity": self.humidity,
            "gas": self.gas
        }

    def to_json(self):
        """Convert a data to a json string"""
        return json.dumps(self.to_dict())

    def from_dict(self, data):
        """Load a data from a dictionary"""
        for field in ["timestamp", "temperature", "humidity", "gas"]:
            if field in data:
                setattr(self, field, data[field])

    def from_json(self, data):
        """Load a data from a json string"""
        return self.from_dict(json.loads(data))

    def save(self):
        """Save a data"""
        db.session.add(self)
        db.session.commit()
        return self

    def delete(self):
        """Delete a data"""
        db.session.remove(self)
        db.session.commit()
        return self

    def update(self):
        """Update a data"""
        db.session.update(self)
        db.session.commit()
        return self

    @staticmethod
    def get_all():
        """Get all data"""
        return Data.query.all()

    @staticmethod
    def get_by_timestamp(timestamp):
        """Get a data by timestamp"""
        return Data.query.filter_by(timestamp=timestamp).first()

    @staticmethod
    def get_by_temperature(temperature):
        """Get a data by temperature"""
        return Data.query.filter_by(temperature=temperature).first()

    @staticmethod
    def get_by_humidity(humidity):
        """Get a data by humidity"""
        return Data.query.filter_by(humidity=humidity).first()


class GetDataBase:
    def __init__(self):
        self.classes = {}

    def add_database(self, name):
        """Add a new database class"""
        if name in self.classes:
            raise ValueError("Class already exists")

        self.classes[name] = type(name, (Data,), {})
        self.classes[name].__tablename__ = name
        print(self.classes[name].__tablename__)
        print(self.classes[name].__name__)
        create_database()
        db.create_all()
        print("Database created")
        return self.classes[name]

    def get_database(self, name):
        """Get a database class"""
        if name not in self.classes:
            raise ValueError("Class does not exist")
        return self.classes[name]
       
def add_data(data_id,timestamp,temperature,humidity,gas):
    """Add data to the database"""
    print(data_id)
    db_finder = GetDataBase()
    if data_id not in db_finder.classes:
        database = db_finder.add_database(data_id)
    database = db_finder.get_database(data_id)
    data = database()
    data.timestamp = timestamp
    data.temperature = temperature
    data.humidity = humidity
    data.gas = gas
    data.save()
    
    return data

def get_app():
    """Get a quart app"""
    return app
