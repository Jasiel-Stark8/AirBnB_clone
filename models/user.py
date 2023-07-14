# models/user.py

class User(BaseModel):
    def __init__(self, *args, **kwargs):
        """Initialize user"""
        super().__init__(*args, **kwargs)  
        if kwargs:
            self.email = kwargs.get("email")
            self.password = kwargs.get("password")
            self.first_name = kwargs.get("first_name")
            self.last_name = kwargs.get("last_name")