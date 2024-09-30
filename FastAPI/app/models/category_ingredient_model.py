"""
This module contains the Pydantic model for category ingredient data.
"""

from pydantic import BaseModel

class CategoryIngredient(BaseModel):
    """
    Category Ingredient model class.
    Attributes:
        idCategoryIngredient (int): The unique identifier of the category ingredient.
        nameCategoryIngredient (str): The name of the category ingredient.
        descriptionCategoryIngredient (str): The description of the category ingredient.
    """
    idCategoryIngredient : int
    nameCategoryIngredient : str
    descriptionCategoryIngredient : str
