"""
This module contains the routes for managing menu data.
"""
from fastapi import APIRouter, Body, HTTPException
from peewee import DoesNotExist
from app.models.menu_model import Menu
from app.services.menu_service import (
    create_menu_service,
    get_all_menus_service,
    get_menu_service,
    update_menu_service,
    delete_menu_service
)

menu_router = APIRouter()

@menu_router.post("/")
def create_menu(menu: Menu = Body(...)):
    """
    Creates a new menu in the database.

    Parameters:
        menu (Menu): An object containing the menu details.
        
    Returns:
        The created menu object.
    """
    return create_menu_service(menu)

@menu_router.get("/{menu_id}")
def read_menu(menu_id: int):
    """
    Retrieves a menu by its ID.

    Args:
        menu_id (int): The ID of the menu to retrieve.

    Returns:
        Menu: The menu object.

    Raises:
        HTTPException: If the menu is not found.
    """
    try:
        return get_menu_service(menu_id)
    except DoesNotExist as exc:
        raise HTTPException(status_code=404, detail="Menu not found") from exc

@menu_router.get("/")
def read_menus():
    """
    Reads and returns all menus.

    Returns:
        List[Menu]: A list of all menus.
    """
    return get_all_menus_service()

@menu_router.put("/{menu_id}")
def update_menu(menu_id: int, menu_data: Menu = Body(...)):
    """
    Update a menu with the given menu_id and menu_data.

    Parameters:
        menu_id (int): The ID of the menu to update.
        menu_data (Menu): The updated menu data.

    Returns:
        The updated menu object.

    Raises:
        HTTPException: If the menu with the given ID does not exist.
    """
    try:
        return update_menu_service(menu_id, menu_data)
    except DoesNotExist as exc:
        raise HTTPException(status_code=404, detail="Menu not found") from exc

@menu_router.delete("/{menu_id}")
def delete_menu(menu_id: int):
    """
    Delete a menu with the given menu_id.

    Args:
        menu_id (int): The ID of the menu to be deleted.

    Returns:
        None

    Raises:
        HTTPException: If the menu does not exist.
    """
    try:
        return delete_menu_service(menu_id)
    except DoesNotExist as exc:
        raise HTTPException(status_code=404, detail="Menu not found") from exc


