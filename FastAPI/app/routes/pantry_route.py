"""
This module contains the routes for managing pantry data.
"""
from fastapi import APIRouter, Body, HTTPException
from peewee import DoesNotExist
from app.models.pantry_model import Pantry
from app.services.pantry_service import (
    create_pantry_service,
    get_all_pantries_service,
    get_pantry_service,
    # update_pantry_service,
    delete_pantry_service
)

pantry_router = APIRouter()

@pantry_router.post("/")
def create_pantry(pantry: Pantry = Body(...)):
    """
    Creates a new pantry in the database.

    Parameters:
        pantry (Pantry): An object containing the pantry details.
        
    Returns:
        The created pantry object.
    """
    return create_pantry_service(pantry)

@pantry_router.get("/{pantry_id}")
def read_pantry(pantry_id: int):
    """
    Retrieves a pantry by its ID.

    Args:
        pantry_id (int): The ID of the pantry to retrieve.

    Returns:
        Pantry: The pantry object.

    Raises:
        HTTPException: If the pantry is not found.
    """
    try:
        return get_pantry_service(pantry_id)
    except DoesNotExist as exc:
        raise HTTPException(status_code=404, detail="Pantry not found") from exc

@pantry_router.get("/")
def read_pantries():
    """
    Reads and returns all pantries.

    Returns:
        List[Pantry]: A list of all pantries.
    """
    return get_all_pantries_service()

# @pantry_router.put("/{pantry_id}")
# def update_pantry(pantry_id: int, pantry_data: Pantry = Body(...)):
#     """
#     Update a pantry with the given pantry_id and pantry_data.

#     Parameters:
#         pantry_id (int): The ID of the pantry to update.
#         pantry_data (Pantry): The updated pantry data.

#     Returns:
#         The updated pantry object.

#     Raises:
#         HTTPException: If the pantry with the given ID does not exist.
#     """
#     try:
#         return update_pantry_service(pantry_id, pantry_data)
#     except DoesNotExist as exc:
#         raise HTTPException(status_code=404, detail="Pantry not found") from exc

@pantry_router.delete("/{pantry_id}")
def delete_pantry(pantry_id: int):
    """
    Delete a pantry with the given pantry_id.

    Args:
        pantry_id (int): The ID of the pantry to be deleted.

    Returns:
        None

    Raises:
        HTTPException: If the pantry does not exist.
    """
    try:
        return delete_pantry_service(pantry_id)
    except DoesNotExist as exc:
        raise HTTPException(status_code=404, detail="Pantry not found") from exc
