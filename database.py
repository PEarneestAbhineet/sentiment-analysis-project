from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
import datetime

# Setup
engine = create_engine('sqlite:///sentiment_data.db')
Base = declarative_base()

# Define the table
class SentimentRecord(Base):
    __tablename__ = 'sentiment_results'
    
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    raw_text = Column(String, nullable=False)
    predicted_sentiment = Column(String, default="pending")
    confidence_score = Column(Float, default=0.0)

# Create the tables
Base.metadata.create_all(engine)

# Create the session factory
Session = sessionmaker(bind=engine)
session = Session()
print("Database and table created successfully!")