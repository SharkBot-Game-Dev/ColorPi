from sqlalchemy import JSON, Column, Integer, String
from tools.database import Base

class SlotSymbol(Base):
    __tablename__ = "slot_symbol"

    id = Column(Integer, primary_key=True, index=True)
    guild_id = Column(String, nullable=False)
    symbols = Column(JSON)