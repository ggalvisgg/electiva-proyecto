"""This module contains the service functions for the family class."""
from app.models.family_model import Family

def create_family_service(family):
    """
    Creates a new family in the database.

    Args:
        family (Family): An object containing the family details.
        
    Returns:
        FamilyModel: The created family record.
    """
    family_record = Family.create(
        idFamily=family.idFamily,
        nameFamily=family.nameFamily
    )
    return family_record

def get_family_service(family_id: int):
    """
    Retrieves a family by its ID.

    Args:
        family_id (int): The unique identifier of the family.

    Returns:
        DICT: A dictionary containing the family's details.
        
    Raises:
        DoesNotExist: If the family with the given ID does not exist.
    """
    family = Family.get_by_id(family_id)
    return {
        "id": family.idFamily,
        "name": family.nameFamily
    }

def get_all_families_service():
    """
    Retrieves all families from the database.

    Returns:
        List: A list of dictionaries containing the data of each family's details.
    """
    families = list(Family.select())
    return [
        {
        "id": family.idFamily,
        "name": family.nameFamily
        }
        for family in families
    ]

def update_family_service(family_id: int, family_data: Family):
    """
    Updates an existing family's details by its ID.

    Args:
        family_id (int): The ID of the family to update.
        family_data (Family): An object containing the updated family details.
        
    Returns:
        FamilyModel: The updated family record.
        
    Raises:
        DoesNotExist: If the family with the given ID does not exist.
    """
    family = Family.get_by_id(family_id)
    family.nameFamily = family_data.nameFamily
    family.save()
    return family

def delete_family_service(family_id: int):
    """
    Deletes a family from the database by its ID.

    Args:
        family_id (int): The ID of the family to delete.
        
    Returns:
        dict: A message confirming the deletion.
        
    Raises:
        DoesNotExist: If the family with the given ID does not exist.
    """
    family = Family.get_by_id(family_id)
    family.delete_instance()
    return {"message": "Family deleted successfully"}
