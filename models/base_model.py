"""Defines all common attributes/methods for other classes"""

from datetime import datetime
import uuid


class BaseModel():
    """Base class for all models"""
    
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow().isoformat()
        self.updated_at = datetime.utcnow().isoformat()

    def __str__(self):
        """Prints Class, and id as a dictionary"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates the public instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.utcnow().isoformat()
    
    def to_dict(self):
        """ returns a dictionary containing all keys/values of __dict__ of the instance"""
        return {
            "__class__": self.__class__.__name__,
            "id": self.id,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
