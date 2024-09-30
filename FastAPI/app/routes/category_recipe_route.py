"""
This module contains the routes for managing category_recipe data.
"""
from fastapi import APIRouter, Body, HTTPException
from peewee import DoesNotExist
from app.models.category_recipe_model import CategoryRecipe
from app.services.category_recipe_service import (
    create_category_recipe_service,
    get_all_category_recipes_service,
    get_category_recipe_service,
    update_category_recipe_service,
    delete_category_recipe_service
)

category_recipe_router = APIRouter()

@category_recipe_router.post("/")
def create_category_recipe(category_recipe: CategoryRecipe = Body(...)):
    """
    Creates a new categoryRecipe in the database.

    Parameters:
        category_recipe (CategoryRecipe): An object containing the categoryRecipe details.
        
    Returns:
        The created categoryRecipe object.
    """
    return create_category_recipe_service(category_recipe)

@category_recipe_router.get("/{category_recipe_id}")
def read_category_recipe(category_recipe_id: int):
    """
    Retrieves a categoryRecipe by its ID.

    Args:
        category_recipe_id (int): The ID of the categoryRecipe to retrieve.

    Returns:
        CategoryRecipe: The categoryRecipe object.

    Raises:
        HTTPException: If the categoryRecipe is not found.
    """
    try:
        return get_category_recipe_service(category_recipe_id)
    except DoesNotExist as exc:
        raise HTTPException(status_code=404, detail="CategoryRecipe not found") from exc

@category_recipe_router.get("/")
def read_category_recipes():
    """
    Reads and returns all categoryRecipes.

    Returns:
        List[CategoryRecipe]: A list of all categoryRecipes.
    """
    return get_all_category_recipes_service()

@category_recipe_router.put("/{category_recipe_id}")
def update_category_recipe(category_recipe_id: int, 
                           category_recipe_data: CategoryRecipe = Body(...)):
    """
    Update a categoryRecipe with the given category_recipe_id and category_recipe_data.

    Parameters:
        category_recipe_id (int): The ID of the categoryRecipe to update.
        category_recipe_data (CategoryRecipe): The updated categoryRecipe data.

    Returns:
        The updated categoryRecipe object.

    Raises:
        HTTPException: If the categoryRecipe with the given ID does not exist.
    """
    try:
        return update_category_recipe_service(category_recipe_id, category_recipe_data)
    except DoesNotExist as exc:
        raise HTTPException(status_code=404, detail="CategoryRecipe not found") from exc

@category_recipe_router.delete("/{category_recipe_id}")
def delete_category_recipe(category_recipe_id: int):
    """
    Delete a categoryRecipe with the given category_recipe_id.

    Args:
        category_recipe_id (int): The ID of the categoryRecipe to be deleted.

    Returns:
        None

    Raises:
        HTTPException: If the categoryRecipe does not exist.
    """
    try:
        return delete_category_recipe_service(category_recipe_id)
    except DoesNotExist as exc:
        raise HTTPException(status_code=404, detail="CategoryRecipe not found") from exc
    