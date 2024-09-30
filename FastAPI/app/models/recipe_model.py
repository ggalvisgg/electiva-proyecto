"""
This module contains the Pydantic model for recipe data.
"""
from pydantic import BaseModel

class Recipe(BaseModel):
    """
    Recipe model class.
    Attributes:
        idRecipe (int): The unique identifier of the recipe.
        nameRecipe (str): The name of the recipe.
        descriptionRecipe (str): The description of the recipe.
        category (str): The category of the recipe.
        difficulty (str): The difficulty of the recipe.
        timePreparation (int): The time preparation of the recipe.
        instructions (str): The instructions of the recipe.
        nutritionalData (str): The nutritional data of the recipe.
    """
    idRecipe : int
    nameRecipe : str
    descriptionRecipe : str
    category : str
    difficulty : str
    timePreparation : int
    instructions : str
    nutritionalData : str
