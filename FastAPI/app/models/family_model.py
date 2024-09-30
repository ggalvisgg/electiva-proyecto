"""
This module contains the Pydantic model for family data.
"""
from pydantic import BaseModel

class Family(BaseModel):
    """
    Family model class.
    Attributes:
        idFamily (int): The unique identifier of the user.
        nameFamily (str): The name of the user.
    """
    idFamily : int
    nameFamily : str
