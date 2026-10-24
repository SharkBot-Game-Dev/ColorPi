from sqlalchemy import Column, Integer, String
from tools.database import Base

class EconomyUser(Base):
    __tablename__ = "economy_user"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, nullable=False)
    guild_id = Column(String, nullable=False)
    coin = Column(Integer, nullable=False)