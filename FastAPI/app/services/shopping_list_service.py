"""This module contains the service functions for the shoppingList class."""
from app.models.shopping_list_model import ShoppingList

def create_shopping_list_service(shopping_list):
    """
    Creates a new shoppingList in the database.

    Args:
        shopping_list (ShoppingList): An object containing the shoppingList details.
        
    Returns:
        ShoppingListModel: The created shoppingList record.
    """
    shopping_list_record = ShoppingList.create(
        idShoppingList=shopping_list.idShoppingList
    )
    return shopping_list_record

def get_shopping_list_service(shopping_list_id: int):
    """
    Retrieves a shoppingList by its ID.

    Args:
        shopping_list_id (int): The unique identifier of the shoppingList.

    Returns:
        DICT: A dictionary containing the shoppingList's details.
        
    Raises:
        DoesNotExist: If the shoppingList with the given ID does not exist.
    """
    shopping_list = ShoppingList.get_by_id(shopping_list_id)
    return {
        "id": shopping_list.idShoppingList
    }

def get_all_shopping_lists_service():
    """
    Retrieves all shoppingLists from the database.

    Returns:
        List: A list of dictionaries containing the data of each shoppingList's details.
    """
    shopping_lists = list(ShoppingList.select())
    return [
        {
            "id": shopping_list.idShoppingList
        }
        for shopping_list in shopping_lists
    ]

# def update_shopping_list_service(shopping_list_id: int, shopping_list_data: ShoppingList):
#     """
#     Updates an existing shoppingList's details by its ID.

#     Args:
#         shopping_list_id (int): The ID of the shoppingList to update.
#         shopping_list_data (ShoppingList): An object containing the updated shoppingList details.
        
#     Returns:
#         ShoppingListModel: The updated shoppingList record.
        
#     Raises:
#         DoesNotExist: If the shoppingList with the given ID does not exist.
#     """
#     shopping_list = ShoppingList.get_by_id(shopping_list_id)
#     shopping_list.save()
#     return shopping_list

def delete_shopping_list_service(shopping_list_id: int):
    """
    Deletes a shoppingList from the database by its ID.

    Args:
        shopping_list_id (int): The ID of the shoppingList to delete.
        
    Returns:
        dict: A message confirming the deletion.
        
    Raises:
        DoesNotExist: If the shoppingList with the given ID does not exist.
    """
    shopping_list = ShoppingList.get_by_id(shopping_list_id)
    shopping_list.delete_instance()
    return {"message": "ShoppingList deleted successfully"}
