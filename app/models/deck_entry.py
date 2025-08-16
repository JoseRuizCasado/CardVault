from sqlalchemy import Boolean, Column, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from . import Base

class DeckEntry(Base):
    __tablename__ = "deck_entries"

    id = Column(Integer, primary_key=True)
    deck_id = Column(Integer, ForeignKey("decks.id"), nullable=False)
    collection_entry_id = Column(Integer, ForeignKey("collection_entries.id"), nullable=False)
    amount = Column(Integer, nullable=False, default=1)
    sideboard = Column(Boolean, default=False)

    deck = relationship("Deck", back_populates="entries")
    collection_entry = relationship("CollectionEntry")

    def __repr__(self):
        return (f"<DeckEntry(deck_id={self.deck_id}, "
                f"collection_entry_id={self.collection_entry_id}, amount={self.amount})>")