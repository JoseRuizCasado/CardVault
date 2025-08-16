from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

class Deck(Base):
    __tablename__ = "decks"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    description = Column(String, nullable=True)

    owner = relationship("User", backref="decks")
    entries = relationship(
        "DeckEntry",
        back_populates="deck",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Deck(id={self.id}, name='{self.name}', owner_id={self.owner_id})>"
