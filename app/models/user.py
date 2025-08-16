from sqlalchemy import Column, Integer, String
from .import Base

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    full_name = Column(String, nullable=True)
    phone_number = Column(String, nullable=True)
    role = Column(String, default='user')
    
    def __repr__(self):
        return f"<User(id={self.id}, username={self.username}, email={self.email}, full_name={self.full_name}, phone_number={self.phone_number}, role={self.role})>"
