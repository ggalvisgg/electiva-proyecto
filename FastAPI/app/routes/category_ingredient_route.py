"""
This module contains the routes for managing category ingredient data.
"""

from fastapi import APIRouter, Body, HTTPException
from peewee import DoesNotExist
from app.models.category_ingredient_model import CategoryIngredient
from app.services.category_ingredient_service import (
    create_category_ingredient_service,
    get_all_category_ingredients_service,
    get_category_ingredient_service,
    update_category_ingredient_service,
    delete_category_ingredient_service
)

category_ingredient_router = APIRouter()

@category_ingredient_router.post("/")
def create_category_ingredient(category_ingredient: CategoryIngredient = Body(...)):
    """
    Creates a new category ingredient in the database.

    Parameters:
        category_ingredient (CategoryIngredient): An object containing 
        the category ingredient details.
        
    Returns:
        The created category ingredient object.
    """
    return create_category_ingredient_service(category_ingredient)

@category_ingredient_router.get("/{category_ingredient_id}")
def read_category_ingredient(category_ingredient_id: int):
    """
    Retrieves a category ingredient by its ID.

    Args:
        category_ingredient_id (int): The ID of the category ingredient to retrieve.

    Returns:
        CategoryIngredient: The category ingredient object.

    Raises:
        HTTPException: If the category ingredient is not found.
    """
    try:
        return get_category_ingredient_service(category_ingredient_id)
    except DoesNotExist as exc:
        raise HTTPException(status_code=404, detail="CategoryIngredient not found") from exc

@category_ingredient_router.get("/")
def read_category_ingredients():
    """
    Reads and returns all category ingredients.

    Returns:
        List[CategoryIngredient]: A list of all category ingredients.
    """
    return get_all_category_ingredients_service()

@category_ingredient_router.put("/{category_ingredient_id}")
def update_category_ingredient(category_ingredient_id: int, 
                               category_ingredient_data: CategoryIngredient = Body(...)):
    """
    Update a category ingredient with the given category_ingredient_id and category_ingredient_data.

    Parameters:
        category_ingredient_id (int): The ID of the category ingredient to update.
        category_ingredient_data (CategoryIngredient): The updated category ingredient data.

    Returns:
        The updated category ingredient object.

    Raises:
        HTTPException: If the category ingredient with the given ID does not exist.
    """
    try:
        return update_category_ingredient_service(category_ingredient_id, category_ingredient_data)
    except DoesNotExist as exc:
        raise HTTPException(status_code=404, detail="CategoryIngredient not found") from exc

@category_ingredient_router.delete("/{category_ingredient_id}")
def delete_category_ingredient(category_ingredient_id: int):
    """
    Delete a category ingredient with the given category_ingredient_id.

    Args:
        category_ingredient_id (int): The ID of the category ingredient to be deleted.

    Returns:
        None

    Raises:
        HTTPException: If the category ingredient does not exist.
    """
    try:
        return delete_category_ingredient_service(category_ingredient_id)
    except DoesNotExist as exc:
        raise HTTPException(status_code=404, detail="CategoryIngredient not found") from exc

# Asegúrate de que haya una línea en blanco al final del archivo
