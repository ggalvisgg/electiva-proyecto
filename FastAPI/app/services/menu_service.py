"""This module contains the service functions for the menu class."""
from app.models.menu_model import Menu

def create_menu_service(menu):
    """
    Creates a new menu in the database.

    Args:
        menu (Menu): An object containing the menu details.
        
    Returns:
        MenuModel: The created menu record.
    """
    menu_record = Menu.create(
        idMenu=menu.idMenu,
        dateMenu=menu.dateMenu
    )
    return menu_record

def get_menu_service(menu_id: int):
    """
    Retrieves a menu by its ID.

    Args:
        menu_id (int): The unique identifier of the menu.

    Returns:
        DICT: A dictionary containing the menu's details.
        
    Raises:
        DoesNotExist: If the menu with the given ID does not exist.
    """
    menu = Menu.get_by_id(menu_id)
    return {
        "id": menu.idMenu,
        "date": menu.dateMenu
    }

def get_all_menus_service():
    """
    Retrieves all menus from the database.

    Returns:
        List: A list of dictionaries containing the data of each menu's details.
    """
    menus = list(Menu.select())
    return [
        {
        "id": menu.idMenu,
        "date": menu.dateMenu
        }
        for menu in menus
    ]

def update_menu_service(menu_id: int, menu_data: Menu):
    """
    Updates an existing menu's details by its ID.

    Args:
        menu_id (int): The ID of the menu to update.
        menu_data (Menu): An object containing the updated menu details.
        
    Returns:
        MenuModel: The updated menu record.
        
    Raises:
        DoesNotExist: If the menu with the given ID does not exist.
    """
    menu = Menu.get_by_id(menu_id)
    menu.dateMenu = menu_data.dateMenu
    menu.save()
    return menu

def delete_menu_service(menu_id: int):
    """
    Deletes a menu from the database by its ID.

    Args:
        menu_id (int): The ID of the menu to delete.
        
    Returns:
        dict: A message confirming the deletion.
        
    Raises:
        DoesNotExist: If the menu with the given ID does not exist.
    """
    menu = Menu.get_by_id(menu_id)
    menu.delete_instance()
    return {"message": "Menu deleted successfully"}
