"""
This module contains the Pydantic model for shopping list data.
"""
from pydantic import BaseModel

class ShoppingList(BaseModel):
    """
    ShoppingList model class.
    Attributes:
        idShoppingList (int): The unique identifier of the shopping list.
    """
    idShoppingList : int
    