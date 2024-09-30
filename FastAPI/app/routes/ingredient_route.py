"""
This module contains the routes for managing ingredient data.
"""

from fastapi import APIRouter, Body, HTTPException
from peewee import DoesNotExist
from app.models.ingredient_model import Ingredient
from app.services.ingredient_service import (
    create_ingredient_service,
    get_all_ingredients_service,
    get_ingredient_service,
    update_ingredient_service,
    delete_ingredient_service
)

ingredient_router = APIRouter()

@ingredient_router.post("/")
def create_ingredient(ingredient: Ingredient = Body(...)):
    """
    Creates a new ingredient in the database.

    Parameters:
        ingredient (Ingredient): An object containing the ingredient details.
        
    Returns:
        The created ingredient object.
    """
    return create_ingredient_service(ingredient)

@ingredient_router.get("/{ingredient_id}")
def read_ingredient(ingredient_id: int):
    """
    Retrieves an ingredient by its ID.

    Args:
        ingredient_id (int): The ID of the ingredient to retrieve.

    Returns:
        Ingredient: The ingredient object.

    Raises:
        HTTPException: If the ingredient is not found.
    """
    try:
        return get_ingredient_service(ingredient_id)
    except DoesNotExist as exc:
        raise HTTPException(status_code=404, detail="Ingredient not found") from exc
    
@ingredient_router.get("/")
def read_ingredients():
    """
    Reads and returns all ingredients.

    Returns:
        List[Ingredient]: A list of all ingredients.
    """
    return get_all_ingredients_service()

@ingredient_router.put("/{ingredient_id}")
def update_ingredient(ingredient_id: int, ingredient_data: Ingredient = Body(...)):
    """
    Update an ingredient with the given ingredient_id and ingredient_data.

    Parameters:
        ingredient_id (int): The ID of the ingredient to update.
        ingredient_data (Ingredient): The updated ingredient data.

    Returns:
        The updated ingredient object.

    Raises:
        HTTPException: If the ingredient with the given ID does not exist.
    """
    try:
        return update_ingredient_service(ingredient_id, ingredient_data)
    except DoesNotExist as exc:
        raise HTTPException(status_code=404, detail="Ingredient not found") from exc
    
@ingredient_router.delete("/{ingredient_id}")
def delete_ingredient(ingredient_id: int):
    """
    Delete an ingredient with the given ingredient_id.

    Args:
        ingredient_id (int): The ID of the ingredient to be deleted.

    Returns:
        None

    Raises:
        HTTPException: If the ingredient does not exist.
    """
    try:
        return delete_ingredient_service(ingredient_id)
    except DoesNotExist as exc:
        raise HTTPException(status_code=404, detail="Ingredient not found") from exc
