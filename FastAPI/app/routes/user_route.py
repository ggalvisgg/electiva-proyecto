"""
This module contains the routes for managing user data.
"""

from fastapi import APIRouter, Body, HTTPException
from peewee import DoesNotExist
from app.models.user_model import User
from app.services.user_service import (
    create_user_service,
    get_all_users_service,
    get_user_service,
    update_user_service,
    delete_user_service
)

user_router = APIRouter()

@user_router.post("/")
def create_user(user: User = Body(...)):
    """
    Creates a new user in the database.

    Parameters:
        user (User): An object containing the user details.
        
    Returns:
        The created user object.
    """
    return create_user_service(user)

@user_router.get("/{user_id}")
def read_user(user_id: int):
    """
    Retrieves a user by their ID.

    Args:
        user_id (int): The ID of the user to retrieve.

    Returns:
        User: The user object.

    Raises:
        HTTPException: If the user is not found.
    """
    try:
        return get_user_service(user_id)
    except DoesNotExist as exc:
        raise HTTPException(status_code=404, detail="User not found") from exc
    
@user_router.get("/")
def read_users():
    """
    Reads and returns all users.

    Returns:
        List[User]: A list of all users.
    """
    return get_all_users_service()

@user_router.put("/{user_id}")
def update_user(user_id: int, user_data: User = Body(...)):
    """
    Update a user with the given user_id and user_data.

    Parameters:
        user_id (int): The ID of the user to update.
        user_data (User): The updated user data.

    Returns:
        The updated user object.

    Raises:
        HTTPException: If the user with the given ID does not exist.
    """
    try:
        return update_user_service(user_id, user_data)
    except DoesNotExist as exc:
        raise HTTPException(status_code=404, detail="User not found") from exc
    
@user_router.delete("/{user_id}")
def delete_user(user_id: int):
    """
    Delete a user with the given user_id.

    Args:
        user_id (int): The ID of the user to be deleted.

    Returns:
        None

    Raises:
        HTTPException: If the user does not exist.
    """
    try:
        return delete_user_service(user_id)
    except DoesNotExist as exc:
        raise HTTPException(status_code=404, detail="User not found") from exc


