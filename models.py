from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
from database import Base
import enum


class UserRole(enum.Enum):
    USER_DEFAULT = "user"
    USER_ADMIN = "admin"


class TaskStatus(enum.Enum):
    TODO = "TODO"
    IN_PROGRESS = "In progress"
    DONE = "Done"


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role = Column(Enum(UserRole), default=UserRole.USER_DEFAULT)
    tasks = relationship("Task", back_populates="responsible_person")


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, nullable=True)
    status = Column(Enum(TaskStatus), default=TaskStatus.TODO)
    priority = Column(Integer, default=1)
    responsible_person_id = Column(Integer, ForeignKey("users.id"))
    responsible_person = relationship("User", back_populates="tasks")
