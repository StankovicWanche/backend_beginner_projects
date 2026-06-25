from sqlalchemy import Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

# This is the master base class that tracks all of our tables
class Base(DeclarativeBase):
    pass

# This class defines what our database table structure will look like
class StatusLog(Base):
    __tablename__ = "status_log" # The actual name of the table inside SQL

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    status_text: Mapped[str] = mapped_column(String(100), nullable=False)
    

