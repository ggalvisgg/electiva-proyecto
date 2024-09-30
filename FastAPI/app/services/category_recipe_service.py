"""This module contains the service functions for the categoryRecipe class."""
from app.models.category_recipe_model import CategoryRecipe

def create_category_recipe_service(category_recipe):
    """
    Creates a new categoryRecipe in the database.

    Args:
        category_recipe (CategoryRecipe): An object containing the categoryRecipe details.
        
    Returns:
        CategoryRecipeModel: The created categoryRecipe record.
    """
    category_recipe_record = CategoryRecipe.create(
        idCategoryRecipe=category_recipe.idCategoryRecipe,
        nameCategoryRecipe=category_recipe.nameCategoryRecipe,
        descriptionCategoryRecipe=category_recipe.descriptionCategoryRecipe
    )
    return category_recipe_record

def get_category_recipe_service(category_recipe_id: int):
    """
    Retrieves a categoryRecipe by its ID.

    Args:
        category_recipe_id (int): The unique identifier of the categoryRecipe.

    Returns:
        DICT: A dictionary containing the categoryRecipe's details.
        
    Raises:
        DoesNotExist: If the categoryRecipe with the given ID does not exist.
    """
    category_recipe = CategoryRecipe.get_by_id(category_recipe_id)
    return {
        "id": category_recipe.idCategoryRecipe,
        "name": category_recipe.nameCategoryRecipe,
        "description": category_recipe.descriptionCategoryRecipe
    }

def get_all_category_recipes_service():
    """
    Retrieves all categoryRecipes from the database.

    Returns:
        List: A list of dictionaries containing the data of each categoryRecipe's details.
    """
    category_recipes = list(CategoryRecipe.select())
    return [
        {
        "id": category_recipe.idCategoryRecipe,
        "name": category_recipe.nameCategoryRecipe,
        "description": category_recipe.descriptionCategoryRecipe
        }
        for category_recipe in category_recipes
    ]

def update_category_recipe_service(category_recipe_id: int, category_recipe_data: CategoryRecipe):
    """
    Updates an existing categoryRecipe's details by its ID.

    Args:
        category_recipe_id (int): The ID of the categoryRecipe to update.
        category_recipe_data (CategoryRecipe): An object containing 
        the updated categoryRecipe details.
        
    Returns:
        CategoryRecipeModel: The updated categoryRecipe record.
        
    Raises:
        DoesNotExist: If the categoryRecipe with the given ID does not exist.
    """
    category_recipe = CategoryRecipe.get_by_id(category_recipe_id)
    category_recipe.nameCategoryRecipe = category_recipe_data.nameCategoryRecipe
    category_recipe.descriptionCategoryRecipe = category_recipe_data.descriptionCategoryRecipe
    category_recipe.save()
    return category_recipe

def delete_category_recipe_service(category_recipe_id: int):
    """
    Deletes a categoryRecipe from the database by its ID.

    Args:
        category_recipe_id (int): The ID of the categoryRecipe to delete.
        
    Returns:
        dict: A message confirming the deletion.
        
    Raises:
        DoesNotExist: If the categoryRecipe with the given ID does not exist.
    """
    category_recipe = CategoryRecipe.get_by_id(category_recipe_id)
    category_recipe.delete_instance()
    return {"message": "CategoryRecipe deleted successfully"}
