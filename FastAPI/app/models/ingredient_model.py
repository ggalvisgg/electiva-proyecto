"""
This module contains the Pydantic model for ingredient data.
"""
from datetime import date
from pydantic import BaseModel

class Ingredient(BaseModel):
    """
    Ingredient model class.
    Attributes:
        idIngredient (int): The unique identifier of the ingredient.
        nameIngredient (str): The name of the ingredient.
        amountIngredient (float): The amount of the ingredient.
        unitIngredient (str): The unit of the ingredient.
        dateExpirationIngredient (date): The date of expiration of the ingredient.
    """
    idIngredient : int
    nameIngredient : str
    amountIngredient : float
    unitIngredient : str
    dateExpirationIngredient : date
