from sqlalchemy import Column, Integer, ForeignKey, Date, String
from sqlalchemy.orm import relationship
from . import Base

class Loan(Base):
    __tablename__ = "loans"
    id = Column(Integer, primary_key=True)
    borrower_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    deck_id = Column(Integer, ForeignKey("decks.id"), nullable=True)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=True)
    status = Column(String, default="pending")  # pending, active, returned, overdue, etc.
    notes = Column(String, nullable=True)

    borrower = relationship("User", foreign_keys=[borrower_id])
    owner = relationship("User", foreign_keys=[owner_id])
    deck = relationship("Deck")

    items = relationship("LoanItem", back_populates="loan", cascade="all, delete-orphan")

    def __repr__(self):
        return (f"<Loan id={self.id}, borrower_id={self.borrower_id}, "
                f"owner_id={self.owner_id}, deck_id={self.deck_id}, status={self.status}>")
