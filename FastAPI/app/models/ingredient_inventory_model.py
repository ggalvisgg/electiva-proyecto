"""
This module contains the Pydantic model for ingredient inventory data.
"""
from datetime import date
from pydantic import BaseModel

class IngredientInventory(BaseModel):
    """
    Ingredient Inventory model class.
    Attributes:
        idIngredientInventory (int): The unique identifier of the ingrdient inventory.
        name (str): The name of the ingredient inventory.
        amount (float): The amount of the ingredient inventory.
        unit (str): The unit of the ingredient inventory.
        dateExpiration (date): The date of expiration of the ingredient inventory.
    """
    idIngredientInventory : int
    name : str
    amount : float
    unit : str
    dateExpiration : date
    