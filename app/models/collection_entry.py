from sqlalchemy import Column, Integer, ForeignKey, Boolean, Float, String
from sqlalchemy.orm import relationship
from . import Base


class CollectionEntry(Base):
    __tablename__ = "collection_entries"
    id = Column(Integer, primary_key=True)
    card_id = Column(Integer, ForeignKey("cards.id"))
    owner_id = Column(Integer, ForeignKey("users.id"))
    amount = Column(Integer, nullable=False, default=1)
    for_sale = Column(Boolean, default=False)
    price_bought = Column(Float, nullable=True)
    location = Column(String, nullable=True)
    is_foil = Column(Boolean, default=False)
    is_signed = Column(Boolean, default=False)
    condition = Column(String, nullable=True)
    language = Column(String, nullable=True)

    card = relationship("Card")
    owner = relationship("User")

    def __repr__(self):
        return f"<CollectionEntry(id={self.id}, card_id={self.card_id}, owner_id={self.owner_id}, amount={self.amount}, for_sale={self.for_sale}, price_bought={self.price_bought}, location={self.location}, is_foil={self.is_foil}, is_signed={self.is_signed}, condition={self.condition}, language={self.language})>"
