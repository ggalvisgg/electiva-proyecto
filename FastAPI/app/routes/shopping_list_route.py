"""
This module contains the routes for managing shoppingList data.
"""
from fastapi import APIRouter, Body, HTTPException
from peewee import DoesNotExist
from app.models.shopping_list_model import ShoppingList
from app.services.shopping_list_service import (
    create_shopping_list_service,
    get_all_shopping_lists_service,
    get_shopping_list_service,
    #update_shopping_list_service,
    delete_shopping_list_service
)

shopping_list_router = APIRouter()

@shopping_list_router.post("/")
def create_shopping_list(shopping_list: ShoppingList = Body(...)):
    """
    Creates a new shoppingList in the database.

    Parameters:
        shopping_list (ShoppingList): An object containing the shoppingList details.
        
    Returns:
        The created shoppingList object.
    """
    return create_shopping_list_service(shopping_list)

@shopping_list_router.get("/{shopping_list_id}")
def read_shopping_list(shopping_list_id: int):
    """
    Retrieves a shoppingList by its ID.

    Args:
        shopping_list_id (int): The ID of the shoppingList to retrieve.

    Returns:
        ShoppingList: The shoppingList object.

    Raises:
        HTTPException: If the shoppingList is not found.
    """
    try:
        return get_shopping_list_service(shopping_list_id)
    except DoesNotExist as exc:
        raise HTTPException(status_code=404, detail="ShoppingList not found") from exc

@shopping_list_router.get("/")
def read_shopping_lists():
    """
    Reads and returns all shoppingLists.

    Returns:
        List[ShoppingList]: A list of all shoppingLists.
    """
    return get_all_shopping_lists_service()

# @shopping_list_router.put("/{shopping_list_id}")
# def update_shopping_list(shopping_list_id: int, shopping_list_data: ShoppingList = Body(...)):
#     """
#     Update a shoppingList with the given shopping_list_id and shopping_list_data.

#     Parameters:
#         shopping_list_id (int): The ID of the shoppingList to update.
#         shopping_list_data (ShoppingList): The updated shoppingList data.

#     Returns:
#         The updated shoppingList object.

#     Raises:
#         HTTPException: If the shoppingList with the given ID does not exist.
#     """
#     try:
#         return update_shopping_list_service(shopping_list_id, shopping_list_data)
#     except DoesNotExist as exc:
#         raise HTTPException(status_code=404, detail="ShoppingList not found") from exc

@shopping_list_router.delete("/{shopping_list_id}")
def delete_shopping_list(shopping_list_id: int):
    """
    Delete a shoppingList with the given shopping_list_id.

    Args:
        shopping_list_id (int): The ID of the shoppingList to be deleted.

    Returns:
        None

    Raises:
        HTTPException: If the shoppingList does not exist.
    """
    try:
        return delete_shopping_list_service(shopping_list_id)
    except DoesNotExist as exc:
        raise HTTPException(status_code=404, detail="ShoppingList not found") from exc
    