from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import relationship
from src.db.session import Base


class URL(Base):
    __tablename__ = 'urls'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False, index=True)
    campaign_id = Column(Integer, nullable=False, index=True)
    original_url = Column(String(2048), nullable=False)
    short_code = Column(String(8), nullable=False, unique=True, index=True)
    created_at = Column(DateTime(timezone=True),
                        server_default=func.now(), nullable=False)
    views = Column(Integer, default=0, nullable=False)

    logs = relationship("Log", back_populates="url",
                        cascade="all, delete-orphan")
