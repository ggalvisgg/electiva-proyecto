"""
This module contains the Pydantic model for pantry data.
"""
from pydantic import BaseModel

class Pantry(BaseModel):
    """
    Pantry model class.
    Attributes:
        idPantry (int): The unique identifier of the user.
    """
    idPantry : int
