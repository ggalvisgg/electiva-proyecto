"""
This module contains the Pydantic model for category recipe data.
"""
from pydantic import BaseModel

class CategoryRecipe(BaseModel):
    """
    Category Recipe model class.
    Attributes:
        idCategoryRecipe (int): The unique identifier of the category recipe.
        nameCategoryRecipe (str): The name of the category recipe.
        descriptionCategoryRecipe (str): The description of the category recipe.
    """
    idCategoryRecipe : int
    nameCategoryRecipe : str
    descriptionCategoryRecipe : str
