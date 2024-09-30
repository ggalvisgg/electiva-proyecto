"""
This module contains the routes for managing ingredient inventory data.
"""
from fastapi import APIRouter, Body, HTTPException
from peewee import DoesNotExist
from app.models.ingredient_inventory_model import IngredientInventory
from app.services.ingredient_inventory_service import (
    create_ingredient_inventory_service,
    get_all_ingredient_inventories_service,
    get_ingredient_inventory_service,
    update_ingredient_inventory_service,
    delete_ingredient_inventory_service
)

ingredient_inventory_router = APIRouter()

@ingredient_inventory_router.post("/")
def create_ingredient_inventory(ingredient_inventory: IngredientInventory = Body(...)):
    """
    Creates a new ingredient inventory in the database.

    Parameters:
        ingredient_inventory (IngredientInventory): An object containing the ingredient details.
        
    Returns:
        The created ingredient inventory object.
    """
    return create_ingredient_inventory_service(ingredient_inventory)

@ingredient_inventory_router.get("/{ingredient_inventory_id}")
def read_ingredient_inventory(ingredient_inventory_id: int):
    """
    Retrieves an ingredient inventory by its ID.

    Args:
        ingredient_inventory_id (int): The ID of the ingredient inventory to retrieve.

    Returns:
        IngredientInventory: The ingredient inventory object.

    Raises:
        HTTPException: If the ingredient inventory is not found.
    """
    try:
        return get_ingredient_inventory_service(ingredient_inventory_id)
    except DoesNotExist as exc:
        raise HTTPException(status_code=404, detail="Ingredient inventory not found") from exc
    
@ingredient_inventory_router.get("/")
def read_ingredient_inventories():
    """
    Reads and returns all ingredient inventories.

    Returns:
        List[IngredientInventory]: A list of all ingredient inventories.
    """
    return get_all_ingredient_inventories_service()

@ingredient_inventory_router.put("/{ingredient_inventory_id}")
def update_ingredient_inventory(ingredient_inventory_id: int, 
                                ingredient_inventory_data: IngredientInventory = Body(...)):
    """
    Update an ingredient inventory with the given 
    ingredient_inventory_id and ingredient_inventory_data.

    Parameters:
        ingredient_inventory_id (int): The ID of the ingredient inventory to update.
        ingredient_inventory_data (IngredientInventory): The updated ingredient inventory data.

    Returns:
        The updated ingredient inventory object.

    Raises:
        HTTPException: If the ingredient inventory with the given ID does not exist.
    """
    try:
        return update_ingredient_inventory_service(ingredient_inventory_id, 
                                                   ingredient_inventory_data)
    except DoesNotExist as exc:
        raise HTTPException(status_code=404, detail="Ingredient inventory not found") from exc
    
@ingredient_inventory_router.delete("/{ingredient_inventory_id}")
def delete_ingredient_inventory(ingredient_inventory_id: int):
    """
    Delete an ingredient inventory with the given ingredient_inventory_id.

    Args:
        ingredient_inventory_id (int): The ID of the ingredient inventory to be deleted.

    Returns:
        None

    Raises:
        HTTPException: If the ingredient inventory does not exist.
    """
    try:
        return delete_ingredient_inventory_service(ingredient_inventory_id)
    except DoesNotExist as exc:
        raise HTTPException(status_code=404, detail="Ingredient inventory not found") from exc
