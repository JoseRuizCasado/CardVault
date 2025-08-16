from sqlalchemy import Column, Integer, String, Boolean, Float, Enum

from app.models.enums import CardColorEnum
from .import Base


class Card(Base):
    __tablename__ = 'cards'
    
    # TODO: change to collection model detail that change the value of the card.
    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    color = Column(Enum(CardColorEnum), nullable=True)
    edition = Column(String, nullable=True)
    rarity = Column(String, nullable=True)
    cmc = Column(Float, nullable=True)
    card_type = Column(String, nullable=True)

    def __repr__(self):
        return f"<Card(id={self.id}, name={self.name}, color={self.color}, edition={self.edition}, rarity={self.rarity}, cmc={self.cmc}, card_type={self.card_type})>"
