"""
This module contains the routes for managing role data.
"""

from fastapi import APIRouter, Body, HTTPException
from peewee import DoesNotExist
from app.models.role_model import Role
from app.services.role_service import (
    create_role_service,
    get_all_roles_service,
    get_role_service,
    update_role_service,
    delete_role_service
)

role_router = APIRouter()

@role_router.post("/")
def create_role(role: Role = Body(...)):
    """
    Creates a new role in the database.

    Parameters:
        role (Role): An object containing the role details.
        
    Returns:
        The created role object.
    """
    return create_role_service(role)

@role_router.get("/{role_id}")
def read_role(role_id: int):
    """
    Retrieves a role by its ID.

    Args:
        role_id (int): The ID of the role to retrieve.

    Returns:
        Role: The role object.

    Raises:
        HTTPException: If the role is not found.
    """
    try:
        return get_role_service(role_id)
    except DoesNotExist as exc:
        raise HTTPException(status_code=404, detail="Role not found") from exc

@role_router.get("/")
def read_roles():
    """
    Reads and returns all roles.

    Returns:
        List[Role]: A list of all roles.
    """
    return get_all_roles_service()

@role_router.put("/{role_id}")
def update_role(role_id: int, role_data: Role = Body(...)):
    """
    Update a role with the given role_id and role_data.

    Parameters:
        role_id (int): The ID of the role to update.
        role_data (Role): The updated role data.

    Returns:
        The updated role object.

    Raises:
        HTTPException: If the role with the given ID does not exist.
    """
    try:
        return update_role_service(role_id, role_data)
    except DoesNotExist as exc:
        raise HTTPException(status_code=404, detail="Role not found") from exc

@role_router.delete("/{role_id}")
def delete_role(role_id: int):
    """
    Delete a role with the given role_id.

    Args:
        role_id (int): The ID of the role to be deleted.

    Returns:
        None

    Raises:
        HTTPException: If the role does not exist.
    """
    try:
        return delete_role_service(role_id)
    except DoesNotExist as exc:
        raise HTTPException(status_code=404, detail="Role not found") from exc
    
    