from sqlalchemy import create_engine, text

engine = create_engine("sqlite:///backend_data.db", echo=True)