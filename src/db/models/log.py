from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from src.db.session import Base


class Log(Base):
    __tablename__ = 'logs'

    id = Column(Integer, primary_key=True, autoincrement=True)
    url_id = Column(Integer, ForeignKey("urls.id"), nullable=False, index=True)
    clicked_at = Column(DateTime(timezone=True),
                        server_default=func.now(), nullable=False)
    ip_address = Column(String(45), nullable=False)

    url = relationship("URL", back_populates="logs")
