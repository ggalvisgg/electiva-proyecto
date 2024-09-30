"""This module contains the service functions for the categoryIngredient class."""
from app.models.category_ingredient_model import CategoryIngredient

def create_category_ingredient_service(category_ingredient):
    """
    Creates a new categoryIngredient in the database.

    Args:
        category_ingredient (CategoryIngredient): An object containing the 
        categoryIngredient details.
        
    Returns:
        CategoryIngredientModel: The created categoryIngredient record.
    """
    category_ingredient_record = CategoryIngredient.create(
        idCategoryIngredient=category_ingredient.idCategoryIngredient,
        nameCategoryIngredient=category_ingredient.nameCategoryIngredient,
        descriptionCategoryIngredient=category_ingredient.descriptionCategoryIngredient
    )
    return category_ingredient_record

def get_category_ingredient_service(category_ingredient_id: int):
    """
    Retrieves a categoryIngredient by its ID.

    Args:
        category_ingredient_id (int): The unique identifier of the categoryIngredient.

    Returns:
        DICT: A dictionary containing the categoryIngredient's details.
        
    Raises:
        DoesNotExist: If the categoryIngredient with the given ID does not exist.
    """
    category_ingredient = CategoryIngredient.get_by_id(category_ingredient_id)
    return {
        "id": category_ingredient.idCategoryIngredient,
        "name": category_ingredient.nameCategoryIngredient,
        "description": category_ingredient.descriptionCategoryIngredient
    }

def get_all_category_ingredients_service():
    """
    Retrieves all categoryIngredients from the database.

    Returns:
        List: A list of dictionaries containing the data of each categoryIngredient's details.
    """
    category_ingredients = list(CategoryIngredient.select())
    return [
        {
        "id": category_ingredient.idCategoryIngredient,
        "name": category_ingredient.nameCategoryIngredient,
        "description": category_ingredient.descriptionCategoryIngredient
        }
        for category_ingredient in category_ingredients
    ]

def update_category_ingredient_service(category_ingredient_id: int, 
                                       category_data_i: CategoryIngredient):
    """
    Updates an existing categoryIngredient's details by its ID.

    Args:
        category_ingredient_id (int): The ID of the categoryIngredient to update.
        category_ingredient_data (CategoryIngredient): An object containing the 
        updated categoryIngredient details.
        
    Returns:
        CategoryIngredientModel: The updated categoryIngredient record.
        
    Raises:
        DoesNotExist: If the categoryIngredient with the given ID does not exist.
    """
    category_ingre = CategoryIngredient.get_by_id(category_ingredient_id)
    category_ingre.nameCategoryIngredient = category_data_i.nameCategoryIngredient
    category_ingre.descriptionCategoryIngredient = category_data_i.descriptionCategoryIngredient
    category_ingre.save()
    return category_ingre

def delete_category_ingredient_service(category_ingredient_id: int):
    """
    Deletes a categoryIngredient from the database by its ID.

    Args:
        category_ingredient_id (int): The ID of the categoryIngredient to delete.
        
    Returns:
        dict: A message confirming the deletion.
        
    Raises:
        DoesNotExist: If the categoryIngredient with the given ID does not exist.
    """
    category_ingredient = CategoryIngredient.get_by_id(category_ingredient_id)
    category_ingredient.delete_instance()
    return {"message": "CategoryIngredient deleted successfully"}
