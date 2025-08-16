from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from . import Base


class LoanItem(Base):
    __tablename__ = "loan_items"
    id = Column(Integer, primary_key=True)
    loan_id = Column(Integer, ForeignKey("loans.id"), nullable=False)
    collection_entry_id = Column(Integer, ForeignKey("collection_entries.id"), nullable=False)
    amount = Column(Integer, nullable=False, default=1)

    loan = relationship("Loan", back_populates="items")
    collection_entry = relationship("CollectionEntry")

    def __repr__(self):
        return f"<LoanItem loan_id={self.loan_id}, collection_entry_id={self.collection_entry_id}, amount={self.amount}>"
