"""
This module contains the routes for managing recipe data.
"""
from fastapi import APIRouter, Body, HTTPException
from peewee import DoesNotExist
from app.models.recipe_model import Recipe
from app.services.recipe_service import (
    create_recipe_service,
    get_all_recipes_service,
    get_recipe_service,
    update_recipe_service,
    delete_recipe_service
)

recipe_router = APIRouter()

@recipe_router.post("/")
def create_recipe(recipe: Recipe = Body(...)):
    """
    Creates a new recipe in the database.

    Parameters:
        recipe (Recipe): An object containing the recipe details.
        
    Returns:
        The created recipe object.
    """

    return create_recipe_service(recipe)

@recipe_router.get("/{recipe_id}")
def read_recipe(recipe_id: int):
    """
    Retrieves a recipe by their ID.
    Args:
        recipe_id (int): The ID of the recipe to retrieve.
    Returns:
        Recipe: The recipe object.
    Raises:
        HTTPException: If the recipe is not found.
    """

    try:
        return get_recipe_service(recipe_id)
    except DoesNotExist as exc:
        raise HTTPException(status_code=404, detail="Recipe not found") from exc
    
@recipe_router.get("/")
def read_recipes():
    """
    Reads and returns all recipes.
    Returns:
        List[Recipe]: A list of all recipes.
    """

    return get_all_recipes_service()

@recipe_router.put("/{recipe_id}")
def update_recipe(recipe_id: int, recipe_data: Recipe = Body(...)):
    """
    Update a user with the given recipe_id and recipe_data.
    Parameters:
    - recipe_id (int): The ID of the recipe to update.
    - recipe_data (Recipe): The updated recipe data.
    Returns:
    - The updated recipe object.
    Raises:
    - HTTPException: If the recipe with the given ID does not exist.
    """
    try:
        return update_recipe_service(recipe_id, recipe_data)
    except DoesNotExist as exc:
        raise HTTPException(status_code=404, detail="Recipe not found") from exc
    
@recipe_router.delete("/{recipe_id}")
def delete_recipe(recipe_id: int):
    """
    Delete a recipe with the given recipe_id.
    Args:
    - recipe_id (int): The ID of the recipe to be delete.
    Returns:
    - NOne
    Raises:
    - HTTPException: If the recipe does not exist.
    """
    try:
        return delete_recipe_service(recipe_id)
    except DoesNotExist as exc:
        raise HTTPException(status_code=404, detail="Recipe not found") from exc
    