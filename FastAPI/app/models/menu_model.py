"""
This module contains the Pydantic model for menu data.
"""
from datetime import date
from pydantic import BaseModel

class Menu(BaseModel):
    """
    Menu model class.
    Attributes:
        idMenu (int): The unique identifier of the menu.
        dateMenu (date): The date of the menu.
    """
    idMenu : int
    dateMenu : date
