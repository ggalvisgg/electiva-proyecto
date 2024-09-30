"""
This module contains the routes for managing family data.
"""
from fastapi import APIRouter, Body, HTTPException
from peewee import DoesNotExist
from app.models.family_model import Family
from app.services.family_service import (
    create_family_service,
    get_all_families_service,
    get_family_service,
    update_family_service,
    delete_family_service
)

family_router = APIRouter()

@family_router.post("/")
def create_family(family: Family = Body(...)):
    """
    Creates a new family in the database.

    Parameters:
        family (Family): An object containing the family details.
        
    Returns:
        The created family object.
    """
    return create_family_service(family)

@family_router.get("/{family_id}")
def read_family(family_id: int):
    """
    Retrieves a family by its ID.

    Args:
        family_id (int): The ID of the family to retrieve.

    Returns:
        Family: The family object.

    Raises:
        HTTPException: If the family is not found.
    """
    try:
        return get_family_service(family_id)
    except DoesNotExist as exc:
        raise HTTPException(status_code=404, detail="Family not found") from exc

@family_router.get("/")
def read_families():
    """
    Reads and returns all families.

    Returns:
        List[Family]: A list of all families.
    """
    return get_all_families_service()

@family_router.put("/{family_id}")
def update_family(family_id: int, family_data: Family = Body(...)):
    """
    Update a family with the given family_id and family_data.

    Parameters:
        family_id (int): The ID of the family to update.
        family_data (Family): The updated family data.

    Returns:
        The updated family object.

    Raises:
        HTTPException: If the family with the given ID does not exist.
    """
    try:
        return update_family_service(family_id, family_data)
    except DoesNotExist as exc:
        raise HTTPException(status_code=404, detail="Family not found") from exc

@family_router.delete("/{family_id}")
def delete_family(family_id: int):
    """
    Delete a family with the given family_id.

    Args:
        family_id (int): The ID of the family to be deleted.

    Returns:
        None

    Raises:
        HTTPException: If the family does not exist.
    """
    try:
        return delete_family_service(family_id)
    except DoesNotExist as exc:
        raise HTTPException(status_code=404, detail="Family not found") from exc
    