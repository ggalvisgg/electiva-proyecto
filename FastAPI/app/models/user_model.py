"""
This module contains the Pydantic model for customer data.
"""
from pydantic import BaseModel

class User(BaseModel):
    """
    User model class.
    Attributes:
        id (str): The unique identifier of the user.
        name (str): The name of the user.
        password (str): The password of the user.
        email (str): The email address of the user.
        photo (str): The photo of the user.
    """
    idUser : str
    name : str
    password : str
    email : str
    photo : str
